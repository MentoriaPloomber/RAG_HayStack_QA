import pandas as pd
import os 
#from bs4 import BeautifulSoup
import extract as function_extract
import time as tm

#Proceso de creacion del archivo de metadata para la 
#Extraccion de Links de descarga e informacion de los archivos
# Para correrlo es necesario tener el archivo de relatoria corte

# df=pd.read_html("relatoria_corte_Constitucional_20230922.xls")[0]

# with open('relatoria_corte_Constitucional_20230922.xls','r',encoding='utf-8') as file:
#     content=file.read()

# soup=BeautifulSoup(content,"html.parser")
# href_tag=soup.find_all('a', href=True)
# links=[]
# for tag in href_tag:
#     links.append((tag.text,tag['href']))
# df_links=pd.DataFrame(links, columns =['Providencia', 'Link'])
# df_descarga=df.merge(df_links,how="left",left_on="Providencia",right_on="Providencia").set_index("#")
# df_descarga["Link_descarga"]=df_descarga["Link"].str.replace("relatoria","sentencias",regex=False).str.replace("htm","rtf",regex=False)
# df_descarga.to_csv("Metadata.csv",sep="|",index=None)



#Lectura del archivo de metadatos con los links de descarga de los archivos
df_descarga=pd.read_csv("Metadata.csv",sep="|")

#Procedimiento para descarga automatica de archivos RTF utilizando el 
#archivo de metadata.csv el cual se genero por un proceso previo
# se coloco un time out de 30 segundos entre peticion y peticion

##Funcion cuando se monta en un colab
#from google.colab import drive
#drive.mount('/content/drive')
#path_folder='/content/drive/MyDrive/Data_sentencias'

#creacion de la carpeta donde se guardaran los archivos 
path_folder=os.path.join(os.getcwd(),'Data_sentencias')
if not os.path.exists(path_folder):
    os.mkdir(path_folder)
    

for i,j in zip(df_descarga["Link_descarga"],df_descarga["archivo"]):
    path_file=os.path.join(path_folder,j)
    function_extract.get_local_txt_content(i,path_file)
    tm.sleep(30)

##Funcion para visulizar la cadena de texto del archivo txt
# especificando la ruta o el nombre del archivo 
print(function_extract.read_txt_file(path_file))


