import sqlite3
import random

# Conexión a la base de datos (si no existe, se crea)
conn = sqlite3.connect('preguntas.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla preguntas
cursor.execute('''CREATE TABLE IF NOT EXISTS preguntas (
                    id INTEGER PRIMARY KEY,
                    pregunta TEXT NOT NULL
                )''')

# Lista de preguntas aleatorias
preguntas = [
    "¿Cuál es la capital de inglaterra?",
    "¿Cuántos planetas hay en el sistema solar?",
    "¿Cuál es el río más largo del mundo?",
    "¿Quién escribió la obra 'Romeo y Julieta'?",
    "¿Cuál es el animal terrestre más grande del mundo?"
]

# Insertar las preguntas en la tabla
for pregunta in preguntas:
    cursor.execute("INSERT INTO preguntas (pregunta) VALUES (?)", (pregunta,))

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Base de datos creada exitosamente.")


conn = sqlite3.connect('muertes.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla muertes
cursor.execute('''CREATE TABLE IF NOT EXISTS muertes (
                    id INTEGER PRIMARY KEY,
                    muerte INTEGER
                )''')

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Base de datos de muertes creada exitosamente.")




# Conexión a la base de datos (si no existe, se crea)
conn = sqlite3.connect('muertes.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla muertes
cursor.execute('''CREATE TABLE IF NOT EXISTS muertes (
                    id INTEGER PRIMARY KEY,
                    muerte INTEGER
                )''')

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Base de datos de muertes creada exitosamente.")
conexion = sqlite3.connect("videojuego.db")
cursor = conexion.cursor()

def create_admin_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS administrador(
            id_admin INTEGER primary key,
            email  varchar(50),
            password varchar(10)
                   );
                   """)



def create_players_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugadores(
            id_jugador INTEGER primary key,
            nombre varchar(50),
            num_lista varchar(2),
            sexo INTEGER
    );
    """)




def create_levels_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS niveles (
        id_registro_nivel INTEGER PRIMARY KEY,
        id_jugador INTEGER,
        puntaje_nivel_1 INTEGER,
        completado_nivel_1 INTEGER,
        puntaje_nivel_2 INTEGER,
        completado_nivel_2 INTEGER,
        puntaje_nivel_3 INTEGER,
        completado_nivel_3 INTEGER,
        puntaje_total INTEGER,
        progreso INTEGER,

        FOREIGN KEY (id_jugador) REFERENCES jugadores (id_jugador)
    );
    """)



create_admin_table()
create_players_table()
create_levels_table()


conexion.commit()

def insertar_administradores():
    cursor.execute("SELECT COUNT(*) FROM administrador")
    if cursor.fetchone()[0] == 0:
        credenciales_iniciales = [
            ('diegoaguilar@admin.com', 'diego12345'),
            ('rodrigofernando@admin.com', 'rodrigo09876'),
            ('manuelantonio@admin.com', 'manuel13579'),
            ('davidalonso@admin.com', 'david24680'),
            ('joseangel@admin.com', 'jose12457')
        ]
        cursor.executemany("INSERT INTO administrador (email, password) VALUES (?, ?)", credenciales_iniciales)
        conexion.commit()

def insertar_jugadores():
    cursor.execute("SELECT COUNT(*) FROM jugadores")
    if cursor.fetchone()[0] == 0:
        jugadores = [
            ('Diego Aguilar', '1', '1'),
            ('Rodrigo Fernández', '2', '1'),
            ('Manuel Antonio', '3', '1'),
            ('David Alonso', '4', '1'),
            ('José Ángel', '5', '1'),
            ('Eduardo Pérez', '6', '1'),
            ('Luis Fernando', '7', '1'),
            ('Manuel Rodríguez', '8', '1'),
            ('Daniel Alonso', '9', '1'),
            ('José Antonio', '10', '1'),
            ('Nicole Rendon', '11', '0'),
            ('Sofía Campestre', '12', '0'),
            ('Antonia Hernández', '13', '0'),
            ('Julia Torres', '14', '0'),
            ('Gabriela Gómez', '15', '0'),
            ('Regina Ruiz', '16', '0'),
            ('Frida Sofía', '17', '0'),
            ('Dafne García', '18', '0'),
            ('Ashley Pérez', '19', '0'),
            ('Maria Eugenia', '20', '0')
        ]
        cursor.executemany("INSERT INTO jugadores (nombre, num_lista, sexo) VALUES (?, ?, ?)", jugadores)
        conexion.commit()

def insertar_niveles():
    cursor.execute("SELECT COUNT(*) FROM niveles")
    if cursor.fetchone()[0] == 0:
        niveles = [
            (1, 1000, 1, 950, 1, 800, 1, 2750, 100),
            (2, 950, 1, 900, 1, 0, 0, 1850, 66),
            (3, 800, 1, 0, 0, 0, 0, 800, 33),
            (4, 750, 1, 700, 1, 0, 0, 1450, 66),
            (5, 700, 1, 650, 1, 600, 1, 1950, 100),
            (6, 600, 1, 550, 1, 500, 1, 1650, 100),
            (7, 550, 1, 0, 0, 0, 0, 550, 33),
            (8, 500, 1, 450, 1, 400, 1, 1350, 100),
            (9, 400, 1, 0, 0, 0, 0, 400, 33),
            (10, 350, 1, 300, 1, 250, 1, 900, 100),
            (11, 300, 1, 250, 1, 200, 1, 750, 100),
            (12, 250, 1, 200, 1, 150, 1, 600, 100),
            (13, 200, 1, 0, 0, 0, 0, 200, 33),
            (14, 150, 1, 100, 1, 50, 1, 300, 100),
            (15, 100, 1, 50, 1, 0, 1, 150, 100),
            (16, 50, 1, 0, 1, 0, 0, 50, 66),
            (17, 0, 0, 0, 0, 0, 0, 0, 0),
            (18, 950, 1, 900, 1, 850, 1, 2700, 100),
            (19, 800, 1, 750, 1, 700, 1, 2250, 100),
            (20, 750, 1, 700, 1, 650, 1, 2100, 100)
        ]
        cursor.executemany("INSERT INTO niveles (id_jugador, puntaje_nivel_1, completado_nivel_1, puntaje_nivel_2, completado_nivel_2, puntaje_nivel_3, completado_nivel_3, puntaje_total, progreso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", niveles)
        conexion.commit()

insertar_administradores()
insertar_jugadores()
insertar_niveles()

conexion.close()


conn = sqlite3.connect('preguntas2.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla preguntas2
cursor.execute('''CREATE TABLE IF NOT EXISTS preguntas2 (
                    id INTEGER PRIMARY KEY,
                    pregunta TEXT NOT NULL
                )''')

# Lista de preguntas sobre matemáticas
preguntas_matematicas = [
    "¿Cuál es el resultado de 2 + 2?",
    "¿Cuánto es la raíz cuadrada de 16?",
    "¿Cuánto es 5 multiplicado por 7?",
    "¿Cuál es el resultado de 10 - 3?",
    "¿Cuánto es 25 dividido por 5?"
]

# Insertar las preguntas de matemáticas en la tabla preguntas2
for pregunta in preguntas_matematicas:
    cursor.execute("INSERT INTO preguntas2 (pregunta) VALUES (?)", (pregunta,))

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Base de datos preguntas2 creada exitosamente.")
