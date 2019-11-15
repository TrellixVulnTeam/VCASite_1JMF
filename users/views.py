from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }

    first_name = request.user.first_name.capitalize()
    last_name = request.user.last_name.capitalize()
    name=['Profile - '+first_name+' '+last_name]
    return render (request, 'users/profile.html',context, {'title': name})