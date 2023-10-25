import os
from haystack import Pipeline
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import EmbeddingRetriever, PromptNode, PromptTemplate, AnswerParser
from dotenv import load_dotenv
import chainlit as cl


def initialize_rag_pipeline(index_path,config_path,openai_key):
    
    """Proceso de creacion de la base de datos y embeding de la misma (RAG) para esto se parte de tener los archivos
        previamente generados de my_index.faiss, my_config.json y faiss_document_store.db los cuales deben ser 
        los mismos de cuando se genero la base de datos 
    
        Returns:
        pipeline -- Con los pasos necesarios para generar el prompt que se conecta al RAG
        None -- si no existe los archivos necesarios para generar la base de FAISS
        """
    # Carga la base de datos
    try:
        document_store = FAISSDocumentStore.load(index_path=index_path, config_path=config_path)
    except:
        print("La base de datos no se ha cargado. Debes ejecutar la función 'index_documents' primero.")
        return None

    rag_prompt = PromptTemplate(
        prompt="""Synthesize a comprehensive answer from the following text for the given question.
                                Provide a clear and concise response that summarizes the key points and information presented in the text.
                                Your answer should be in your own words and be no longer than 50 words.
                                \n\n Related text: {join(documents)} \n\n Question: {query} \n\n Answer:""",
        output_parser=AnswerParser(),
    )

    model = "gpt-4"
    prompt_node = PromptNode(
        model_name_or_path=model,
        api_key=openai_api_key,
        default_prompt_template=rag_prompt
    )

    retriever = EmbeddingRetriever(document_store=document_store,
                                    embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1")

    query_pipeline = Pipeline()
    query_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
    query_pipeline.add_node(component=prompt_node, name="PromptNode", inputs=["Retriever"])
    return query_pipeline
 
  
  
    
# Importa la clave de API desde .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

#Direccion de los archivos de configuracion de la base
index_path = os.path.join(os.getcwd(),"my_index.faiss")
config_path = os.path.join(os.getcwd(), "my_config.json")
query_pipeline = initialize_rag_pipeline(index_path,config_path,openai_api_key)

@cl.on_message
async def main(message: cl.Message):
    # Use the pipeline to get a response
    output = query_pipeline.run(query=message.content)

    # Create a Chainlit message with the response
    response = output['answers'][0].answer
    msg = cl.Message(content=response)

    # Send the message to the user
    await msg.send()

