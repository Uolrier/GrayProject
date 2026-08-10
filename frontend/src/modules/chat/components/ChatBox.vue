<script setup>
import { onMounted, ref } from "vue";

import { useChatStore } from "@/stores/chat";
import { useKnowledgeBaseStore } from "@/stores/knowledgeBase";

const chatStore = useChatStore();
const knowledgeBaseStore =
    useKnowledgeBaseStore();

onMounted(async () => {
    try {
        await knowledgeBaseStore.loadKnowledgeBases();
    } catch (error) {
        console.error(error);
    }
});

const input = ref("");

async function stop() {
    try {
        await chatStore.stopGeneration();
    } catch (error) {
        console.error(error);
    }
}

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
        <div class="knowledge-base-selector">

            <label>
                知识库：
            </label>

            <select
                :value="
                    knowledgeBaseStore.currentKnowledgeBase
                "
                @change="
                    knowledgeBaseStore.setCurrentKnowledgeBase(
                        $event.target.value
                    )
                "
                :disabled="
                    knowledgeBaseStore.loading ||
                    knowledgeBaseStore.knowledgeBases.length === 0
                "
            >

                <option
                    v-if="
                        knowledgeBaseStore.knowledgeBases.length === 0
                    "
                    value=""
                >
                    暂无知识库
                </option>

                <option
                    v-for="
                        name in knowledgeBaseStore.knowledgeBases
                    "
                    :key="name"
                    :value="name"
                >
                    {{ name }}
                </option>

            </select>

        </div>

            <div class="messages">

                <div
                    v-for="(
                        message,
                        index
                    ) in chatStore.messages"

                    :key="index"

                    class="message-row"

                    :class="message.role"
                >

                        <div
                            v-if="message.role === 'assistant'"
                            class="avatar-box"
                        >
                            <img
                                class="avatar"
                                src="/images/ai-avatar.jpg"
                            />
                        </div>


                    <div class="message">

                        <span>
                            {{ message.content }}
                        </span>

                    </div>


                    <div
                        v-if="message.role === 'user'"
                        class="avatar-box"
                    >
                        <img
                            class="avatar"
                            src="/images/user-avatar.gif"
                        />
                    </div>

                </div>

            </div>


        <div class="input-area">

            <input
                v-model="input"
                @keyup.enter="send"
                :disabled="
                    chatStore.loading ||
                    !knowledgeBaseStore.currentKnowledgeBase
                "
                placeholder="输入消息..."
            />

            <button
                v-if="!chatStore.loading"
                @click="send"
                :disabled="
                    !knowledgeBaseStore.currentKnowledgeBase
                "
            >
                发送
            </button>


            <button
                v-else
                @click="stop"
            >
                停止
            </button>

        </div>

    </div>

</template>


<style scoped>

.chat-box {

    display:flex;

    flex-direction:column;

    width:100%;

    height:100%;

    padding:20px;

    box-sizing:border-box;


    user-select:text;
    -webkit-user-select:text;

}

.knowledge-base-bar {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 12px;
}

.knowledge-base-bar select {
    min-width: 220px;
    height: 36px;
    padding: 0 8px;
}

.messages {

    flex:1;

    overflow-y:auto;

    min-height:0;

    padding:10px;

}
.message-row {

    display:flex;

    align-items:flex-start;

    gap:10px;

    margin:15px 0;

}


.message {

    padding:12px 16px;

    border-radius:18px;

    max-width:75%;

    width:fit-content;

    line-height:1.6;

    word-break:break-word;


    background:
    rgba(255,255,255,0.75);


    color:#222;


    backdrop-filter:
    blur(10px);


    box-shadow:
    0 4px 15px rgba(0,0,0,0.15);


    transform:translateZ(0);

    will-change:transform;

}


.assistant {

    justify-content:flex-start;

}



.user {

    justify-content:flex-end;

}



.user .message {


    background:
    rgba(120,170,220,0.45);


    order:1;

}


.user .avatar-box {
    order: 2;
}

.assistant .avatar-box {
    order: 0;
}

.avatar-box {

    width:40px;

    height:40px;

    flex-shrink:0;

    overflow:hidden;

    isolation:isolate;

}


.avatar {

    width:40px;

    height:40px;

    display:block;

    border-radius:50%;

    object-fit:cover;

    user-select:none;

    -webkit-user-drag:none;

}

.input-area {

    display:flex;

    gap:8px;

    padding-top:12px;

}


.input-area input {

    flex:1;

    height:40px;


    padding:0 15px;


    font-size:16px;


    border:none;


    border-radius:20px;


    background:

    rgba(255,255,255,0.75);


    backdrop-filter:

    blur(10px);


}
.input-area button {

    height:40px;

    padding:0 20px;


    border:none;


    border-radius:20px;


    background:

    rgba(0,0,0,0.65);


    color:white;


    cursor:pointer;

}
.knowledge-base-selector{

    align-self:flex-start;


    display:flex;


    align-items:center;


    gap:10px;


    margin-bottom:10px;


    padding:8px 12px;


    width:fit-content;


    background:

    rgba(255,255,255,0.7);


    backdrop-filter:
    blur(10px);


    border-radius:15px;


    color:#222;

}
</style>