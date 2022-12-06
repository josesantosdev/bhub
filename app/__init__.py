from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    
    #Models
    from app.models.costumer_model import Costumer
    from app.models.bank_details_model import BankDetail
    
    #Controllers
    from app.controllers.costumer_controller import CostumerController

    #Blueprints
    app.register_blueprint(CostumerController.costumer_controller, url_prefix='/api/v1/clientes')
    
    return app
    