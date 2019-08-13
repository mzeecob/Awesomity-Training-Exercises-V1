from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ImageForm
from django.contrib import messages


class UserFormView(View):
    form_class = ImageForm
    template_name = 'upload/home.html'

    # a blank form for new user to a website
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process from data
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Upload Done')
            return redirect('http://127.0.0.1:8000/upload')
        # else is to try again
        return render(request, self.template_name, {'form': form})
