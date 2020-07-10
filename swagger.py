# coding=utf-8
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
