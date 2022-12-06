from app import db, ma

from sqlalchemy import Column, BigInteger, String, Float

from sqlalchemy.orm import relationship

from marshmallow import fields

from app.models.bank_details_model import BankDetailSchema, BankDetail



class Costumer(db.Model):
    
    __tablename__ = 'Costumer'
    id_cliente = Column(BigInteger, primary_key=True)
    razao_social = Column(String(60), nullable=False)
    telefone = Column(BigInteger)
    endereco = Column(String(155))
    faturamento_declarado = Column(Float, nullable=False)
    dados_bancarios = relationship(BankDetail, backref='Costumer', lazy="dynamic")
    
    
    def __init__(self, razao_social, telefone, endereco, faturamento_declarado) -> None:
        self.razao_social = razao_social
        self.telefone = telefone
        self.endereco = endereco
        self.faturamento_declarado = faturamento_declarado
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def __repr__(self) -> str:
        return f'<id_cliente: {self.id_cliente}'
    
    
class CostumerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Costumer
        load_instance = True
        sqla_session = db.session
        include_relationship = True
        include_fk = True
        
    id_cliente = fields.Integer(dump_only=True)
    razao_social = fields.Str()
    telefone = fields.Integer()
    endereco = fields.Str()
    faturamento_declarado = fields.Float()
    dados_bancarios = fields.Nested(BankDetailSchema(many=True))
       
        
    _links = ma.Hyperlinks({
        "collection": ma.URLFor('costumer_controller.get_costumer'),
        "self": ma.URLFor('costumer_controller.get_costumer_by_id', values=dict(id_cliente="<id_cliente>"))
    })
 