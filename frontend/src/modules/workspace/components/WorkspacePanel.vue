<template>

<div
    class="panel"
    :data-panel-id="panel.id"
    :style="panelStyle"
    @mousedown.stop="handleMouseDown"
>


    <button
    v-if="
    panel.closable
    &&
    !locked
    "
    class="close"
    @click.stop="closePanel"
    >
    ×
    </button>


    <div class="title">

        {{ panel.title }}

    </div>

    <div class="content">

        <slot />

</div>
    <div
    v-if="!props.locked"
    class="resize-handle"
    @mousedown.stop="startResize"
    />


    <div
    v-if="!props.locked"
    class="rotate-handle"
    @mousedown.stop="startRotate"
    />
</div>

</template>



<script setup>

import {
    computed,
    ref
}
from "vue";


import {
    usePanelInteraction
}
from "../composables/usePanelInteraction";



const props = defineProps({

    panel:{
        type:Object,
        required:true
    },


    locked:{
        type:Boolean,
        default:true
    }

});



const emit = defineEmits([

    "move",
    "focus",
    "close",
    "minimize",
    "resize",
    "rotate"

]);



const {

    startDrag,

    startResize,

    startRotate


}=usePanelInteraction(

    props.panel,

    emit

);

function closePanel(){

    emit(
        "close",
        props.panel
    );

}

function handleMouseDown(e){
    if(props.locked)
        return;
    emit(
        "focus",
        props.panel
    );
    startDrag(e);
}

const panelStyle = computed(()=>{
    return {
        width:
        props.panel.width+"px",
        height:
        props.panel.height+"px",
        backgroundImage:
        `url(${props.panel.image})`,
        transform:
        `
        translate(
            ${props.panel.position.x}px,
            ${props.panel.position.y}px
        )
        rotate(
            ${props.panel.rotate}deg
        )
        `,
        borderRadius:
        props.panel.radius+"px",
        zIndex:
        props.panel.zIndex || 1
    }
});



</script>





<style scoped>

.panel {

    position:absolute;

    background-size:cover;

    background-position:center;

    display:flex;

    justify-content:center;

    align-items:center;

    cursor:move;

    user-select:none;
    -webkit-user-select:none;

    overflow:visible;


    border:
    3px solid rgba(255,255,255,0.75);


    outline:
    2px solid rgba(255,255,255,0.15);


    box-shadow:
    0 10px 30px rgba(0,0,0,0.35);


    transition:
    0.2s ease;

}

.title{

position:absolute;

top:15px;

left:15px;


background:
rgba(0,0,0,0.35);

backdrop-filter:
blur(8px);


padding:
8px 16px;


border-radius:
12px;


color:white;


font-size:22px;


font-weight:600;


letter-spacing:1px;


text-shadow:
0 2px 5px rgba(0,0,0,0.8);


z-index:10;

}

.close{


position:absolute;


top:10px;


right:10px;



width:35px;


height:35px;



border:none;



border-radius:50%;



background:
rgba(0,0,0,0.7);



color:white;



font-size:24px;



cursor:pointer;



z-index:20;



display:flex;


align-items:center;


justify-content:center;



}




.resize-handle{


position:absolute;



right:0;



bottom:0;



width:20px;



height:20px;



cursor:se-resize;



background:
rgba(255,255,255,0.4);



border-radius:5px;



}

.rotate-handle{


position:absolute;


top:-25px;

right:-25px;


width:25px;

height:25px;


border-radius:50%;


background:white;


border:2px solid #333;


cursor:grab;


}


.rotate-handle:hover{

background:#aaa;

}

.content{

    width:100%;

    height:100%;

    display:flex;

    overflow:hidden;

    padding-top:55px;

    box-sizing:border-box;

    user-select:text;
}


</style>