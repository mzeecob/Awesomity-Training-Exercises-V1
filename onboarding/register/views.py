from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


def index(request):
    return render(request, 'register/home.html')


def user_login(request):
    return render(request, 'register/login.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'register/register.html'

    # a blank form for new user to a website
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process from data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # save it on local variable

            # clean (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)  # change password
            user.save()

            # returns user object if the credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    messages.success(request, 'Congratulation, Account created')
                    login(request, user)
                    return redirect('http://127.0.0.1:8000/admin')

        # else is to try again
        return render(request, self.template_name, {'form': form})
