##### Importacion de Librerias y Depemdemcias.
import locale
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from functools import wraps
from web_app import app
##### Formato de hora y fecha local.
locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')

# Middleware para proteger rutas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, inicia sesión para acceder a esta página.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Decorador para verificar si el usuario tiene un rol específico
def role_required(*required_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Debes iniciar sesión para acceder a esta página.', 'error')
                return redirect(url_for('login'))
            
            user_role = session.get('role')
            
            if user_role not in required_roles: # Verifica si el rol del usuario NO ESTÁ en los roles requeridos
                nombre = session.get('nombre')
                apellido = session.get('apellido')
                nombre_completo = f"{nombre} {apellido}" if nombre and apellido else "Usuario"   # Obtener nombre completo
                flash(('No tienes permiso para acceder a esta página.', nombre_completo), 'error')
                return redirect(url_for('peliculas_contenido'))  # Redirigir a una página sin restricciones
            return f(*args, **kwargs)
        return decorated_function
    return decorator

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
    
#################### CONTROLADOR PARA SALIR DEL SISTEMA   
@app.route('/logout')
def logout():
     # Elimina los datos de la sesión
    session.clear()
    flash('Has cerrado sesión correctamente.' , 'info')
    
    return redirect(url_for('login'))


# Desactivar caché en rutas protegidas
@app.after_request
def no_cache(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response