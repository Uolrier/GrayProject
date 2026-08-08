import api from "./index";

export async function listKnowledgeBases() {
    const response = await api.get(
        "/knowledge-bases"
    );

    return response.data.knowledge_bases;
}
