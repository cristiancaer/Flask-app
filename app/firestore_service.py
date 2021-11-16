import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection('users').document(user_id).get()

def put_user(user_data):
    new_user=db.collection('users').document(user_data.user_id)
    new_user.set({'password':user_data.password})

def get_tasks(user_id):
    return db.collection('users').document(user_id).collection('tasks').get()

def put_task(user_id,description):
    task_ref=db.collection('users').document(user_id).collection('tasks')
    task_ref.add({'description':description,'done':False})
def del_task(user_id,task_id):
    task_ref=_get_task_ref(user_id,task_id)
    task_ref.delete()
def db_update_task(user_id,task_id,done):
    done=not bool(done)
    task_ref=_get_task_ref(user_id,task_id)
    task_ref.update({'done':done})

def _get_task_ref(user_id,task_id):
    task_ref=db.document('users/{}/tasks/{}'.format(user_id,task_id))
    return task_ref