from django.contrib import admin

# Register your models here.
from .models import ChatModel,GroupModel
@admin.register(ChatModel)
class chatAdmin(admin.ModelAdmin):
    list_display=['id','content','date','group']
@admin.register(GroupModel)
class groupAdmin(admin.ModelAdmin):
    list_display=['id','name']