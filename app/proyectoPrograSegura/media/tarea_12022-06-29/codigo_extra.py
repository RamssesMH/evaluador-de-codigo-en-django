def ejecutar_script(content):  # PENDIENTE PORQUE YA NO SE UTILIZARA
    """
        todo: En proceso: Ejecución del script que mando el alumno
    """
    ruta_archivo = guardar_archivo_en_ruta_especifica(content)
    # Asignamos permisos
    comando = f"chmod +x {ruta_archivo}"
    dar_permisos = Popen(
        comando,
        shell=True,
        stdin=PIPE,
        stdout=PIPE,
        stderr=STDOUT,
    )
    # Ejecución del script
    ejecutar = f"{ruta_archivo} susan"
    dar_ejecucion = Popen(ejecutar,
                          shell=True,
                          stdin=PIPE,
                          stdout=PIPE,
                          stderr=STDOUT)
    stdout = dar_ejecucion.communicate()[0].decode("utf-8").rstrip("\n")
    stderr = dar_ejecucion.communicate()[1]
    salida_esperada = "hola, es una prueba susan"
    if salida_esperada == stdout:
        print("Código correcto")
        return
    print(stderr)


def guardar_archivo_en_ruta_especifica(content):
    """
    ! Está función almacena el archivo subido por el alumno en un directorio especial del sistema
    """
    extension = content.name.split('.')[1]
    name_file = 'otra_prueba'
    ruta_destino = os.path.join('/tmp', name_file + '.' + extension)
    guardar_contenido = open(ruta_destino, "wb")
    for chunk in content.chunks():
        guardar_contenido.write(chunk)
    guardar_contenido.close()
    return ruta_destino


fecha_creacion = datetime.date.today()
nombre_ejercicio = EjercicioDefinido.objects.filter(
    id=id_ejercicio).values("titulo")
nombre_ejercicio = str(nombre_ejercicio).split(":")[
    1].split("'")[1].strip().replace(" ", "_").lower()
print(nombre_ejercicio)
ruta_salvar = "scripts/{0}/{1}/{2}/{3}".format(fecha_creacion,
                                               alumno_matricula,
                                               nombre_ejercicio,
                                               content)
