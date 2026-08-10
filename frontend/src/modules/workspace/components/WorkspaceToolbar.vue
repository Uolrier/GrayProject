<template>

<div
    v-if="closedPanels.length"
    class="toolbar"
>


    <button

        v-for="panel in closedPanels"

        :key="panel.id"

        @click="open(panel)"

    >

        Open {{ panel.title }}

    </button>


</div>

</template>





<script setup>


defineProps({

    closedPanels:{

        type:Array,

        default:()=>[]

    }

});



const emit = defineEmits([

    "open"

]);



function open(panel){


    emit(

        "open",

        panel

    );


}


</script>





<style scoped>


.toolbar{


position:absolute;



right:20px;



top:20px;




z-index:999;



display:flex;



flex-direction:column;



gap:10px;



}




button{


padding:

10px 20px;



cursor:pointer;




border:none;



border-radius:10px;



background:

rgba(0,0,0,0.6);



color:white;



font-size:14px;



backdrop-filter:

blur(5px);



}



button:hover{


background:

rgba(255,255,255,0.25);



}



</style>