# coding=utf-8
from flask import Flask, Blueprint, render_template, request, redirect, jsonify
from flasgger import Swagger, swag_from
from language import language_blue
from product import product_blue

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'xx',
            "route": '/api/flask_test/swagger/swagger.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/swagger/"
}
template = {
    "swagger": "2.0",
    "info": {
        "title": "商品微服务",
        "description": "商品微服务---",
        "version": "0.0.1"
    }
}

app = Flask(__name__)
swagger = Swagger(app, config=swagger_config, template=template)

app.register_blueprint(language_blue)
app.register_blueprint(product_blue)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4001)
