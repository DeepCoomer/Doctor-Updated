from django.contrib import admin
from .models import DiseaseData

class DiseaseDataModel(admin.ModelAdmin):
    list_display = ['PatientName', 'Gender', 'MobileNumber', 'EmailID', 'DrName', 'Treatment', 'LatestPathelogyReport', 'ProblemSinceMonths', 'Diseases', 'Symptoms']

admin.site.register(DiseaseData, DiseaseDataModel)

# Register your models here.
