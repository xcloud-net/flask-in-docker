# coding=utf-8

import sys
import random
from flask import Flask, Blueprint, render_template, request, redirect, jsonify
from flasgger import Swagger, swag_from

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
        "description": "API for my data",
        "version": "0.0.1"
    }
}

app = Flask(__name__)
swagger = Swagger(app, config=swagger_config, template=template)


@app.route('/api/<string:language>/', methods=['GET'])
def index(language):
    """
    This is the language awesomeness API
    Call this api passing a language name and get back its features
    ---
    tags:
      - Awesomeness Language API
    parameters:
      - name: language
        in: path
        type: string
        required: true
        description: 语言名称
      - name: size
        in: query
        type: integer
        description: size of awesomeness
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
        schema:
          id: awesome
          properties:
            language:
              type: string
              description: The language name
              default: Lua
            features:
              type: array
              description: The awesomeness list
              items:
                type: string
              default: ["perfect", "simple", "lovely"]
    """

    language = language.lower().strip()
    features = [
        "awesome", "great", "dynamic",
        "simple", "powerful", "amazing",
        "perfect", "beauty", "lovely"
    ]
    size = int(request.args.get('size', 1))
    if language in ['php', 'vb', 'visualbasic', 'actionscript']:
        return "An error occurred, invalid language for awesomeness", 500
    return jsonify(
        language=language,
        features=random.sample(features, size)
    )


if __name__ == '__main__':
    app.run(debug=True, port=4001)
