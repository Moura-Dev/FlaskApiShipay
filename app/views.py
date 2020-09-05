from flask import Blueprint, jsonify, request
from .models import Transacao
from . import db

main = Blueprint('main', __name__)


@main.route('/api/v1/transacao/')
def Consultar_TransacaoCpf():
    consultar = Transacao.query.all()

    tr = []

    for t in consultar:
        tr.append({'id': t.id, 'estabelecimento': t.estabelecimento, 'cliente': t.cliente, 'valor': t.valor, 'descricao': t.descricao ,})

    return jsonify(tr)


@main.route('/api/v1/transacao/<cpf>')
def Consultar_Transacao(cpf):
    if len(cpf) == 11:
        cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]

    if len(cpf) < 11 or len(cpf) > 14:
        return jsonify('CPF invalido')

    consultar = Transacao.query.filter(Transacao.cliente == cpf)

    tr = []

    for t in consultar:
        tr.append({'id': t.id, 'estabelecimento': t.estabelecimento, 'cliente': t.cliente, 'valor': t.valor, 'descricao': t.descricao ,})

    return jsonify(tr)



@main.route('/api/v1/transacao/', methods=['POST'])
def Add_Transacao():
    tr_data = request.get_json()

    new_tr = Transacao(estabelecimento=tr_data['estabelecimento'], cliente=tr_data['cliente'], valor=tr_data['valor'], descricao=tr_data['descricao'])

    db.session.add(new_tr)
    db.session.commit()

    return {'aceito': True}