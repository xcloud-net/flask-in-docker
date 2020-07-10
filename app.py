# coding=utf-8
from flask import Flask
from flasgger import Swagger
from language import language_blue
from product import product_blue
from account import account_blue
from auth import get_jwk
from middleware import test_middleware
from swagger import swagger_config, template

app = Flask(__name__,
            template_folder='./templates',
            static_folder='./static',
            static_url_path='/static')

# get jwk public keys
app.config['jwk_key'] = get_jwk()
# enable middleware
app.wsgi_app = test_middleware(app.wsgi_app)
# enable swagger
swagger = Swagger(app, config=swagger_config, template=template)

# reg components
app.register_blueprint(account_blue)
app.register_blueprint(language_blue)
app.register_blueprint(product_blue)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4001)
