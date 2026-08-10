import { createRouter, createWebHistory } from "vue-router";

import ChatView from "@/modules/chat/views/ChatView.vue";
import WorkspaceView from "@/modules/workspace/views/WorkspaceView.vue";


const router = createRouter({

  history: createWebHistory(),

  routes: [

    {
      path: "/",
      redirect: "/chat",
    },

    {
      path: "/chat",
      name: "chat",
      component: ChatView,
    },

    {
      path: "/workspace",
      name: "workspace",
      component: WorkspaceView,
    },

  ],

});


export default router;