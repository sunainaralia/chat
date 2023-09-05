from django.db import models
class ChatModel(models.Model):
    content=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now=True)
    group=models.ForeignKey('GroupModel',on_delete=models.CASCADE)
class GroupModel(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
