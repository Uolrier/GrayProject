export async function streamChat(
    message,
    onToken,
    onInit,
) {
    const response = await fetch(
        "/chat/stream",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                message,
            }),
        }
    );

    if (!response.ok) {
        throw new Error(
            `HTTP error: ${response.status}`
        );
    }

    const reader = response.body.getReader();

    const decoder = new TextDecoder(
        "utf-8"
    );

    let event = "message";

    while (true) {

        const {
            done,
            value,
        } = await reader.read();

        if (done) {
            break;
        }

        const chunk = decoder.decode(
            value,
            {
                stream: true,
            }
        );

        const lines = chunk.split("\n");

        for (const line of lines) {

            if (line.startsWith("event:")) {
                event = line.slice(6).trim();
                continue;
            }

            if (!line.startsWith("data:")) {
                continue;
            }

            const data = line.slice(5).trim();

            if (!data) {
                continue;
            }

            if (data === "[DONE]") {
                return;
            }

            try {

                const json = JSON.parse(data);

                if (event === "init") {

                    onInit?.(json.task_id);

                } else if (json.content) {

                    onToken(json.content);

                }

            } catch {

                onToken(data);

            }

            event = "message";
        }
    }
}

export async function stopChat(taskId) {
    const response = await fetch(
        "/chat/stop",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                task_id: taskId,
            }),
        }
    );

    if (!response.ok) {
        throw new Error(
            `HTTP error: ${response.status}`
        );
    }

    return response.json();
}