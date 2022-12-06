from app import db, ma

from sqlalchemy import Column, BigInteger, String, Float

from marshmallow import fields


class Costumer(db.Model):
    
    __tablename__ = 'ClienteTable'
    id_cliente = Column(BigInteger, primary_key=True)
    razao_social = Column(String(60), nullable=False)
    telefone = Column(BigInteger)
    endereco = Column(String(155))
    faturamento_declarado = Column(Float, nullable=False)
    
    
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
        
        id_cliente = fields.Integer(dump_only=True)
        razao_social = fields.Str()
        telefone = fields.Integer()
        endereco = fields.Str()
        faturamento_declarado = fields.Float()
    '''    
    _links = ma.Hyperlinks({
        "collection": ma.URLFor(''),
        "self": ma.URLFor('')
    })
    '''    