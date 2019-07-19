from django.shortcuts import render
from django.views.generic import View
from .forms import ImageForm


class UserFormView(View):
    form_class = ImageForm
    template_name = 'upload/home.html'

    # a blank form for new user to a website
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process from data
    def post(self, request):
        form = self.form_class(request.POST,)

        if form.is_valid():
            form.save()
        # else is to try again
        return render(request, self.template_name, {'form': form})
