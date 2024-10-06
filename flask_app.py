from flask import Flask, request, jsonify,render_template
import sqlite3
import json
import math

app = Flask(__name__,static_url_path='/static')
port = 5000  # Puerto por defecto para Flask

# Función para conectar a la base de datos SQLite
def connect_db():
    return sqlite3.connect('preguntas.db')

def connect_db_preguntas():
    return sqlite3.connect('preguntas2.db')



@app.route('/')
def index():
    return render_template('Login.html')






@app.route('/temperatura')
def temperatura():
    data = {"temperature":40,"wind":30}
    return jsonify(data)



@app.route('/profesores')
def profesores():
    return render_template('SistemaWebProf.html')

@app.route('/admin')
def administradores():
    return render_template('SistemaWeb.html')



@app.route("/login", methods=["POST", "GET"])
def valid_login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('videojuego.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM administrador WHERE email = ? AND password = ?", (email, password))
        credencial = cursor.fetchone()

        conn.close()

        if credencial:
            return 'Acceso válido'
        else:
            return 'Credenciales inválidas'

    elif request.method == "GET":
        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()

        c.execute("SELECT * FROM administrador")
        credenciales = c.fetchall()

        conn.close()

        return jsonify(credenciales=credenciales)






@app.route('/preguntas2', methods=['GET'])
def obtener_preguntas2():
    conn = connect_db_preguntas()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM preguntas2")
    preguntas = cursor.fetchall()
    conn.close()

    preguntas_list = [{"id": pregunta[0], "pregunta": pregunta[1]} for pregunta in preguntas]

    # Envolver las preguntas en un objeto JSON
    response = {"preguntas": preguntas_list}

    return jsonify(response)




@app.route('/unity', methods=['POST'])
def doUnity():
    data = request.form['user']
    user = json.loads(data)

    print(user['list'], user['name'])  # JSON a diccionario

    response = {
        "id": 1,
        "levels": [
            {"name": 1, "played": True, "score": 100, "finished": True},
            {"name": 2, "played": True, "score": 200, "finished": True}
        ]
    }

    response["list"] = user["list"]
    response["name"] = user["name"]

    # Devolver la respuesta como JSON
    return jsonify(response)

def connect_db_videojuego():
    return sqlite3.connect('videojuego.db')

@app.route('/puntaje', methods=['POST'])
def recibir_puntaje():
    data = request.json

    nombre = data.get('nombre')
    num_lista = data.get('num_lista')
    sexo = data.get('sexo')
    puntaje_nivel_1 = data.get('puntaje_nivel_1')
    completado_nivel_1 = data.get('completado_nivel_1')
    puntaje_nivel_2 = data.get('puntaje_nivel_2')
    completado_nivel_2 = data.get('completado_nivel_2')
    puntaje_nivel_3 = data.get('puntaje_nivel_3')  # Muertes
    completado_nivel_3 = data.get('completado_nivel_3')
    puntaje_total = data.get('puntaje_total')
    progreso = data.get('progreso')

    conn = connect_db_videojuego()
    cursor = conn.cursor()

    # Insertar los datos de jugador si no existe en la tabla de jugadores
    cursor.execute("""
        INSERT OR IGNORE INTO jugadores (nombre, num_lista, sexo) VALUES (?, ?, ?);
    """, (nombre, num_lista, sexo))

    # Obtener el ID del último jugador registrado
    cursor.execute("SELECT MAX(id_jugador) FROM jugadores;")
    jugador_id = cursor.fetchone()[0]

    # Insertar un nuevo registro con los datos proporcionados en la tabla de niveles
    cursor.execute("""
        INSERT INTO niveles (id_jugador, puntaje_nivel_1, completado_nivel_1, puntaje_nivel_2, completado_nivel_2, puntaje_nivel_3, completado_nivel_3, puntaje_total, progreso)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (jugador_id, puntaje_nivel_1, completado_nivel_1, puntaje_nivel_2, completado_nivel_2, puntaje_nivel_3, completado_nivel_3, puntaje_total, progreso))

    conn.commit()
    conn.close()

    response = {"status": "success", "message": "Nuevo registro insertado correctamente en la base de datos del videojuego"}
    return jsonify(response)





@app.route('/preguntas', methods=['GET'])
def obtener_preguntas():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM preguntas")
    preguntas = cursor.fetchall()
    conn.close()

    preguntas_list = [{"id": pregunta[0], "pregunta": pregunta[1]} for pregunta in preguntas]

    # Envolver las preguntas en un objeto JSON
    response = {"preguntas": preguntas_list}

    return jsonify(response)







@app.route("/topGlobal")
def topGlobal():
        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()
        c.execute("""
        SELECT nombre, puntaje_total
        FROM jugadores
        INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
        ORDER BY puntaje_total DESC
        LIMIT 5
        """)
        top5 = c.fetchall()
        conn.close()
        return jsonify(top5)


@app.route("/topF")
def topFemenino():
        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()
        c.execute("""
        SELECT nombre, puntaje_total
        FROM jugadores
        INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
        WHERE jugadores.sexo = 0
        ORDER BY puntaje_total DESC
        LIMIT 5
        """)
        topFemenino = c.fetchall()
        conn.close()

        return jsonify(topFemenino)


@app.route("/topM")
def topMasculino():
        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()
        c.execute("""
        SELECT nombre, puntaje_total
        FROM jugadores
        INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
        WHERE jugadores.sexo = 1
        ORDER BY puntaje_total DESC
        LIMIT 5
        """)
        topMasculino = c.fetchall()
        conn.close()

        return jsonify(topMasculino)


@app.route("/peoresGlobal")
def peoresGlobal():
        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()
        c.execute("""
        SELECT nombre, puntaje_total
        FROM jugadores
        INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
        ORDER BY puntaje_total ASC
        LIMIT 5
        """)
        peoresGlobal = c.fetchall()
        conn.close()

        return jsonify(peoresGlobal)


@app.route("/peoresF")
def peoresFemenino():
        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()
        c.execute("""
        SELECT nombre, puntaje_total
        FROM jugadores
        INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
        WHERE jugadores.sexo = 0
        ORDER BY puntaje_total ASC
        LIMIT 5
        """)
        peoresFemenino = c.fetchall()
        conn.close()

        return jsonify(peoresFemenino)


@app.route("/peoresM")
def peoresMasculino():
        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()
        c.execute("""
        SELECT nombre, puntaje_total
        FROM jugadores
        INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
        WHERE jugadores.sexo = 1
        ORDER BY puntaje_total ASC
        LIMIT 5
        """)
        peoresMasculino = c.fetchall()
        conn.close()

        return jsonify(peoresMasculino)


@app.route("/puntajeMaximoNiveles")
def puntaje_maximo_niveles():
    conn = sqlite3.connect('videojuego.db')
    c = conn.cursor()

    c.execute("""
        SELECT nombre, puntaje_nivel_1
        FROM jugadores
        INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
        WHERE puntaje_nivel_1 = (SELECT MAX(puntaje_nivel_1) FROM niveles)
    """)
    puntaje_nivel_1 = c.fetchall()

    c.execute("""
        SELECT nombre, puntaje_nivel_2
        FROM jugadores
        INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
        WHERE puntaje_nivel_2 = (SELECT MAX(puntaje_nivel_2) FROM niveles)
    """)
    puntaje_nivel_2 = c.fetchall()

    c.execute("""
        SELECT nombre, puntaje_nivel_3
        FROM jugadores
        INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
        WHERE puntaje_nivel_3 = (SELECT MAX(puntaje_nivel_3) FROM niveles)
    """)
    puntaje_nivel_3 = c.fetchall()


    conn.close()

    return jsonify({
        "puntaje_maximo_nivel_1": puntaje_nivel_1,
        "puntaje_maximo_nivel_2": puntaje_nivel_2,
        "puntaje_maximo_nivel_3": puntaje_nivel_3
    })


@app.route("/progresoPromedio")
def progresoPromedio():
    conn = sqlite3.connect('videojuego.db')
    c = conn.cursor()
    c.execute("SELECT AVG(progreso) FROM niveles")
    progresoPromedio = c.fetchone()[0]
    conn.close()

    progresoPromedio = round(progresoPromedio, 2)

    return jsonify(progresoPromedio)


@app.route("/exito_fallo")
def exito_fallo_por_nivel():
    puntajes_exitosos = {1: 75, 2: 90, 3: 85}

    conn = sqlite3.connect('videojuego.db')
    c = conn.cursor()

    exito_fallo_por_nivel = {}

    for nivel, puntaje_exitoso in puntajes_exitosos.items():
        c.execute(f"""
            SELECT
                SUM(CASE WHEN puntaje_nivel_{nivel} >= {puntaje_exitoso} THEN 1 ELSE 0 END) AS exitosos,
                SUM(CASE WHEN puntaje_nivel_{nivel} < {puntaje_exitoso} THEN 1 ELSE 0 END) AS fracasados
            FROM niveles
        """)

        exitosos, fracasados = c.fetchone()
        total_jugadores = exitosos + fracasados

        porcentaje_exito = (exitosos / total_jugadores) * 100 if total_jugadores > 0 else 0
        porcentaje_fracaso = (fracasados / total_jugadores) * 100 if total_jugadores > 0 else 0

        exito_fallo_por_nivel[f"Nivel {nivel}"] = {
            "exito": porcentaje_exito,
            "fallo": porcentaje_fracaso
        }

    conn.close()

    return jsonify(exito_fallo_por_nivel)



@app.route("/crear_jugador", methods=["GET", "POST"])
def crear_jugador():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        num_lista = request.form.get("num_lista")
        sexo = request.form.get("sexo")

        sexo = 1 if sexo == "M" else 0

        puntaje_nivel_1 = request.form.get("puntaje_nivel_1")
        completado_nivel_1 = request.form.get("completado_nivel_1")
        puntaje_nivel_2 = request.form.get("puntaje_nivel_2")
        completado_nivel_2 = request.form.get("completado_nivel_2")
        puntaje_nivel_3 = request.form.get("puntaje_nivel_3")
        completado_nivel_3 = request.form.get("completado_nivel_3")
        puntaje_total = int(puntaje_nivel_1) + int(puntaje_nivel_2) + int(puntaje_nivel_3)
        progreso = math.floor(((int(completado_nivel_1) + int(completado_nivel_2) + int(completado_nivel_3)) / 3) * 100)

        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()
        c.execute("INSERT INTO jugadores (nombre, num_lista, sexo) VALUES (?, ?, ?)", (nombre, num_lista, sexo))
        jugador_id = c.lastrowid

        c.execute("""
            INSERT INTO niveles (id_jugador, puntaje_nivel_1, completado_nivel_1, puntaje_nivel_2, completado_nivel_2,
                                 puntaje_nivel_3, completado_nivel_3, puntaje_total, progreso)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (jugador_id, puntaje_nivel_1, completado_nivel_1, puntaje_nivel_2, completado_nivel_2,
              puntaje_nivel_3, completado_nivel_3, puntaje_total, progreso))
        conn.commit()
        conn.close()

        return "¡Jugador creado exitosamente!"

    # Si la solicitud es GET, renderiza el formulario
    form_html = """
    <h1>Crear Nuevo Jugador</h1>
    <form method="post">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required><br>

        <label for="num_lista">Número de Lista:</label>
        <input type="text" id="num_lista" name="num_lista" required><br>

        <label for="sexo">Sexo:</label>
        <select id="sexo" name="sexo" required>
            <option value="M">Masculino</option>
            <option value="F">Femenino</option>
        </select><br>

        <!-- Campos para la información de niveles -->
        <label for="puntaje_nivel_1">Puntaje Nivel 1:</label>
        <input type="number" id="puntaje_nivel_1" name="puntaje_nivel_1" required><br>

        <label for="completado_nivel_1">Completado Nivel 1:</label>
        <input type="number" id="completado_nivel_1" name="completado_nivel_1" required><br>

        <label for="puntaje_nivel_2">Puntaje Nivel 2:</label>
        <input type="number" id="puntaje_nivel_2" name="puntaje_nivel_2" required><br>

        <label for="completado_nivel_2">Completado Nivel 2:</label>
        <input type="number" id="completado_nivel_2" name="completado_nivel_2" required><br>

        <label for="puntaje_nivel_3">Puntaje Nivel 3:</label>
        <input type="number" id="puntaje_nivel_3" name="puntaje_nivel_3" required><br>

        <label for="completado_nivel_3">Completado Nivel 3:</label>
        <input type="number" id="completado_nivel_3" name="completado_nivel_3" required><br>

        <!-- Campos para puntaje total-->
        <label for="puntaje_total">Puntaje Total:</label>
        <input type="number" id="puntaje_total" name="puntaje_total" readonly><br>

        <!-- Campo para progreso -->
        <label for="progreso">Progreso (%):</label>
        <input type="number" id="progreso" name="progreso" required><br>

        <button type="submit">Guardar Jugador</button>
    </form>
    <script>
        // Calcular puntaje total y progreso al ingresar datos
        function calcularPuntajeYProgreso() {
            var puntajeNivel1 = parseInt(document.getElementById("puntaje_nivel_1").value) || 0;
            var puntajeNivel2 = parseInt(document.getElementById("puntaje_nivel_2").value) || 0;
            var puntajeNivel3 = parseInt(document.getElementById("puntaje_nivel_3").value) || 0;
            var completadoNivel1 = parseInt(document.getElementById("completado_nivel_1").value) || 0;
            var completadoNivel2 = parseInt(document.getElementById("completado_nivel_2").value) || 0;
            var completadoNivel3 = parseInt(document.getElementById("completado_nivel_3").value) || 0;

            var puntajeTotal = puntajeNivel1 + puntajeNivel2 + puntajeNivel3;
            var progreso = Math.floor(((completadoNivel1 + completadoNivel2 + completadoNivel3) / 3) * 100);

            document.getElementById("puntaje_total").value = puntajeTotal;
            document.getElementById("progreso").value = progreso.toFixed(2);
        }

        var inputs = document.querySelectorAll("input[type='number']");
        inputs.forEach(function(input) {
            input.addEventListener("input", calcularPuntajeYProgreso);
        });
    </script>
    """
    return form_html


@app.route("/leer_jugador", methods=["POST", "GET"])
def leer_jugador():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        num_lista = request.form.get("num_lista")

        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()

        c.execute("""
            SELECT jugadores.nombre, jugadores.num_lista,
                  niveles.puntaje_nivel_1, niveles.completado_nivel_1,
                  niveles.puntaje_nivel_2, niveles.completado_nivel_2,
                  niveles.puntaje_nivel_3, niveles.completado_nivel_3,
                  niveles.puntaje_total, niveles.progreso
            FROM jugadores
            INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
            WHERE jugadores.nombre = ? AND jugadores.num_lista = ?
        """, (nombre, num_lista))

        info_jugador = c.fetchone()

        conn.close()

        if info_jugador:
            html_response = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Información del Jugador</title>
            </head>
            <body>
                <h2>Información del Jugador</h2>
                <p>Nombre: {info_jugador[0]}</p>
                <p>Número de Lista: {info_jugador[1]}</p>
                <p>Puntaje Nivel 1: {info_jugador[2]}</p>
                <p>Nivel 1 Completado: {"Sí" if info_jugador[3] else "No"}</p>
                <p>Puntaje Nivel 2: {info_jugador[4]}</p>
                <p>Nivel 2 Completado: {"Sí" if info_jugador[5] else "No"}</p>
                <p>Puntaje Nivel 3: {info_jugador[6]}</p>
                <p>Nivel 3 Completado: {"Sí" if info_jugador[7] else "No"}</p>
                <p>Puntaje Total: {info_jugador[8]}</p>
                <p>Progreso: {info_jugador[9]}</p>
            </body>
            </html>
            """
            return html_response
        else:
            return "No se encontró información para el jugador especificado."

    elif request.method == 'GET':
        form_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Consulta de Información del Jugador</title>
        </head>
        <body>
            <h2>Consulta de Información del Jugador</h2>
            <form method="post">
                <label for="nombre">Nombre del Jugador:</label><br>
                <input type="text" id="nombre" name="nombre" required><br>

                <label for="num_lista">Número de Lista:</label><br>
                <input type="text" id="num_lista" name="num_lista" required><br>

                <input type="submit" value="Consultar Información">
            </form>
        </body>
        </html>
        """
        return form_html


@app.route("/actualizar_jugador", methods=["POST", "GET"])
def actualizar_jugador():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        num_lista = request.form.get("num_lista")

        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()

        c.execute("""
            SELECT jugadores.nombre, jugadores.num_lista, jugadores.sexo,
                  niveles.puntaje_nivel_1, niveles.completado_nivel_1,
                  niveles.puntaje_nivel_2, niveles.completado_nivel_2,
                  niveles.puntaje_nivel_3, niveles.completado_nivel_3,
                  niveles.puntaje_total, niveles.progreso
            FROM jugadores
            INNER JOIN niveles ON jugadores.id_jugador = niveles.id_jugador
            WHERE jugadores.nombre = ? AND jugadores.num_lista = ?
        """, (nombre, num_lista))

        info_jugador = c.fetchone()

        conn.close()

        if info_jugador:
            form_html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Actualizar Información del Jugador</title>
            </head>
            <body>
                <h2>Actualizar Información del Jugador</h2>
                <form method="post" action="/actualizar_info_jugador">
                    <label for="nombre_original">Nombre Original:</label><br>
                    <input type="text" id="nombre_original" name="nombre_original" value="{nombre}" readonly><br>

                    <label for="num_lista_original">Número de Lista Original:</label><br>
                    <input type="text" id="num_lista_original" name="num_lista_original" value="{num_lista}" readonly><br>

                    <label for="nombre">Nuevo Nombre del Jugador:</label><br>
                    <input type="text" id="nombre" name="nombre" value="{nombre}" required><br>

                    <label for="num_lista">Nuevo Número de Lista:</label><br>
                    <input type="text" id="num_lista" name="num_lista" value="{num_lista}" required><br>

                    <label for="sexo">Nuevo Sexo:</label><br>  <!-- Agregamos el campo para el sexo -->
                    <select id="sexo" name="sexo" required>
                        <option value="1" {"selected" if info_jugador[2] == 1 else ""}>Masculino</option>
                        <option value="0" {"selected" if info_jugador[2] == 0 else ""}>Femenino</option>
                    </select><br>

                    <label for="puntaje_nivel_1">Puntaje Nivel 1:</label><br>
                    <input type="text" id="puntaje_nivel_1" name="puntaje_nivel_1" value="{info_jugador[3]}"><br>

                    <label for="completado_nivel_1">Nivel 1 Completado:</label><br>
                    <input type="text" id="completado_nivel_1" name="completado_nivel_1" value="{info_jugador[4]}"><br>

                    <label for="puntaje_nivel_2">Puntaje Nivel 2:</label><br>
                    <input type="text" id="puntaje_nivel_2" name="puntaje_nivel_2" value="{info_jugador[5]}"><br>

                    <label for="completado_nivel_2">Nivel 2 Completado:</label><br>
                    <input type="text" id="completado_nivel_2" name="completado_nivel_2" value="{info_jugador[6]}"><br>

                    <label for="puntaje_nivel_3">Puntaje Nivel 3:</label><br>
                    <input type="text" id="puntaje_nivel_3" name="puntaje_nivel_3" value="{info_jugador[7]}"><br>

                    <label for="completado_nivel_3">Nivel 3 Completado:</label><br>
                    <input type="text" id="completado_nivel_3" name="completado_nivel_3" value="{info_jugador[8]}"><br>

                    <label for="puntaje_total">Puntaje Total:</label><br>
                    <input type="text" id="puntaje_total" name="puntaje_total" value="{info_jugador[9]}"><br>

                    <label for="progreso">Progreso:</label><br>
                    <input type="text" id="progreso" name="progreso" value="{info_jugador[10]}"><br>

                    <input type="submit" value="Actualizar Información">
                </form>
            </body>
            </html>
            """
            return form_html
        else:
            return "No se encontró información para el jugador especificado."

    elif request.method == 'GET':
        form_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Actualizar Información del Jugador</title>
        </head>
        <body>
            <h2>Actualizar Información del Jugador</h2>
            <form method="post">
                <label for="nombre">Nombre del Jugador:</label><br>
                <input type="text" id="nombre" name="nombre" required><br>

                <label for="num_lista">Número de Lista:</label><br>
                <input type="text" id="num_lista" name="num_lista" required><br>

                <input type="submit" value="Consultar Información">
            </form>
        </body>
        </html>
        """
        return form_html


@app.route("/actualizar_info_jugador", methods=["POST"])
def actualizar_info_jugador():
    nombre_original = request.form.get("nombre_original")
    num_lista_original = request.form.get("num_lista_original")
    nombre = request.form.get("nombre")
    num_lista = request.form.get("num_lista")
    sexo = request.form.get("sexo")
    puntaje_nivel_1 = request.form.get("puntaje_nivel_1")
    completado_nivel_1 = request.form.get("completado_nivel_1")
    puntaje_nivel_2 = request.form.get("puntaje_nivel_2")
    completado_nivel_2 = request.form.get("completado_nivel_2")
    puntaje_nivel_3 = request.form.get("puntaje_nivel_3")
    completado_nivel_3 = request.form.get("completado_nivel_3")
    puntaje_total = request.form.get("puntaje_total")
    progreso = request.form.get("progreso")

    conn = sqlite3.connect('videojuego.db')
    c = conn.cursor()

    c.execute("""
        SELECT id_jugador
        FROM jugadores
        WHERE nombre = ? AND num_lista = ?
    """, (nombre_original, num_lista_original))
    jugador = c.fetchone()
    if not jugador:
        conn.close()
        return "No se encontró información para el jugador especificado."

    jugador_id = jugador[0]

    c.execute("""
        UPDATE jugadores
        SET nombre = ?, num_lista = ?, sexo = ?
        WHERE id_jugador = ?
    """, (nombre, num_lista, sexo, jugador_id))

    c.execute("""
        UPDATE niveles
        SET puntaje_nivel_1 = ?, completado_nivel_1 = ?,
            puntaje_nivel_2 = ?, completado_nivel_2 = ?,
            puntaje_nivel_3 = ?, completado_nivel_3 = ?,
            puntaje_total = ?, progreso = ?
        WHERE id_jugador = ?
    """, (puntaje_nivel_1, completado_nivel_1, puntaje_nivel_2, completado_nivel_2,
          puntaje_nivel_3, completado_nivel_3, puntaje_total, progreso, jugador_id))

    conn.commit()

    conn.close()

    return "¡La información del jugador ha sido actualizada exitosamente!"


@app.route("/borrar_jugador", methods=["POST", "GET"])
def borra_jugador():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        num_lista = request.form.get("num_lista")

        conn = sqlite3.connect('videojuego.db')
        c = conn.cursor()


        c.execute("SELECT id_jugador FROM jugadores WHERE nombre = ? AND num_lista = ?", (nombre, num_lista))
        jugador_id = c.fetchone()

        if jugador_id:
            jugador_id = jugador_id[0]
            c.execute("DELETE FROM niveles WHERE id_jugador = ?", (jugador_id,))
            c.execute("DELETE FROM jugadores WHERE id_jugador = ?", (jugador_id,))

            conn.commit()
            conn.close()

            return "¡El jugador y su información han sido eliminados exitosamente!"

        else:
            conn.close()
            return "No se encontró el jugador especificado."

    elif request.method == 'GET':
        form_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Borrar Jugador y su Información</title>
        </head>
        <body>
            <h2>Borrar Jugador y su Información</h2>
            <form method="post">
                <label for="nombre">Nombre del Jugador:</label><br>
                <input type="text" id="nombre" name="nombre" required><br>

                <label for="num_lista">Número de Lista:</label><br>
                <input type="text" id="num_lista" name="num_lista" required><br>

                <input type="submit" value="Borrar Jugador y su Información">
            </form>
        </body>
        </html>
        """
        return form_html


if __name__ == '_main_':
    app.run(port=port, debug=True)