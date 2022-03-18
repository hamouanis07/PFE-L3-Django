# from .models import CostumUser
# class CostumUserAuth(object):
#     def authunticate(self,username=None,password=None):
#         try:
#             user = CostumUser.objects.get(email=username)
#             if user.check_password(password):
#                 return user
#         except CostumUser.DoesNotExist:
#             return None
#
#     def get_user(self,user_id):
#         user = CostumUser.objects.get(pk=user_id)
#         if user.is_active:
#