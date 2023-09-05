from django.shortcuts import render
from .models import ChatModel,GroupModel
# Create your views here.
def run(request,groupname):
    # group=GroupModel.objects.filter(name=groupname).first()
    data=[]
    # if group:
    #     data=ChatModel.objects.filter(group=group.id)
    # else:
    #     groups=GroupModel(name=groupname)
    #     groups.save()
    return render(request,'home/index.html',{'groupname':groupname,'data':data})