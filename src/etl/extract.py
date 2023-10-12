import requests
from striprtf.striprtf import rtf_to_text
#from bs4 import BeautifulSoup


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
        create_txt_file(content_text,NAME)
    return content_text


def convert_rtf_file(content):
   """Lee un archivo de tipo RTF y lo convierte en una cadena string"""
   try:
        text = rtf_to_text(content)
   except:
       pass 
   return text   


def read_txt_file(NAME):
    """Lee un archivo de tipo txt para visualizar en una cadena string"""
    with open(f'{NAME}.txt','r',encoding='utf-8') as file:
        content=file.read()
    return content   