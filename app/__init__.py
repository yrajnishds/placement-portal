from flask import Flask, render_template
from app.config import config
from app.extensions import db, migrate, bcrypt, login_manager



def create_app(config_name='default'):

    # Create Flask app object
    app = Flask(__name__)

    # Load config (dev / prod / testing)
    app.config.from_object(config[config_name])

    # Bind extensions to this app
    db.init_app(app)
    migrate.init_app(app, db)    # unique: needs db too
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register blueprints (MUST be inside this function!)
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from app.company import company as company_blueprint
    app.register_blueprint(company_blueprint, url_prefix='/company')

    from app.student import student as student_blueprint
    app.register_blueprint(student_blueprint, url_prefix='/student')

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)   # no prefix → handles /

    # Register error handlers
    @app.errorhandler(404)
    def not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('errors/500.html'), 500

    # Return the fully configured app
    return app