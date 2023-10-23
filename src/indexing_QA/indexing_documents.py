import os
from haystack import Pipeline
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import PreProcessor, EmbeddingRetriever
from haystack.utils import convert_files_to_docs
#from tqdm import tqdm

def index_documents(doc_dir, document_store_dir, db_name):


  # Verificar si el archivo de índice ya existe en la carpeta de destino
  index_dir = os.path.join(document_store_dir, db_name)
  index_path = os.path.join(index_dir, "my_index.faiss")
  config_path = os.path.join(index_dir, "my_config.json")

  if os.path.exists(index_path):
    return 

  # Asegurarse de que el directorio de destino exista
  if not os.path.exists(document_store_dir):
      os.makedirs(document_store_dir)

  # Asegurarse de que el directorio del índice exista
  if not os.path.exists(index_dir):
      os.makedirs(index_dir)

  # Convertir los documentos en objetos de Haystack
  all_docs = convert_files_to_docs(dir_path=doc_dir)

  # Configurar el preprocesamiento
  preprocessor = PreProcessor(
      clean_empty_lines=True,
      clean_whitespace=True,
      clean_header_footer=False,
      split_by="word",
      split_length=500,
  )

  # Configurar el almacenamiento de documentos FAISS
  document_store = FAISSDocumentStore(faiss_index_factory_str="Flat")

  # Configurar el recuperador de incrustaciones
  retriever = EmbeddingRetriever(document_store=document_store,
                                  embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1")

  # Procesar los documentos
  docs = preprocessor.process(all_docs)

  # Escribir los documentos en el almacenamiento
  document_store.delete_documents()
  document_store.write_documents(docs)

  # Actualizar las incrustaciones
  document_store.update_embeddings(retriever)

  # Guardar el índice y la configuración
  document_store.save(index_path=index_path, config_path=config_path)
  #print(f"Índice guardado en: {index_path}")
if __name__ == "__main__":
  doc_dir = os.path.join(os.getcwd(),"Data_sentencias")
  document_store_dir=os.getcwd()
  db_name='my_index'
  index_documents(doc_dir=doc_dir,document_store_dir=document_store_dir,db_name=db_name)
