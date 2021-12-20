from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import LABORATORY, Supervisor, Analyst




class LaboratoryView(View):
    def get(self, request):
        return render(request, 'exercises_app/laboratory.html', {'laboratory': LABORATORY})

class FirmLaboratoryView(View):
    def get(self, request, laboratory_name):
        analyst = Analyst.objects.filter(laboratory_name=laboratory_name)
        return render(request, "exercises_app/firmlab.html", {"analysts": analysts,
                                              "laboratory_name": LABORATORY[int(laboratory)-1][1]})
class AnalystView(View):
    def get(self, request, analyst_id):
        student = Analyst.objects.get(id=analyst_id)
        subjects = Supervisor.objects.all()
        return render(request, 'exercises_app/analyst.html', {'analyst': analyst, 'subjects': subjects})



