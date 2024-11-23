import sqlite3

# Función para convertir la imagen a formato binario
def convertir_imagen_a_binario(ruta_imagen):
    with open(ruta_imagen, 'rb') as archivo:
        return archivo.read()

# Conectar a la base de datos (se creará si no existe)
conexion = sqlite3.connect('imagenes.db')

# Crear un cursor
cursor = conexion.cursor()

# Crear la tabla 'personas' si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        correo TEXT NOT NULL,
        imagen BLOB
    )
''')

# Confirmar la creación de la tabla
conexion.commit()

# Definir los valores de los campos para 6 personas
personas = [
    {"nombre": "Julian", "apellido": "Nova", "correo": "julian.nova@gmail.com", "ruta_imagen": "julian.jpeg"},
    {"nombre": "Felipe", "apellido": "Trivino", "correo": "felipe.trivino@gmail.com", "ruta_imagen": "felipe.jpeg"},
    {"nombre": "Lucho", "apellido": "Romero", "correo": "luis.romero@gmail.com", "ruta_imagen": "lucho.jpeg"},
    {"nombre": "Alejandra", "apellido": "Correa", "correo": "alejandra.correa@gmail.com", "ruta_imagen": "alejandra.jpeg"},
    {"nombre": "Tomas", "apellido": "Vera", "correo": "tomas.vera@gmail.com", "ruta_imagen": "tomas.jpeg"},
    {"nombre": "Nicolas", "apellido": "Moreo", "correo": "nicolas.moreno@gmail.com", "ruta_imagen": "nicolas.jpeg"}
]

# Insertar los registros en la base de datos
for persona in personas:
    imagen_binaria = convertir_imagen_a_binario(persona["ruta_imagen"])
    
    cursor.execute('''
        INSERT INTO personas (nombre, apellido, correo, imagen)
        VALUES (?, ?, ?, ?)
    ''', (persona["nombre"], persona["apellido"], persona["correo"], imagen_binaria))

# Confirmar la inserción de los registros
conexion.commit()

# Cerrar la conexión
conexion.close()

print("Registros insertados exitosamente y tabla creada (si no existía).")
