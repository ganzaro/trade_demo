import os
from flask import jsonify

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

# routes
@app.route('/hi')
def hello():
   return 'Hello World'




if __name__ == '__main__':
    app.run()







