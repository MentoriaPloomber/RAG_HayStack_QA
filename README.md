# Hacktoberfest 2023 project: building ETL and RAG pipelines with open source 

## Set up /  Configuración

There should be one GitHub repository per team. /  Debería haber un repositorio de GitHub por equipo.

**Ensure all team members have completed all steps in the [set up](setup.md) document.**

**Asegúrate de que todos los miembros del equipo hayan completado todos los pasos en el [documento de configuración](setup-espanol.md).**

## Theme of your project / Tema de tu proyecto

1. Retrieval Augmented Generation (RAG) pipeline for question answering /  Pipeline de Generación Aumentada por Recuperación (RAG) para responder preguntas

## Description / Descripción 

The basic idea is that a user asks the app if certain facts have been covered by judicial rulings of the High Courts in Colombia.

Context:

Colombia is a Social State of Law, power is divided into the classic 3 branches of public power; executive, legislative, judicial, plus other bodies such as the Attorney General's Office and Comptroller's Office.

The Judicial Branch resolves disputes that arise between citizens, whether civil, administrative, family, labor, agrarian, etc.

The Guardianship Action was included in the 1991 Constitution, [which has equivalents in other countries](https://repository.unilibre.edu.co/bitstream/handle/10901/23071/LA%20ACCI%C3%93N%20DE%20TUTELA%20COMPARADA%20CON%20OTROS%20PROCEDURES%20DE%20AMPARO%20ESTABLISHED%20EN%20AM%C3%89RICA%20LATINA.pdf?sequence=2), which through a procedure of 10 business days resolves the protection of fundamental rights , such as: health, life, education, access to information, dignity.

If a person feels or believes that their right is being violated or violated, they need to either hire a lawyer, go to the ombudsman's office or to a legal office at a university. Many times hiring a lawyer is already a barrier to the administration of justice if the interested party cannot afford the fees. The ombudsman's office, which offers free advice, is congested by the number of users in need. University legal offices cease service during the student vacation period.

Although judges are encouraged to write sentences in [easy reading](https://www.ambitojuridico.com/noticias/administrativo/congreso-crearia-formato-de-sentencias-de-lectura-facil), the use is inevitable of technicality, and non-lawyers would not know which sentences to pay attention to among the sea of ​​jurisprudence.

For this reason, a question and answer application (QA) is valuable for a person who believes that he or she is immersed in a circumstance of violation of rights because he or she can, by simply recording what happens to him or her -the facts-, know if previously, any sentence has protected a fundamental right in a similar case.

La idea básica es que un usuario pregunte a la app si unos hechos han sido amparados por sentencias judiciales de Altas Cortes en Colombia.

### Contexto:

Colombia es un Estado Social de Derecho, se divide el poder en las clásicas 3 ramas del poder público; ejecutivo, legislativo, judicial, más otros órganos como la Procuraduría y Contraloría.

La Rama Judicial resuelve las controversias que se dan entre los ciudadanos, sea de carácter civil, administrativo, familiar, laboral, agrario, etcétera.

Dentro de la Constitución de 1991 se incluyó la Acción de tutela, [que tiene equivalentes en otros países](https://repository.unilibre.edu.co/bitstream/handle/10901/23071/LA%20ACCI%C3%93N%20DE%20TUTELA%20COMPARADA%20CON%20OTROS%20PROCEDIMIENTOS%20DE%20AMPARO%20ESTABLECIDOS%20EN%20AM%C3%89RICA%20LATINA.pdf?sequence=2), la cual mediante un trámite de 10 días hábiles resuelve la protección de derechos fundamentales, tales como: salud, vida, educación, acceso a la información, dignidad.

Si una persona siente o cree que se le viola o vulnera un derecho necesita, o contratar un abogado, recurrir a la defensoría del pueblo o a un consultorio jurídico de una universidad. Muchas veces contratar a un abogado es ya una barrera a la administración de justicia si el interesado no puede costearse los honorarios. La defensoría del pueblo que ofrece asesoría gratuita, esta congestionada por la cantidad de usuarios necesitados. Los consultorios jurídicos de universidades cesan la atención durante el período de vacaciones de los estudiantes.

Aunque se exhorta a los jueces redacción de sentencias de [lectura fácil](https://www.ambitojuridico.com/noticias/administrativo/congreso-crearia-formato-de-sentencias-de-lectura-facil) , es inevitable el uso de tecnicismo, y las personas no abogadas no sabrían a cuales sentencias prestarle atención entre el mar de jurisprudencia.

Por lo anterior, una aplicación de preguntas y respuestas (QA) es valiosa para una persona que se cree inmersa en una circunstancia de violación de derechos porque puede, con solo consignar lo que le pasa -los hechos- , conocer si previamente, alguna sentencia ha protegido un derecho fundamental en un caso similar.

## Data sources / Fuentes de datos

1. Name of the data set: Guardianship Sentences of the High Courts of Colombia

Description: Text documents that can be downloaded in .rtf format

Source: https://www.corteconstitucional.gov.co/relatoria/

License: Public because they are judicial decisions and their use would be equivalent to the GNU 3.0 license:

https://es.wikipedia.org/wiki/GNU_General_Public_License

2. Name of the data set: Sentences of the Judiciary of Michoacan

Description: Text documents that can be downloaded in .pdf format

Source: https://www.poderjudicialmichoacan.gob.mx/web/consultas/sentenciasPublicas.aspx

License: Public because they are judicial decisions and their use would be equivalent to the GNU 3.0 license:

https://es.wikipedia.org/wiki/GNU_General_Public_License 


1. Nombre del conjunto de datos: Sentencias de Tutela de Altas Cortes de Colombia

Descripción: Documentos de texto que se pueden descargar en formato .rtf 

Fuente: https://www.corteconstitucional.gov.co/relatoria/

Licencia: Pública por ser decisiones judiciales y su uso sería equivalente a la licencia GNU 3.0:  

https://es.wikipedia.org/wiki/GNU_General_Public_License

2. Nombre del conjunto de datos: Sentencias del Poder Judicial de Michoacan

Descripción: Documentos de texto que se pueden descargar en formato .pdf

Fuente: https://www.poderjudicialmichoacan.gob.mx/web/consultas/sentenciasPublicas.aspx

Licencia: Pública por ser decisiones judiciales y su uso sería equivalente a la licencia GNU 3.0:  

https://es.wikipedia.org/wiki/GNU_General_Public_License

**Do not upload data to GitHub** / **No suba datos a GitHub**

## Methods / Métodos

Describe the methods you are using. Include a description of the tools you are using.

Describa los métodos que está utilizando. Incluya una descripción de las herramientas que está utilizando.

## User interface your project will have / Interfaz de usuario que tendrá su proyecto

Describe the user interface your project will have. Include a description of the tools you are using.

Options: 

1. FastAPI application
2. Chainlit application
3. Haystack application

Describa la interfaz de usuario que tendrá su proyecto. Incluya una descripción de las herramientas que está utilizando.

Opciones:

1. Aplicación FastAPI
2. Aplicación Chainlit
3. Aplicación Haystack

## Team members/ Miembros del equipo

[Elka Buitrago](https://github.com/elkabuitrago)
[Juan Vázquez Montejo](https://github.com/juanvazqmont)
[María Carolina Passarello](https://github.com/caropass)
[Sergio Maldonado Rodríguez](https://github.com/SergioRodMa)
[Anuar Menco Nemes](https://github.com/anuarmenco) 