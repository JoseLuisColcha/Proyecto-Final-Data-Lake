# Pulso político por provincias en Ecuador


***
 ### [Datos](https://github.com/JoseLuisColcha/Proyecto-Final-Data-Lake/tree/main/2.Pulso%20politico%20por%20provincias/Datos) 🛠️

 Contiene los 30.000 datos recolectados alrededor de las 24 provincias del Ecuador acerca de temas políticos en la red social Twitter ,almacenados previamente en el gestor de base de datos CouchDB en el cual se creo una unificación de las 24 provincias.
 ***
  ### [Scripts](https://github.com/JoseLuisColcha/Proyecto-Final-Data-Lake/tree/main/2.Pulso%20politico%20por%20provincias/Scripts)📄
  Se utilizo dos scripts para la recopilación de datos :
  - El [primer script](https://github.com/JoseLuisColcha/Proyecto-Final-Data-Lake/blob/main/2.Pulso%20politico%20por%20provincias/Scripts/TwCouchDB.py)  se utilizo para recopilar información política en la red social twitter alrededor de las 24 provincias esto se logro gracias a la geolocalización.
  
  
  - El [segundo script](https://github.com/JoseLuisColcha/Proyecto-Final-Data-Lake/blob/main/2.Pulso%20politico%20por%20provincias/Scripts/TwCouchDB.py) se utilizo para migrar de base de datos de couchDB a mongoDB y de esa forma facilitar la exportacion de datos.

***

 ### [Visualizaciones](https://github.com/JoseLuisColcha/Proyecto-Final-Data-Lake/tree/main/2.Pulso%20politico%20por%20provincias/Datos)📌
Con ayuda del gestor de visualizaciones PowerBi se procedio a realizar 3 visualizaciones.

1. #### Total de retweets por provincias

Las primeras 3 provincias que más se habla de política son: Pichincha, Azuay y Guayas por otro lado las provincias en las cuales no se hablan acerca de política ni se twittea son: Carchi. Cotopaxi y Galápagos.

<img src="Visualizaciones/Tweets-por-provincia.jpg" width="1000"/><br/>
  
 *** 
1. ### Total de tweets favoritos en todas las provincias por candidato.
Andrés Arauz es el candidato presidencial más nombrado en la red social Twitter y agregado a la sección de favoritos, seguido por Guillermo Lasso y Yaku Pérez además Lucio Gutiérrez y Xavier Hervas también son nombrados, aunque en menor cantidad.
<img src="Visualizaciones/Total-tweets-favoritos-por-candidato.jpg" width="1000"/><br/>
***

1. ### Total de tweets por provincia y candidato presidencial.

Las primeras 3 provincias que más se habla de política son: Pichincha, Azuay y Guayas por otro lado las provincias en las cuales no se hablan acerca de política ni se twittea son: Carchi. Cotopaxi y Galápagos.
<img src="Visualizaciones/total-replay-por-provincias-y-candidato.jpg"/><br/>
***
