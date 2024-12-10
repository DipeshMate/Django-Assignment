from django.shortcuts import render, redirect ,HttpResponseRedirect
from .forms import UserForm
from .models import Users
from django.contrib import messages
from django.http import Http404

# Create your views here.
def notFound(request):
    return render(request,'userNotFound.html')



# function while access /hello returning a string HelloWorld
def hello(request):
    return render(request, 'hello.html')



# function for User details retrieval.
def users(request):
    us = Users.objects.all()
    return render(request,'userDetails.html',{'users':us})



# function for find user by his Id
def findUser(request, id):
 try: 
     us = Users.objects.get(pk=id)
     print('finding User',us)
     fm = UserForm(instance=us)
     return render(request,'user.html',{'user':us,'form':fm})
 except Users.DoesNotExist: 
    raise Http404("User Not Found: Sorry, the User you are looking for does not exist")
     #return HttpResponseRedirect('users/<int:id>/UserNotFound/')



# function for adding new User
def new_users(request):
    if request.method == 'POST':
        us = UserForm(request.POST)
        if us.is_valid():
          name = us.cleaned_data.get('name')
          email = us.cleaned_data.get('email')
          role = us.cleaned_data.get('role')
          reg = Users(name=name,email=email,role=role)
          reg.save()
          messages.success(request,('New User has been Successfully Added!'))
          return redirect('new_users')
    else:
        
        us = UserForm()
    return render(request, 'addUsers.html',{'form':us})
        
