
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .forms import *
from django.core.mail import send_mail


@login_required
def index(request):
    return render(request, 'accounts/home.html')


class LoginFormView(View):

    form_class = LoginForm
    template_name = 'accounts/login.html'

    # a blank form for new user to a website
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        next = request.GET.get('next')
        form = self.form_class(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['Email']
            user = authenticate(Email=email, password=password)
            login(request, user)
            if next:
                return redirect(next)
        # else is to try again
        return render(request, self.template_name, {'form': form})





class UserFormView(View):
    form_class = UserForm
    template_name = 'accounts/register.html'

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
            password = form.cleaned_data['password']
            email = form.cleaned_data['Email']
            user.set_password(password)
            user.save()

            # returns user object if the credentials are correct

            user = authenticate(Email=email, password=password)

            subject = 'Congratulation'
            to_email = [email]
            register_message = 'You are now one of us.'

            send_mail(
                subject=subject,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=to_email,
                message=register_message,
                fail_silently=False,
            )

            if user is not None:
                if user.is_active:
                    messages.success(request, 'Congratulation, Account created')
                    login(request, user)
                    return redirect('http://127.0.0.1:8000')

        # else is to try again
        return render(request, self.template_name, {'form': form})