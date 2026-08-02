import { defineStore } from "pinia";

import {
    streamChat,
    stopChat,
} from "@/api/chat";


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


                this.loading = true;


                // 用户消息

                this.addMessage(
                    "user",
                    message
                );


                // 创建assistant占位

                this.addMessage(
                    "assistant",
                    ""
                );


                const assistantIndex =
                    this.messages.length - 1;


                try {

                    await streamChat(
                        message,

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