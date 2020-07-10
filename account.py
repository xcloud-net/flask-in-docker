# coding=utf-8
from flask import request, jsonify, Blueprint
from flasgger import swag_from
from auth import login_required

account_blue = Blueprint('account', __name__, url_prefix='/api/account')


@swag_from('./account_def.yml')
@account_blue.route('/user_info/', methods=['GET'])
@login_required
def get_user_info():
    print('当前登陆用户', request.user)
    return jsonify(
        user=request.user
    )
