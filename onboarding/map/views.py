from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import View
from django.contrib import messages

class Index(View):
    form_class = coordinates
    template_name = 'map/home.html'

    # a blank form for new user to a website
    def get(self, request):
        form = self.form_class(None)
        location = Coordinates.objects.all()
        return render(request, self.template_name, {'form': form, 'location': location})

    # process from data
    def post(self, request):
        form = self.form_class(request.POST)



        if form.is_valid():
            form.save()
            messages.success(request, 'save Done')
            return redirect('http://127.0.0.1:8000/map')
        # else is to try again
        return render(request, self.template_name, {'form': form})





def distance(request):
    return render(request, 'map/distance.html')
