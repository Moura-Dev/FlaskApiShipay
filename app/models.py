from . import db

class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estabelecimento = db.Column(db.String(100))
    cliente = db.Column(db.String(100))
    valor = db.Column(db.Float())
    descricao = db.Column(db.String(100))
