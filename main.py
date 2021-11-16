
from flask import app, request,session,url_for,redirect,render_template,make_response,flash
from flask_login import login_required,current_user
from app.firestore_service import del_task, get_tasks, put_task, put_user, db_update_task
from app.models.forms import DeleteForm, LoginTask, UpdateTaskForm
import unittest
from app import create_app
app=create_app()
tasks=['task {}'.format(i) for i in range(5)]
@app.cli.command()
def test():
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
@app.errorhandler(404)
def error_404(error):
    return render_template('error_404.html',error=error)
@app.route('/index/')
def index():
    ip_addr=request.remote_addr
    res=make_response(redirect(url_for('hello')))
    session['ip_addr']=ip_addr
    return res
@app.route('/hello/',methods=['GET','POST'])
@login_required
def hello():
    log=LoginTask()
    delete_form=DeleteForm()
    update_task_form=UpdateTaskForm()
    ip_addr=session.get('ip_addr')
    user_id=current_user.id
    tasks=get_tasks(user_id)
    if log.validate_on_submit():
        task=log.task.data
        put_task(user_id,task)
        return redirect(url_for('hello'))
    
    context={'ip_addr':ip_addr,'tasks':tasks,'user':user_id,'log':log,'delete_form':delete_form,'update_task_form':update_task_form}
    return render_template('hello.html',**context)
@app.route('/del_task/<task_id>',methods=['POST'])
@login_required
def delete_task(task_id):
    user_id=current_user.id
    del_task(user_id,task_id)
    return redirect(url_for('index'))

@app.route('/update_task/<task_id>/<int:done>',methods=['POST'])
@login_required
def update_task(task_id,done):
    print(done)
    user_id=current_user.id
    db_update_task(user_id,task_id,done)
    return redirect(url_for('index'))
