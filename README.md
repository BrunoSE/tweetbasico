# Tweet bot basico
Este script es un "bot" básico que simplemente twittea lo deseado a la misma
hora cada día. Para esto basta cambiar cuatro variables del script: tuit, hora, minuto, segundo.\
Adicionalmente, es necesario obtener las cuatro llaves o token de API para twitter developers, entregadas por twitter gratis en su página.

## Detalles

Hay cuatro variables al inicio del script

```
tuit = String con mensaje, máximo 280 caracteres.
hora = número entero con la hora del tiempo del día en que se desea twittear
minuto = número entero con el minuto del tiempo del día en que se desea twittear
segundo = número entero con el segundo del tiempo del día en que se desea twittear
```

Además hay otras cuatro variables que representan los TOKEN entregados para desarrolladores
```
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
```

### Requerimientos
python 3\
pip install twython\
Las cuatro llaves o token de API para twitter developers, entregadas por twitter gratis en su página.