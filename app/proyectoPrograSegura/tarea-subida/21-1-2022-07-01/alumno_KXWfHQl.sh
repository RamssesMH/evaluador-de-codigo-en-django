[ "$1" ] || { echo "Se esperaban un parámetro";  exit 0; }
# [ -f "$1" ] || { echo "El primer parámetro debek ser un archivo existente";  exit 0; }

cat $1