export async function listKnowledgeBases() {
    const response = await fetch(
        "/knowledge-bases",
        {
            method: "GET",
        }
    );

    if (!response.ok) {
        throw new Error(
            `HTTP error: ${response.status}`
        );
    }

    return response.json();
}