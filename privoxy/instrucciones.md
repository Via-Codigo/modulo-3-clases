# Como configurarlo

En todas las máquinas hay que instalar privoxy

sudo apt-get install privoxy

Lo configuramos

`sudo subl /etc/privoxy`

Abrimos el archivo config y buscamos la línea donde pone:


`listen-address  127.0.0.1:8118`  (si esto esta commented con un # hay que quitar el #)

Y agregamos debajo:

```
actionsfile blacklist.action
actionsfile whitelist.action
```

En la misma carpeta del config creamos dos archivos:

blacklist.action
whitelist.action

Notaran que son los mismos que hemos agregado arriba, es básicamente un import

Contenido de blacklist.action:

```
######################################################
{ +block }
/ # Block all URLs

############################################################
```

Contenido de whitelist.action

```
######################################################
{ -block }
codepen.io #ejemplo
www.codepen.io #ejemplo

######################################################

```

Arrancando privoxy cuando arranca el sistema:

`sudo systemctl enable privoxy`

Arrancando privoxy ahora

`sudo systemctl start privoxy`

Viendo si esta corriendo bien

`sudo systemctl status privoxy`

Desactivando privoxy al arrancar la compu

`sudo systemctl disable privoxy`

Parando privoxy en este momento

`sudo systemctl stop privoxy`


Como se usa:

En los navegadores hay que configurar el proxy.

Por lo que he visto, firefox lo configura automáticamente

En todo caso

Firefox

ir a configuracion, buscar proxy y decirle que use el proxy del sistema

Chrome

ir a configuración, ir a avanzadas, buscar proxy

settear proxy manualmente

HTTP 127.0.0.1 port 8118

apply

reiniciar chrome