# coding=utf-8
from flask import request, jsonify, Blueprint, render_template
import random
from log import get_logger

product_blue = Blueprint('product', __name__, url_prefix='/api/product')

logger = get_logger('product')


@product_blue.route('/search/<string:query>/', methods=['GET'])
def product_index(query):
    """
    搜索商品
    ---
    tags:
      - product
    parameters:
      - name: query
        in: path
        type: string
        description: 关键词
    """
    logger.info(msg='search products', extra={'arg': query})
    return jsonify(
        data=[1, 2]
    )


@product_blue.route('/delete/<int:uid>/', methods=['DELETE'])
def delete_product(uid):
    """
    删除商品
    ---
    tags:
      - product
    """

    logger.warn(msg='delete product', extra={'arg': uid})
    return jsonify(
        data=[1, 2]
    )


@product_blue.route('/detail/<int:uid>')
def product_detail(uid):
    """
    商品详情
    ---
    tags:
        - product
    """
    logger.info(msg='query product', extra={'arg': uid})
    data = {
        'title': 'xx'
    }
    return render_template('/product/detail.html', data=data)
