from . import app
from model import User
from flask import abort, redirect, url_for
from functools import wraps
from flask import current_app, request, jsonify
from itsdangerous import SignatureExpired, BadSignature
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from utils.error_code import *

from flask.ext.cors import CORS
CORS(app)


def gen_token(user, expiration=86400):
    print current_app.config
    s = Serializer(current_app.config.SECRET_KEY, expires_in=expiration)
    return s.dumps({'id': user.id})


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.json['token']
        s = Serializer(current_app.config.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return jsonify({'status': ERROR_CODE_TOKEN_EXPIRED})
        except BadSignature:
            return jsonify({'status': ERROR_CODE_TOKEN_INVALID})

        return func(*args, **kwargs)
    return wrapper

headers = {"Access-Control-Allow-Origin": "*",
                  "Access-Control-Allow-Headers":
                  "Origin, X-Requested-With, Content-Type, Accept, X-ID, X-TOKEN, X-ANY-YOUR-CUSTOM-HEADER",
                  "Access-Control-Allow-Methods": "POST, PUT, GET, OPTIONS, DELETE"}

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'OPTION'])
def login():
    print type(User.query.all())
    ret = User.query.all()
    for r in ret:
        print r.id, r.username, r.name
    try:
        print dir(request)
        print request.get_data()
        return 'Hello World!'
    except:
        import traceback
        print traceback.format_exc()
        return "bad"