# morpho-web
Aplicación Web para el análisis morfológico de textos en español.

##Instalación
Para correr la aplicación es necesario tener instalado freeling y su API para python y Flask para la generación del servicio Web.

```{r, engine='bash', count_lines}
git clone https://github.com/ficolo/morpho-web.git
pip install flask
python application.py
```

En caso de no tener instaldo Freeling puede usar este contenedor de Docker que contiene todas las librerías necesarias para correr la aplicación y la aplicación misma:

```{r, engine='bash', count_lines}
sudo apt-get update
sudo apt-get install docker
sudo docker pull ficolo/morpho-web:latest
sudo docker run -d -p 5000:5000  ficolo/morpho-web python /root/morpho-web/application.py
```

Este comando descargará y levantará el contenedor con la aplicación y expondrá el puerto 5000 del contenedor para así poder accederlo a través un navegador usando http://127.0.0.1:5000.

