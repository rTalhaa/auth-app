from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Initialize database after app context
with app.app_context():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 400
        
    new_user = User(email=email, password=password)  # In real app, hash password!
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User created'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or user.password != data['password']:  # Never do this in production!
        return jsonify({'message': 'Invalid credentials'}), 401
        
    return jsonify({'message': 'Login successful'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)