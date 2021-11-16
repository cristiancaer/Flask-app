from flask_login import UserMixin
from app.firestore_service import *
class UserData:
    def __init__(self,user_id,password) -> None:
        self.user_id=user_id
        self.password=password

class UserModel(UserMixin):
    def __init__(self,user_data) -> None:
        """ 
        :param user_data=UserData class
        """
        super().__init__()
        self.id=user_data.user_id
        self.password=user_data.password
    @staticmethod
    def query(user_id):
        user_ref=get_user(user_id)
        user_data=UserData(user_ref.id,user_ref.to_dict()['password'])
        return UserModel(user_data)