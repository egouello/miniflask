# miniflask
## simple app with flask and json data

# Flask
Flask est un mini framework python destiné à créer des applications web.
On l'installe sur un ordinateur qui servira de serveur (un rapberry pi par exemple), on lance le script python qui contient
l'application, puis on peut accéder à l'application web avec n'importe quel navigateur d'un ordi relié au réseau de ce serveur.

# Installation de flask
Sur un raspberry pi sous rasbian, il suffit de taper en ligne de commande:
```
sudo pip install Flask
```
ensuite, il faut créer un dossier dans lequel installer miniflask
```
mkdir miniflask
```
C'est dans ce dossier qu'il faut copier les fichiers du projet

Ensuite, il suffit de lancer le serveur flask avec la commande :
```
python3 app.py
```
Le serveur flask est alors à l'écoute du port 5000 et il suffit alors de se connecter avec un navigateur sur le port 5000.
Si le raspberry a comme adresse IP 111.222.333.444, alors il faut taper dans le navigateur : 111.222.333.444:5000
