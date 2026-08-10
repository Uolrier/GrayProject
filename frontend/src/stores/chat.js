import { defineStore } from "pinia";

import {
    streamChat,
    stopChat,
} from "@/modules/chat/api/chat";

import { useKnowledgeBaseStore } from "@/stores/knowledgeBase";

export const useChatStore = defineStore(
    "chat",
    {
        state: () => ({
            messages: [],
            loading: false,
            currentTaskId: null,
        }),

        actions: {

            async stopGeneration() {

                if (!this.currentTaskId) {
                    return;
                }

                try {

                    await stopChat(
                        this.currentTaskId
                    );

                } finally {

                    this.currentTaskId = null;

                }
            },

            addMessage(
                role,
                content
            ) {

                this.messages.push({
                    role,
                    content,
                });

            },

            async sendMessage(
                message
            ) {

                if (
                    !message ||
                    this.loading
                ) {
                    return;
                }

                const knowledgeBaseStore =
                    useKnowledgeBaseStore();

                const collection =
                    knowledgeBaseStore.currentKnowledgeBase;

                if (!collection) {
                    return;
                }

                this.loading = true;

                // 用户消息

                this.addMessage(
                    "user",
                    message
                );

                // 创建 assistant 占位

                this.addMessage(
                    "assistant",
                    ""
                );

                const assistantIndex =
                    this.messages.length - 1;

                if (!collection) {

                    this.messages[
                        assistantIndex
                    ].content =
                        "请先选择知识库";

                    this.loading = false;

                    return;
                }

                try {

                    await streamChat(
                        message,
                        collection,

                        (token) => {
                            this.messages[
                                assistantIndex
                            ].content += token;
                        },

                        (taskId) => {
                            this.currentTaskId = taskId;
                        }
                    );

                } catch (error) {

                    this.messages[
                        assistantIndex
                    ].content =
                        "请求失败";

                    console.error(
                        error
                    );

                } finally {

                    this.loading = false;

                    this.currentTaskId = null;

                }
            },
        },
    }
);