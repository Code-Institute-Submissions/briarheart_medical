from django.db import models
from django.contrib.auth.models import User

class UserModel(User):

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)