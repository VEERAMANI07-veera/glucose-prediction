import os
from flask import Flask, render_template
from flask_cors import CORS

from routes.api import api_blueprint

def create_app():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, 'templates')
    static_dir = os.path.join(current_dir, 'static')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    CORS(app)
    
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'glucopredict-secret')

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
