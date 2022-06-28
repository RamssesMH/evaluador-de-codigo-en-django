def crear_dockerfile(directorio):
    """
    Crea el archivo Docker file y la imagen que permite ejecutar los scripts en un sandbox
    keyword Arguments:
        returns: ""
    """
    try:
        dockerfile = open(directorio + "/Dockerfile", "a+")
        dockerfile.write('FROM python:3.9\n')
        dockerfile.write('WORKDIR /usr/src/myapp\n')
        dockerfile.write('COPY ./code .\n')
        dockerfile.write('ENTRYPOINT ["/bin/bash"]\n')
    except Exception as e:
        pass


crear_dockerfile("code")