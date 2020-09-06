# APi-FLASK-PYTHON
Desafio Shipay :


# Modelo de Uso com Docker:

no terminal execute o build:

docker-compose -f "docker-compose.yml" up -d --build

Apos subir o docker a aplicação esta pronta para uso.



# Endpoint Post:
Modelo de post Url Esperada pela API:
Method: POST
url = /api/v1/transacao (POST)

{
   "estabelecimento": "45.283.163/0001-67",
   "cliente": "094.214.930-01",
   "valor": 590.01,
   "descricao": "Almoço em restaurante chique pago via Shipay!"
}

# Endpoint Consultar Transacoes (Listar todas as transacoes no banco):

Method: Get
url =  /api/v1/transacao (GET)


# Endpoint Consultar Transacoes pelo campo  cliente:

Method: GET

url = /api/v1/transacao/parametrocpf"/ (GET)

modelo de url = /api/v1/transacao/095.215.910-01       ou     /api/v1/transacao/09521591001

Modelo de cpf esperado com caracteres: 094.214.930-01
Modelo de cpf esperado sem caracteres: 09421493001





# Modo de uso sem docker:

# Crie um virtualenv 
python3 -m virtualenv venv

# Ativar virtualenv
source /venv/bin/activate

# Para usar o sistema
pip install -r requirements.txt

# Exportar flask:
Export FLASK_APP=app

# Conectar e Criar Banco de Dados
Edit app.conf app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/pdv' no arquivo __init__.py com suas configuraçoes


no terminal execute:
flask db init
flask db migrate
flask db upgrade
e pode ligar o aplicativo usando o comando flask run

# Endpoint Post:
Modelo de post Url Esperada pela API:
Method: POST
url = /api/v1/transacao (POST)

{
   "estabelecimento": "45.283.163/0001-67",
   "cliente": "094.214.930-01",
   "valor": 590.01,
   "descricao": "Almoço em restaurante chique pago via Shipay!"
}

# Endpoint Consultar Transacoes (Listar todas as transacoes no banco):

Method: Get
url =  /api/v1/transacao (GET)


# Endpoint Consultar Transacoes pelo campo  cliente:

Method: GET
url =  /api/v1/transacao<cpf>/ (GET)

Modelo de cpf esperado com caracteres: 094.214.930-01
Modelo de cpf esperado sem caracteres: 09421493001






