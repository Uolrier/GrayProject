export async function streamChat(message, onToken) {
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

    while (true) {
        const {
            done,
            value,
        } = await reader.read();

        if (done) {
            break;
        }

        const chunk =
            decoder.decode(value, {
                stream: true,
            });

        const lines =
            chunk.split("\n");


        for (const line of lines) {
            if (
                line.startsWith("data:")
            ) {
                const data =
                    line.slice(5).trim();

                if (data) {
                    if (data === "[DONE]") {
                        return;
                    }


                    try {

                        const json = JSON.parse(data);


                        if (json.content) {
                            onToken(json.content);
                        }


                    } catch {

                        onToken(data);

                    }
                }
            }
        }
    }
}