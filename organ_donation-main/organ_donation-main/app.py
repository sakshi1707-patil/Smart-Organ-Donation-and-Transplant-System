from flask import Flask
from flask_cors import CORS


# Import routes
from routes.users import users_bp
from routes.donor import donor_bp
from routes.recipient import recipient_bp
from routes.admin import admin_bp

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(donor_bp, url_prefix='/donors')
app.register_blueprint(recipient_bp, url_prefix='/recipients')
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def home():
    return "Organ Donation Backend is Running"

if __name__ == '__main__':
    app.run(debug=True)


