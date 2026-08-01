<script setup>
import { ref } from "vue";

import { useChatStore } from "@/stores/chat";


const chatStore = useChatStore();


const input = ref("");


function send() {

    const message =
        input.value.trim();


    if (!message) {
        return;
    }


    chatStore.sendMessage(message);

    input.value = "";
}

</script>


<template>

<div class="chat-box">


    <div class="messages">

        <div
            v-for="(
                message,
                index
            ) in chatStore.messages"
            :key="index"
            class="message"
            :class="message.role"
        >

            <strong>
                {{ message.role }}:
            </strong>

            <span>
                {{ message.content }}
            </span>

        </div>


    </div>



    <div class="input-area">

        <input
            v-model="input"
            @keyup.enter="send"
            placeholder="输入消息..."
        />


        <button
            @click="send"
            :disabled="chatStore.loading"
        >

            发送

        </button>


    </div>


</div>

</template>


<style scoped>


.chat-box {

    display:flex;

    flex-direction:column;

    height:100%;

}


.messages {

    flex:1;

    overflow-y:auto;

}


.message {

    margin:8px;

}


.user {

    text-align:right;

}


.assistant {

    text-align:left;

}



.input-area {

    display:flex;

    gap:8px;

}


.input-area input {

    flex:1;

}


</style>