from django.db import models
from django.contrib.auth.models import User

class REST(models.Model):
    roll = models.CharField(max_length = 180)
    student_name = models.CharField(max_length = 180)
    admission_date = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task