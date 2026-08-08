export async function streamChat(
    message,
    onToken,
    onInit,
) {

    const response = await fetch(
        "/rag/chat/stream",
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json",
            },
            body:JSON.stringify({
                query:message,
            }),
        }
    );


    if(!response.ok){
        throw new Error(
            `HTTP error:${response.status}`
        );
    }


    const reader =
        response.body.getReader();


    const decoder =
        new TextDecoder("utf-8");


    let buffer = "";


    while(true){

        const {
            done,
            value,
        } = await reader.read();


        if(done){
            break;
        }


        buffer += decoder.decode(
            value,
            {
                stream:true,
            }
        );


        const events =
            buffer.split("\n\n");


        buffer =
            events.pop();


        for(
            const eventBlock
            of events
        ){

            const lines =
                eventBlock.split("\n");


            let event =
                "message";

            let data =
                null;


            for(
                const line
                of lines
            ){

                if(
                    line.startsWith("event:")
                ){

                    event =
                        line
                        .slice(6)
                        .trim();

                }


                if(
                    line.startsWith("data:")
                ){

                    data =
                        line
                        .slice(5)
                        .trim();

                }
            }


            if(!data){
                continue;
            }


            if(data==="[DONE]"){
                return;
            }


            const json =
                JSON.parse(data);


            if(event==="init"){

                onInit?.(
                    json.task_id
                );

            }
            else if(json.content){

                onToken(
                    json.content
                );
            }
        }
    }
}

export async function stopChat(taskId) {
    const response = await fetch(
        "/rag/chat/stop",
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

export async function ragChat(
    message,
) {
    const response = await fetch(
        "/rag/chat",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                query: message,
            }),
        },
    );

    if (!response.ok) {
        throw new Error(
            `HTTP error: ${response.status}`
        );
    }

    return response.json();
}