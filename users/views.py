from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def register(req):
    if req.method=='POST':
        form=UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(req,f'Acount created for {username}! You can now log in')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(req,'users/register.html',{'form':form})

'''
messages.debug
messages.info
messages.success
warning
error
'''