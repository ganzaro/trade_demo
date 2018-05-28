from flask import Flask, render_template, jsonify

from config import app_config
# from app.mini_red.str_ops import StringMap

def create_app(config_name='development'):
 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    
    from app import str_api, list_api, map_api
    app.register_blueprint(str_api.str_api)
    app.register_blueprint(list_api.list_api)
    # app.register_blueprint(str_api.str_api)

    @app.route('/help', methods = ['GET'])
    def help():
        """Print available functions."""
        func_list = {}
        for rule in app.url_map.iter_rules():
            if rule.endpoint != 'static':
                func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
        return jsonify(func_list)

    return app

 