from click.core import Context
from flask import redirect,url_for,render_template,session
from flask.helpers import flash
from app.models.forms import LoginForm
from . import auth
from app.firestore_service import *
from flask_login import login_user,login_required,current_user,logout_user
from app.models.users import *
from werkzeug.security import generate_password_hash,check_password_hash
@auth.route('/login/',methods=['GET','POST'])
def login():
    log=LoginForm()

    if log.validate_on_submit():
        user=log.user.data
        user_doc=get_user(user)
        if user_doc.to_dict():
            user_id=user_doc.id
            user_password=user_doc.to_dict()['password']
            print('password',user_password)
            if  check_password_hash(user_password,log.password.data):
                user_data=UserData(user_id,user_password)
                
                login_user(UserModel(user_data))
                flash('login success',category='success')
                return redirect(url_for('hello'))
            else:
                flash('wrong password!',category='warning')
        else:
            flash('User not find',category='warning')
        
    context={'log':log}
    return render_template('login.html',**context)
@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('see you later','message')
    return redirect(url_for('auth.login'))
@auth.route('/singup/',methods=['GET','POST'])
def singup():
    log=LoginForm()
    if log.validate_on_submit():
        user_id=log.user.data
        password=log.password.data
        user_doc=get_user(user_id)
        if not  user_doc.to_dict():
            password=generate_password_hash(password)
            user_data=UserData(user_id,password)
            put_user(user_data)
            login_user(UserModel(user_data))
            flash('success user creation',category='success')
            return redirect(url_for('hello'))
        else:
            flash('the user already exist. Tray with another user nick',category='warning')
    context={'log':log,}  
    return render_template('singup.html',**context)