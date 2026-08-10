import { ref } from "vue";


const currentZIndex = ref(10);



export function useWindowManager(){



    function focus(
        panel,
        panels
    ){


        const maxZ =
            Math.max(
                ...panels.map(
                    item =>
                    item.zIndex || 1
                )
            );



        panel.zIndex =
            maxZ + 1;



    }






    function move(
        panel,
        position
    ){


        panel.position.x =
            position.x;


        panel.position.y =
            position.y;



    }





    function resize(
        panel,
        size
    ){


        panel.width =
            size.width;


        panel.height =
            size.height;



    }







    function rotate(
        panel,
        angle
    ){


        panel.rotate =
            angle;



    }








    function close(
        panel,
        panels,
        closedPanels
    ){


        const index =
            panels.findIndex(
                item =>
                item.id === panel.id
            );



        if(index !== -1){


            const removed =
                panels.splice(
                    index,
                    1
                )[0];


            closedPanels.push(
                removed
            );


        }


    }







    function restore(
        panel,
        panels,
        closedPanels
    ){


        const index =
            closedPanels.findIndex(
                item =>
                item.id === panel.id
            );



        if(index !== -1){


            const restored =
                closedPanels.splice(
                    index,
                    1
                )[0];


            panels.push(
                restored
            );


        }


    }






    return {


        focus,

        move,

        resize,

        rotate,

        close,

        restore


    };


}