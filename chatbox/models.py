from django.db import models
import uuid
from django.core.validators import MinLengthValidator

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50)
    roll_no = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=12, validators=[MinLengthValidator(12)])

    def __str__ (self):
        return self.user_name

#class Conversation(models.Model):
#    conversation_id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=24, validators=[MinLengthValidator(24)])
#    first_member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_member')
#    second_member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_member')
#
#    def __str__(self):
#        return str(self.first_member + '-' + self.second_member)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
#    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    def __str__ (self):
        return self.message

