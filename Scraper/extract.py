import requests
from striprtf.striprtf import rtf_to_text
#from bs4 import BeautifulSoup


def get_response(URL):
    """Extrae la informacion de la URL que se le pasa
    
        Returns:
        string -- Con el contenido de la informacion del enlace (RTF)
        None -- Cuando la peticion no fue exitosa"""
        
    headers={
        'User-Agent':'Mozilla/5.0'
    }
    response=requests.get(URL,headers=headers,verify=False)
    if response.status_code==200:
        return response.text
   
    return None

def create_hmtl_file(content,NAME):
    """Crea el archivo RTF de manera local a partir del contenido que se le pasa"""
    
    try:
        with open(f'{NAME}.rtf','w',encoding='utf-8') as file:
            file.write(content)
    except:
        pass

def get_hmtl_file(NAME):
    """Lee el contienido de un archivo local"""
    content=None
    try:
        with open(f'{NAME}.rtf','r',encoding='utf-8') as file:
            content=file.read()
    except:
        pass
    return content

def get_local_html_content(URL,NAME):
    """Obtiene el contenido del archvio descargado de la peticion ya sea de forma local o mediante peticion"""
    content=get_hmtl_file(NAME)
    if content:
        return content
    else:
        content=get_response(URL)
        create_hmtl_file(content,NAME)
    return content


def read_file(NAME):
    """Lee un archivo de tipo RTF y lo convierte en una cadena string"""
    with open(f'{NAME}.rtf') as infile:
        content = infile.read()
        text = rtf_to_text(content)
    return text   

