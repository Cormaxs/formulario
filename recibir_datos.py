from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  return render_template("index.html")  # Renderiza el formulario HTML

@app.route("/recibir_datos", methods=["POST"])
def recibir_datos():
  # Obtiene los datos del formulario
  nombre = request.form.get("nombre")
  precio = request.form.get("precio")

  # Maneja posibles errores (por ejemplo, campos vacíos)
  if not nombre or not precio:
    return render_template("error.html", mensaje="Faltan datos del producto.")

  # Procesa el precio (convierte a float si es necesario)
  try:
    precio = float(precio)
  except ValueError:
    return render_template("error.html", mensaje="Precio inválido (debe ser un número).")

  # Obtiene el archivo de imagen (si se ha proporcionado)
  imagen = request.files.get("imagen")

  # Guarda los datos del formulario (reemplaza con tu lógica real de almacenamiento de datos)
  # ... (por ejemplo, guardar en una base de datos, crear un archivo de producto)

  # Muestra un mensaje de éxito o redirige a otra página
  return render_template("success.html", nombre=nombre, precio=precio)  # Pasa datos a la plantilla de éxito

@app.route("/error.html")
def error():
  return render_template("error.html")  # Muestra la plantilla de error

@app.route("/success.html")
def success():
  nombre = request.args.get("nombre")  # Accede a los datos pasados en los parámetros de la consulta
  precio = request.args.get("precio")
  return render_template("success.html", nombre=nombre, precio=precio)  # Muestra la plantilla de éxito

if __name__ == "__main__":
  app.run(debug=True)

