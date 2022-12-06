from app import db, ma

from sqlalchemy import Column, BigInteger, ForeignKey

from marshmallow import fields


class BankDetail(db.Model):
    __tablename__ = "BankDetail"
    id_conta_banco = Column(BigInteger, primary_key=True)
    agencia = Column(BigInteger, nullable=False)
    conta = Column(BigInteger, nullable=False)
    banco = Column(BigInteger, nullable=False)
    id_cliente = Column(BigInteger, ForeignKey('Costumer.id_cliente'))
 
    
    def __init__(self, agencia, conta, banco, id_cliente) -> None:
       self.agencia = agencia
       self.conta = conta
       self.banco = banco
       self.id_cliente = id_cliente
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def __repr__(self) -> str:
      return f'<id_conta_banco: {self.id_conta_banco}'
  
  
class BankDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BankDetail
        load_instance = True
        sqla_session = db.session
        include_relationship = True
        include_fk = True
        
        id_conta_banco = fields.Integer(dump_only=True)
        agencia = fields.Integer()
        conta = fields.Integer()
        banco = fields.Integer()
        id_cliente = fields.Integer()        
        
    '''    
    _links = ma.Hyperlinks({
        "collection": ma.URLFor(''),
        "self": ma.URLFor('')
    })
    '''    
    
    