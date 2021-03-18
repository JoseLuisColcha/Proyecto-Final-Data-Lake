# Noticias y eventos mundiales
## 1. [Extracción de datos](Datos)
- Se extrajo datos de la pagina web **kaggle** relacionados a las personas vacunadas del Covid-19 y de una página web llamada **statista**, la cual proporciona la evolución del Covid-19 en el mundo desde el 3 de febrero de 2020 hasta el 12 de marzo de 2021. Las graficas de dichos datos se los realizo en PowerBi.
- Se recopilaron datos de Facebook, de algunos portales de noticias más populares como BBCnewsMundo, CNN en Español, El Clarin, El mundo y RT media, donde se los almaceno en MongoDB.  
## 2. [Scripts](Scripts)
- Se generaron varios scripts .py para recopilar los datos de Facebook.
- Los datos obtenidos de los cuales solo se analizó la columna texto con la librería de Python [textBlob](Scripts/Facebook_textblob.py), para obtener las noticias positivas, negativas.
## 3. [Visualizaciones](Visualizaciones)
- Los graficos de los datos obtenidos de la pagina web **kaggle** se los obtuvo con **kibana** mediante **elasticsearch** y [**logstash**](paises_vacunados.conf). Se obtuvieron dos graficas: [personas completamente vacunados](Visualizaciones/personas_completamente_vacunados.jpg) y las [personas vacunadas diariamente](Visualizaciones/personas_vacunadas_diariamente_por_paises.jpg).
- Los graficos de los datos obtenidos de la pagina web **statista** se los realizo con PowerBI. Se obtuvieron 3 graficas: [número de personas confirmadas](Visualizaciones/Número_de_personas_confirmadas.png), [número de personas fallecidas](Visualizaciones/Número_de_personas_fallecidas.png) y [número de personas recuperadas](Visualizaciones/Número_de_personas_recuperadas.png).
- Los datos que se recopilaron de Facebook se los analizo con PowerBI y se obtuvieron 5 graficas: [noticias positivas y negativas de BBC news Mundo](Visualizaciones/Polaridad-BBC.png), [noticias positivas y negativas de CNN en español](Visualizaciones/Polaridad-CNN.png), [noticias positivas y negativas de El Clarín](Visualizaciones/Polaridad-El_Clarín.png), [noticias positivas y negativas de El Mundo](Visualizaciones/Polaridad-El_Mundo.png) y [noticias positivas y negativas de RT](Visualizaciones/Polaridad-RT.png)     
