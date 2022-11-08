from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
import os

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

@login_required
def profile(req):
    if req.method == 'POST':
        prev_image=req.user.profile.image.path
        u_form = UserUpdateForm(req.POST,instance=req.user)
        p_form = ProfileUpdateForm(req.POST,
                                   req.FILES,
                                   instance=req.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            os.remove(prev_image)
            u_form.save()
            p_form.save()
            messages.success(req,f'Your accout has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=req.user)
        p_form = ProfileUpdateForm(instance=req.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(req,'users/profile.html',context)





'''
messages.debug
messages.info
messages.success
warning
error
'''