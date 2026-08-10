import workspaceConfig from "../config/workspace.json";


const STORAGE_KEY =
    "gray_workspace_state";




function cloneDefaultWorkspace(){


    return structuredClone(
        workspaceConfig
    );


}




export function loadWorkspaceState(){


    const saved =

        localStorage.getItem(
            STORAGE_KEY
        );



    if(saved){


        try{


            const state =
                JSON.parse(saved);



            return {


                panels:
                    state.panels || [],



                closedPanels:
                    state.closedPanels || []


            };



        }catch(e){


            console.warn(

                "workspace state corrupted"

            );


        }


    }




    const defaultState =
        cloneDefaultWorkspace();




    return {


        panels:
            defaultState.panels || [],



        closedPanels:[]

    };


}





export function saveWorkspaceState(state){



    localStorage.setItem(

        STORAGE_KEY,

        JSON.stringify(state)

    );


}




export function resetWorkspaceState(){


    localStorage.removeItem(

        STORAGE_KEY

    );


}