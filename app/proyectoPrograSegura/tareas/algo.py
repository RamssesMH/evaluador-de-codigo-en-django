docker_compose = """'version: "3.7"

services:
  ev:
    image: {0}
    restart: always
    container_name: {1}
    volumes:
      - {2}:/entorno_ejercicio
'""".format(nombre_ejercicio, alumno_matricula.lower(), volumen, volumen_remoto)
    
enviar_dkcp = f"echo {docker_compose} > /tmp/docker-compose.yml"
    # ? Envio del archivo
Popen(['python', ruta_socket, enviar_dkcp], stdin=PIPE,
          stdout=PIPE, stderr=STDOUT).communicate()
    # ? Crear contenedor
crear_contenedor = f"cd /tmp && docker-compose up"
Popen(['python', ruta_socket, crear_contenedor], stdin=PIPE,
          stdout=PIPE, stderr=STDOUT).communicate()