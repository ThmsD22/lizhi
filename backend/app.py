from flask import Flask
from backend.extensions import db, cors
from backend.models.database_models import Variety, ProductionArea, Farmer, Comment, Like # Make sure all models are imported

def create_app():
    app = Flask(__name__)

    # Configuration
    # TODO: Replace with MySQL connection string from environment variable for production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./development.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    # Allowing all origins for /api/ routes for now, can be configured more strictly.
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    # Create database tables if they don't exist
    # In a real application, Flask-Migrate is a better choice for managing schema changes.
    with app.app_context():
        db.create_all()

    @app.route('/')
    def hello():
        return "Hello from Flask Backend with DB setup!"

    # Register Blueprints for API routes
    from backend.routes.variety_routes import variety_bp
    from backend.routes.production_area_routes import production_area_bp
    from backend.routes.farmer_routes import farmer_bp

    app.register_blueprint(variety_bp, url_prefix='/api/varieties')
    app.register_blueprint(production_area_bp, url_prefix='/api/production_areas')
    app.register_blueprint(farmer_bp, url_prefix='/api/farmers')

    from backend.routes.comment_routes import comment_bp
    from backend.routes.like_routes import like_bp
    app.register_blueprint(comment_bp, url_prefix='/api/comments')
    app.register_blueprint(like_bp, url_prefix='/api/likes')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
