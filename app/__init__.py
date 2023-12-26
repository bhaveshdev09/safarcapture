from flask import Flask


# Create Flask App
def create_app():
    app = Flask(__name__)

    # Define URL Routers
    from app.routes import router

    app.register_blueprint(router)

    return app
