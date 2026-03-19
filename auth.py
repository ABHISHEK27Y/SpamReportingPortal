from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
from models import db, User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            return render_template('login.html', error="Email is required")
            
        name = email.split('@')[0] # Mock name based on email
        
        user = User.query.filter_by(email=email).first()
        if not user:
            # Create new user if not exists (Simulation)
            # Use ui-avatars for a generic profile pic
            user = User(email=email, name=name, profile_pic=f"https://ui-avatars.com/api/?name={name}&background=random")
            db.session.add(user)
            db.session.commit()
            
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
