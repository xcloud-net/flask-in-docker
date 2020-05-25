# coding=utf-8
from flask import request, jsonify, Blueprint
import random
from flasgger import swag_from

language_blue = Blueprint('language', __name__, url_prefix='/api/language')


@swag_from('language_def.yml')
@language_blue.route('/get/<string:language>/', methods=['GET'])
def get_language(language):
    """
    This is the language awesomeness API
    Call this api passing a language name and get back its features
    ---
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
