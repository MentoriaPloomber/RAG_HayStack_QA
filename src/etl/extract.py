import requests
from striprtf.striprtf import rtf_to_text
import pandas as pd
import os 
import extract as function_extract
import time as tm
#from bs4 import BeautifulSoup


def get_url_by_year(year_s_list= [2022]):

  """
  Input: Se ingresa una lista de años desde 1992 hasta 2022, por defecto esta el año 2022
  Return: se obtiene una lista de url de sentencias de tutela de la Corte Constitucional de Colombia

  Ejemplo:
  sentencias_2000 = get_url_by_year([2000])
  len(sentencias_2000)
  >>>3516

  sentencias_2005_2000 = get_url_by_year([2000, 2005])
  len(sentencias_2005_2000)
  >>>6178
  """
  #Convierte la lista de años en texto
  year_s_list = [str(year) for year in year_s_list]
  #Se inicializa la variable url donde se depositaran los link que se retornaran
  url = []
  #Diccionario de años con el numero total de sentencias de Tutela de cada año
  years_dict = {
      "1992": 615,
      "1993": 598,
      "1994": 580,
      "1995": 624,
      "1996": 717,
      "1997": 680,
      "1998": 805,
      "1999": 999,
      "2000": 1758,
      "2001": 1346,
      "2002": 1127,
      "2003": 1233,
      "2004": 1249,
      "2005": 1331,
      "2006": 1089,
      "2007": 1099,
      "2008": 1276,
      "2009": 974,
      "2010": 999,
      "2011": 981,
      "2012": 1097,
      "2013": 956,
      "2014": 977,
      "2015": 777,
      "2016": 737,
      "2017": 744,
      "2018": 501,
      "2019": 621,
      "2020": 536,
      "2021": 462,
      "2022": 471,
  }
  #Se itera por cada año ingresado como parametro
  for year in year_s_list:
    #si el año ingresado esta en las llaves del diccionario, se mide si la sentencia máxima 
    # si el año no existe se genera una liga inexistente por default
    if (year in years_dict.keys()):
      for step in range(1, years_dict[year] + 1):
        url.append(f"https://www.corteconstitucional.gov.co/sentencias/{year}/T-{str(step).zfill(3)}-{year[-2:]}.rtf")
        url.append(f"https://www.corteconstitucional.gov.co/sentencias/{year}/T-{str(step).zfill(3)}A-{year[-2:]}.rtf")
    else:
      url.append("https://www.corteconstitucional.gov.co/sentencias/001/T-001-001.rtf")
   
   
  return url

def get_response(URL):
    """Extrae la informacion de la URL que se le pasa
    
        Returns:
        string -- Con el contenido de la informacion del enlace (txt)
        None -- Cuando la peticion no fue exitosa"""

    headers={
        'User-Agent':'Mozilla/5.0'
    }
    response=requests.get(URL,headers=headers,verify=False)
    if response.status_code==200:
        return response.text

    return None

def create_txt_file(content,NAME):
    """Crea el archivo txt de manera local a partir del contenido que se le pasa si el contenido es menor a 500 
    caracteres se considera un error en el archivo y no se genera"""
    if len(content)>500:
        try:
            with open(f'{NAME}.txt','w',encoding='utf-8') as file:
                file.write(content)
        except:
            pass

def get_txt_file(NAME):
    """Lee el contienido de un archivo local"""
    content=None
    try:
        with open(f'{NAME}.txt','r',encoding='utf-8') as file:
            content=file.read()
    except:
        pass
    return content

def get_local_txt_content(URL,NAME):
    """Obtiene el contenido del archvio descargado de la peticion ya sea de forma local o mediante peticion """
    content=get_txt_file(NAME)
    if content:

        return content
    else:
        content=get_response(URL)
        content_text=convert_rtf_file(content)
        if content_text:
            create_txt_file(content_text,NAME)
    return content_text


def convert_rtf_file(content):
   """Lee un archivo de tipo RTF y lo convierte en una cadena string"""
   try:
        text = rtf_to_text(content)
   except:
       text = None
   return text   


def read_txt_file(NAME):
    """Lee un archivo de tipo txt para visualizar en una cadena string"""
    with open(f'{NAME}.txt','r',encoding='utf-8') as file:
        content=file.read()
    return content   

if __name__ == "__main__":
    

    #Descarga de lista de enlaces para sentencias
    sentencias= get_url_by_year()
    df_descarga=pd.DataFrame(sentencias,columns=["Link_descarga"])
    df_descarga["archivo"]=df_descarga["Link_descarga"].map(lambda x:os.path.basename(x).replace(".rtf", ""))

    #creacion de la carpeta donde se guardaran los archivos 
    path_folder=os.path.join(os.getcwd(),'Data_sentencias')
    if not os.path.exists(path_folder):
        os.mkdir(path_folder)
        
    for i,j in zip(df_descarga["Link_descarga"],df_descarga["archivo"]):
        path_file=os.path.join(path_folder,j)
        get_local_txt_content(i,path_file)
        tm.sleep(30)

    


