# miniflask
Une petite app avec flask et des données json

# Qu'est ce que Flask
![Logo de flask](http://sdz.tdct.org/sdz/medias/uploads.siteduzero.com_files_390001_391000_390565.png "le logo de flask")

Flask est un micro-framework python destiné à créer des applications web.
On l'installe sur un ordinateur qui servira de serveur (un rapberry pi par exemple), on lance le script python qui contient
l'application, puis on peut accéder à l'application web avec n'importe quel navigateur d'un ordi relié au réseau de ce serveur.

# Installation de flask et de l'application miniflask
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

Vous trouverez plein d'informations utiles sur flask sur :

[La page officielle de flask](https://www.palletsprojects.com/p/flask/)

[Ce tutoriel en français](http://sdz.tdct.org/sdz/creez-vos-applications-web-avec-flask.html)

[Ce tutoriel en anglais, le plus réussi des 3](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)



