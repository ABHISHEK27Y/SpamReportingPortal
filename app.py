from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager, login_required, current_user
from models import db, User, Complaint
from auth import auth
from ml_engine import ml_engine
from pdf_gen import generate_report
import os

app = Flask(__name__)
# In production, use a secure random key
app.config['SECRET_KEY'] = 'dev-secret-key-12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    history = Complaint.query.filter_by(user_id=current_user.id).order_by(Complaint.timestamp.desc()).all()
    return render_template('dashboard.html', user=current_user, history=history)

@app.route('/predict', methods=['POST'])
@login_required
def predict():
    data = request.json
    message = data.get('message')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    if not ml_engine:
        return jsonify({'error': 'ML Engine not initialized'}), 500
        
    try:
        result = ml_engine.predict(message)
        
        # Save to db
        complaint = Complaint(
            user_id=current_user.id,
            message_content=message,
            is_spam_prediction=result['prediction'],
            probabilities=f"{result['fraud_probability']:.4f},{result['legit_probability']:.4f}"
        )
        db.session.add(complaint)
        db.session.commit()
        
        # Generate PDF
        pdf_url = generate_report(current_user, complaint, result)
        
        return jsonify({
            'success': True,
            'result': result,
            'pdf_url': pdf_url,
            'complaint_id': complaint.id,
            'timestamp': complaint.timestamp.strftime('%Y-%m-%d %H:%M')
        })
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database initialized.")
    app.run(debug=True, port=5000)
