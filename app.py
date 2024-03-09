from flask import Flask, render_template
import os
import json
from database import init_db, populate_db
from api import api_bp

def create_app():
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'nobel.db'),
    )
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Register blueprints
    app.register_blueprint(api_bp)
    
    # Main route
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

if __name__ == '__main__':
    # Initialize and populate database
    init_db()
    
    # Copy winners.json to current directory if it doesn't exist
    if not os.path.exists('winners.json'):
        with open('winners.json', 'w') as f:
            # Read data from the uploaded file and write it to the new file
            with open(__file__) as source_file:
                content = source_file.read()
                # This is a placeholder - in a real app, you would handle file copying differently
                # For this example, we assume the JSON data is already available
                pass
    
    # Populate database with data
    populate_db()
    
    # Create and run app
    app = create_app()
    app.run(debug=True)
