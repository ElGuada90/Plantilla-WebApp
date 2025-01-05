##### Importacion de Librerias y Depemdemcias.
import locale
from datetime import datetime
from flask import render_template
from web_app import app
##### Formato de hora y fecha local.
locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')

##### Controlador y Ruta para la vista de pagina de inicio o Index.
@app.route('/')
@app.route('/index')
def index():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y a las %I:%M:%S %p")

    return render_template(
        "index.html",
        title = "ElGuada90",
        message = "Bienvenidos",
        content = formatted_now.capitalize())
    
##### Controlador y Ruta para la vista de la pagina Canal.
@app.route('/micanal')
def micanal():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y a las %I:%M:%S %p")

    return render_template(
        "micanal.html",
        title = "ElGuada90",
        message = "Top Apps",
        content = formatted_now.capitalize())