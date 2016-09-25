from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """log out user"""
    logout(request)
    return HttpResponseRedirect(reverse('cwjobs:index'))


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank form
        form = UserCreationForm()
    else:
        # Process complete form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # log the user in and redirect to home page
            authenticated_user = authenticate(username=new_user.username,
                                                          password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('cwjobs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)


