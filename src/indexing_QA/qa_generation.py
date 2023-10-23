import os
from haystack import Pipeline
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import EmbeddingRetriever, PromptNode, PromptTemplate, AnswerParser
from dotenv import load_dotenv


def initialize_rag_pipeline(index_path,config_path,openai_key):
  

  # Carga la base de datos
  if os.path.exists(index_path):
      document_store = FAISSDocumentStore.load(index_path=index_path, config_path=config_path)
  else:
      print("La base de datos no se ha cargado. Debes ejecutar la función 'index_documents' primero.")
      return 

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

  def answer_question(question):
      respuesta = query_pipeline.run(query=question)
      return respuesta['answers'][0].to_dict()['answer']

  if __name__ == "__main__":
      while True:
          user_question = input("Haz una pregunta (o escribe 'salir' para salir): ")
          if user_question.lower() == 'salir':
              break
          answer = answer_question(user_question)
          print("Respuesta:", answer)

if __name__=="__main__":
    
  # Importa la clave de API desde config.py  
  load_dotenv()
    
  openai_api_key = os.getenv("OPENAI_API_KEY")
  
  #Direccion de los archivos de configuracion de la base
  index_path = os.path.join(os.getcwd(),"my_index.faiss")
  config_path = os.path.join(os.getcwd(), "my_config.json")

  # Initialize pipeline
  query_pipeline = initialize_rag_pipeline(index_path,config_path,openai_api_key)
