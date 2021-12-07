from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import LABORATORY



class LaboratoryView(View):
    def get(self, request):
        return render(request, 'exercises_app/laboratory.html', {'laboratory': LABORATORY})


