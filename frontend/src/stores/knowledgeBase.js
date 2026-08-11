import { defineStore } from "pinia";

import { listKnowledgeBases } from "@/shared/api/knowledgeBase";

export const useKnowledgeBaseStore = defineStore(
    "knowledgeBase",
    {
        state: () => ({
            knowledgeBases: [],
            currentKnowledgeBase: null,
            loading: false,
        }),

        actions: {
            async loadKnowledgeBases() {
                this.loading = true;

                try {
                    const data =
                        await listKnowledgeBases();

                    this.knowledgeBases =
                        data ?? [];

                    if (
                        this.knowledgeBases.length > 0 &&
                        !this.knowledgeBases.includes(
                            this.currentKnowledgeBase
                        )
                    ) {
                        this.currentKnowledgeBase =
                            this.knowledgeBases[0];
                    }

                    if (
                        this.knowledgeBases.length === 0
                    ) {
                        this.currentKnowledgeBase =
                            null;
                    }

                } finally {
                    this.loading = false;
                }
            },

            setCurrentKnowledgeBase(name) {
                if (
                    !this.knowledgeBases.includes(name)
                ) {
                    return;
                }

                this.currentKnowledgeBase = name;
            },

            clearCurrentKnowledgeBase() {
                this.currentKnowledgeBase = null;
            },
        },
    }
);