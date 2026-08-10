import { reactive } from "vue";


import workspaceConfig 
from "../config/workspace.json";


const STORAGE_KEY =
"gray_workspace_layout";




function loadState(){


    const saved =
    localStorage.getItem(
        STORAGE_KEY
    );


    if(saved){


        try{


            return JSON.parse(saved);


        }catch(e){


            console.warn(
                "workspace state invalid"
            );


        }


    }




    return {


        panels:
        structuredClone(
            workspaceConfig.panels
        ),


        closedPanels:[]

    };


}






const state = reactive(
    loadState()
);








function save(){


    localStorage.setItem(

        STORAGE_KEY,

        JSON.stringify({

            panels:
            state.panels,


            closedPanels:
            state.closedPanels


        })

    );


}







function move(
    panel,
    position
){


    panel.position.x =
    position.x;


    panel.position.y =
    position.y;



    save();


}








function resize(
    panel,
    size
){


    panel.width =
    size.width;


    panel.height =
    size.height;



    save();


}








function rotate(
    panel,
    angle
){


    panel.rotate =
    angle;


    save();


}








function focus(panel){


    const maxZ =

    Math.max(

        ...state.panels.map(

            item=>
            item.zIndex || 1

        )

    );



    panel.zIndex =
    maxZ + 1;



    save();


}









function close(panel){



    const index =

    state.panels.findIndex(

        item=>
        item.id===panel.id

    );



    if(index!==-1){


        const removed =

        state.panels.splice(

            index,

            1

        )[0];



        state.closedPanels.push(
            removed
        );


    }


    save();


}








function restore(panel){



    const index =

    state.closedPanels.findIndex(

        item=>
        item.id===panel.id

    );



    if(index!==-1){


        const restored =

        state.closedPanels.splice(

            index,

            1

        )[0];


        state.panels.push(
            restored
        );


    }


    save();


}








function reset(){


    state.panels =

    structuredClone(
        workspaceConfig.panels
    );


    state.closedPanels=[];


    save();


}








export function useWorkspaceStore(){


    return {


        panels:
        state.panels,


        closedPanels:
        state.closedPanels,


        move,


        resize,


        rotate,


        focus,


        close,


        restore,


        reset


    };


}