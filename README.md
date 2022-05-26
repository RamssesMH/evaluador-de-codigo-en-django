# Prueba piloto farmacia

Proyecto que contiene el proyecto de Programación Segua

## Getting started

## Intalar ccrypt
```
sudo apt-get install ccrypt
```

## crear archivo conf.en en el directorio ráiz del proyecto (donde se encuentra el archivo manage.py)
```

nano conf.env

- Agrega las variables de entorno sin comillas y sin espacios
- Agrega una variable de entorno por linea
- Variables necesarias: LLAVEDJANGO,NAMEDB,USERDB,PASSWORDDB,HOSTDB,PORTDB 

ej.		LLAVEDJANGO=llave-a-crear
```


## Cifrar el archivo conf.env
```
- ccencrypt conf.env
```

## Asegurate que el servicio de base de datos de MySQL está activo y configurado correctamente
```
- Configura usuario y contraseña
- Crea la base de datos
```
## Dar permisos a archivo conf.env y ejecutarlo con el archivo de conf.env.cpt como parámetro
```
- chmod +x levantar_servidor.sh

- ./levantar_servidor.sh conf.env.cpt
```



## Levantar los contenedores
```
docker-compose up -d
```

