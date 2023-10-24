import os
from haystack import Pipeline
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import PreProcessor, EmbeddingRetriever
from haystack.utils import convert_files_to_docs

def delete_documents(file_path):
  """Funcion para borrar los archivos previo a su generacion"""
  try:
    os.remove(file_path)
  except:
    pass


def index_documents(doc_dir, document_store_dir):
  """ Funcion para indexacion de documentos creando primero la base de datos indexada y despues 
  actualizando la base de acuerdo al embeding
          
          Returns:
        con exito -- genera 3 archivos la base de datos faiss_documents_store.db, my_config.json, my_index.faiss
        None -- No se generan los archivos """

  # Verificar si el archivo de índice ya existe en la carpeta de destino
  index_path = os.path.join(document_store_dir, "my_index.faiss")
  config_path = os.path.join(document_store_dir, "my_config.json")
  db_base = os.path.join(document_store_dir, "faiss_document_store.db")
  
  delete_documents(index_path)
  delete_documents(config_path)
  delete_documents(db_base)

  try:
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
  except:
    pass  

if __name__ == "__main__":
  doc_dir = os.path.join(os.getcwd(),"Data_sentencias")
  document_store_dir=os.getcwd()
  index_documents(doc_dir=doc_dir,document_store_dir=document_store_dir)
