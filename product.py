# coding=utf-8
from flask import request, jsonify, Blueprint
import random

product_blue = Blueprint('product', __name__, url_prefix='/api/product')


@product_blue.route('/search/<string:query>/', methods=['GET'])
def product_index(query):
    """
    搜索商品
    ---
    tags:
      - product
    """

    return jsonify(
        data=[1, 2]
    )


@product_blue.route('/delete/<int:uid>/', methods=['GET'])
def delete_product(uid):
    """
    删除商品
    ---
    tags:
      - product
    """

    return jsonify(
        data=[1, 2]
    )
