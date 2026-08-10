<template>

<WorkspaceLayout
    :locked="workspaceLocked"
    @lock-change="workspaceLocked=$event"
>

    <WorkspacePanel
        :locked="workspaceLocked"

        v-for="panel in panels"

        :key="panel.id"

        :panel="panel"

        @move="updateMove(panel,$event)"

        @resize="updateResize(panel,$event)"

        @rotate="updateRotate(panel,$event)"

        @focus="updateFocus(panel)"

        @close="closePanel"

    >

        <component
            :is="getPanelComponent(panel)"
        />

        </WorkspacePanel>

    <WorkspaceToolbar

        :closedPanels="closedPanels"

        @open="openPanel"

    />


</WorkspaceLayout>


</template>





<script setup>

import ChatBox 
from "@/modules/chat/components/ChatBox.vue";



import {
    reactive,
    toRaw,
    ref
}
from "vue";


import WorkspaceLayout 
from "../components/layout/WorkspaceLayout.vue";


import WorkspacePanel 
from "../components/WorkspacePanel.vue";


import WorkspaceToolbar 
from "../components/WorkspaceToolbar.vue";



import workspaceConfig 
from "../config/workspace.json";



import {

    loadWorkspaceState,

    saveWorkspaceState

}
from "../core/workspaceState";



import {

    useWindowManager

}
from "../core/windowManager";



const workspaceLocked =
ref(true);

const {

    focus,

    move,

    resize,

    rotate,

    close,

    restore

}=useWindowManager();

const workspace =
    loadWorkspaceState();

const panels = reactive(

    workspace.panels || 
    structuredClone(
        workspaceConfig.panels
    )

);





const closedPanels = reactive(

    workspace.closedPanels || []

);



const components = {

    ChatBox: ChatBox

};


function saveState(){


    saveWorkspaceState({

        panels:
        toRaw(panels),


        closedPanels:
        toRaw(closedPanels)

    });


}







function updateMove(panel,position){


    move(
        panel,
        position
    );


    saveState();


}

function updateFocus(panel){
    focus(
        panel,
        panels
    );
    saveState();
}

function closePanel(panel){
    close(
        panel,
        panels,
        closedPanels
    );
    saveState();
}
function openPanel(panel){
    restore(
        panel,
        panels,
        closedPanels
    );
    saveState();
}





function updateResize(panel,size){
    resize(
        panel,
        size
    );
    saveState();
}

function updateRotate(panel,angle){
    rotate(
        panel,
        angle
    );
    saveState();
}

function getPanelComponent(panel){

    const map = {

        chat: ChatBox,

    };


    return map[panel.id] || null;

}

</script>