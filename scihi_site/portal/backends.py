from django.contrib.auth.models import User 
from .models import UserData 
 
class MyBackEnd(object): 
 """ 
 This is the custom backend to authenticate the user in the DB. 
 if this authentication fais then django default authentication  will get called 
 """ 
 
 def authenticate(self, userid, password=None): 
 """ 
 :param username: Username of the user 
 :param password: Password of the user 
 :return: 
 """ 
 #check is user is present in User DB. 
  existing_user = User.objects.get(username=userid) 
  if not existing_user: 
   #Checking the user UserData Custom DB. 
   user_data = UserData.objects.get(userid=userid) 
   print("...%s...." % user_data) 
   if userid == user_data.userid: 
    user =  User.objects.create_user(username=userid,password=12345) 
    user.save() 
    return user 
   else: 
    return None 
  else: 
   return existing_user 
 
 def get_user(self, user_id): 
 try: 
  return User.objects.get(username=user_id) 
 except User.DoesNotExist: 
  return None 