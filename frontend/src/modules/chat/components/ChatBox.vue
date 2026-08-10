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
    display: flex;
    flex-direction: column;
    height: 90vh;
    padding: 20px;
    box-sizing: border-box;
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
    flex: 1;
    overflow-y: auto;
    min-height: 0;
}

.message {
    margin: 8px;
}

.user {
    text-align: right;
}

.assistant {
    text-align: left;
}

.input-area {
    display: flex;
    gap: 8px;
    padding-top: 12px;
}

.input-area input {
    flex: 1;
    height: 40px;
    padding: 0 12px;
    font-size: 16px;
}

.input-area button {
    height: 40px;
    padding: 0 20px;
}

</style>