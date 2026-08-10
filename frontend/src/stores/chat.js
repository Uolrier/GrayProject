import { defineStore } from "pinia";

import {
    streamChat,
    stopChat,
} from "@/modules/chat/api/chat";

import { useKnowledgeBaseStore } from "@/stores/knowledgeBase";


const STORAGE_KEY =
    "gray_chat_messages";


function loadMessages(){

    try {

        const data =
            localStorage.getItem(
                STORAGE_KEY
            );

        return data
            ? JSON.parse(data)
            : [];

    } catch(error){

        console.error(
            "load chat history failed:",
            error
        );

        return [];

    }

}


function saveMessages(messages){

    localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify(messages)
    );

}



export const useChatStore = defineStore(
    "chat",
    {

        state: () => ({

            messages:
                loadMessages(),

            loading:false,

            currentTaskId:null,

        }),



        actions:{


            save(){

                saveMessages(
                    this.messages
                );

            },



            async stopGeneration(){


                if(
                    !this.currentTaskId
                ){
                    return;
                }


                try{

                    await stopChat(
                        this.currentTaskId
                    );


                    const lastMessage =
                        this.messages[
                            this.messages.length - 1
                        ];


                    if(
                        lastMessage &&
                        lastMessage.role === "assistant"
                    ){

                        lastMessage.content +=
                            "\n\n[已停止生成]";

                    }


                    this.save();


                }finally{


                    this.currentTaskId =
                        null;


                    this.loading =
                        false;


                }

            },



            addMessage(
                role,
                content
            ){


                this.messages.push({

                    role,

                    content,

                });


                this.save();


            },



            async sendMessage(
                message
            ){


                if(
                    !message ||
                    this.loading
                ){

                    return;

                }



                const knowledgeBaseStore =
                    useKnowledgeBaseStore();



                const collection =
                    knowledgeBaseStore.currentKnowledgeBase;



                if(!collection){

                    return;

                }



                this.loading=true;



                this.addMessage(
                    "user",
                    message
                );



                this.addMessage(
                    "assistant",
                    ""
                );



                const assistantIndex =
                    this.messages.length - 1;



                try{


                    await streamChat(

                        message,

                        collection,


                        (token)=>{


                            this.messages[
                                assistantIndex
                            ].content += token;


                            this.save();


                        },


                        (taskId)=>{


                            console.log(
                                "store task id:",
                                taskId
                            );


                            this.currentTaskId =
                                taskId;


                        }

                    );



                }catch(error){


                    this.messages[
                        assistantIndex
                    ].content =
                        "请求失败";


                    this.save();



                    console.error(
                        error
                    );


                }finally{


                    this.loading=false;


                    this.currentTaskId=null;


                }


            },


            clearHistory(){


                this.messages=[];


                localStorage.removeItem(
                    STORAGE_KEY
                );


            },


        },

    }
);