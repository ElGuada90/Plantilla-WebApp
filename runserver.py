import os

from web_app import app    # Imports the code from web_app/__init__.py

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = int(os.environ.get('SERVER_PORT', '1991'))
    except ValueError:
        PORT = 1991
        
    app.run(HOST, PORT, debug=True)