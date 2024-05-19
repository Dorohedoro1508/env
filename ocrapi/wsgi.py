from waitress import serve
from ocrapi.main import app as application  # Asume que `app` es tu aplicación Flask

if __name__ == "__main__":
    # Esta parte se ejecutará solo cuando ejecutes el script directamente
    application.run()
else:
    # Esta parte se ejecutará cuando el script sea importado como un módulo
    serve(application, host='0.0.0.0', port=8080)
    # Para ejecutar el script, ejecuta:
    # $ python3 app.py

    # Para ejecutar el script como un módulo, ejecuta:

    # $ python3 -m app

    # Para ejecutar el script como un módulo en un puerto diferente, ejecuta:

    # $ python3 -m app --port 8081

    # Para ejecutar el script como un módulo en un puerto y host diferentes, ejecuta:

    # $ python3 -m app --host 0.0.0.0 --port 8081

    # Para ejecutar el script como un módulo en un puerto y host diferentes, ejecuta:

    # $ python3 -m app --host 0.0.0.0 --port 8081   