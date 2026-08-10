<template>

<div class="workspace-layout">

        <button
            class="workspace-lock"
            @click="toggleLock"
        >

            <img
                :src="
                    props.locked
                    ?
                    '/images/Lock-close.jpg'
                    :
                    '/images/Lock-open.jpg'
                "
            />

        </button>

        <div
            class="workspace-background"
            :style="backgroundStyle"
        >

        </div>


        <div class="workspace-content">

            <slot />

        </div>


    </div>

</template>

<script setup>

import {
    computed
}
from "vue";


import {
    loadWorkspaceConfig
}
from "../../core/loader";


const props = defineProps({

    locked:{
        type:Boolean,
        default:true
    }

});


const emit = defineEmits([
    "lock-change"
]);



const config =
loadWorkspaceConfig();



const backgroundStyle =
computed(()=>{


    const bg =
    config.background;


    return {

        backgroundImage:
        `url(${bg.image})`,

        backgroundSize:
        bg.size,

        backgroundPosition:
        bg.position,

        backgroundRepeat:
        bg.repeat

    };


});



function toggleLock(){


    emit(
        "lock-change",
        !props.locked
    );


}


</script>



<style scoped>


.workspace-layout {

    width:100%;

    height:100%;

    min-height:100vh;

    position:relative;

    overflow:hidden;

}



.workspace-background {


    position:absolute;

    top:0;

    left:0;

    right:0;

    bottom:0;


    z-index:0;


}



.workspace-content {


    position:relative;

    z-index:1;


    width:100%;

    height:100%;


}

.workspace-lock{


position:absolute;


left:30px;

bottom:30px;


width:45px;

height:45px;


z-index:100;


border:none;


background:none;


cursor:pointer;


}


.workspace-lock img{


width:100%;

height:100%;


}
</style>