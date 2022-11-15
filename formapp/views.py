from django.shortcuts import render
from .models import DiseaseData

# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    if request.method == "POST":
        PatientName = request.POST.get('PatientName')
        Gender = request.POST.get('gender')
        MobileNumber = request.POST.get('MobileNumber')
        EmailID = request.POST.get('EmailID')
        DrName = request.POST.get('DrName')
        TreatMent = request.POST.get('Treatment')
        LatestPathelogyReport = request.POST.get('Latestpathalogyreport')
        ProblemSinceMonths = request.POST.get('Problemmonth')
        Diseases = request.POST.getlist('Diseases')
        Symptoms = request.POST.getlist('Symptoms')

        print(PatientName, Gender, MobileNumber, EmailID, DrName, TreatMent, LatestPathelogyReport, ProblemSinceMonths, Diseases, Symptoms)

        data = DiseaseData(PatientName = PatientName, Gender = Gender, MobileNumber = MobileNumber, EmailID = EmailID, DrName = DrName, Treatment = TreatMent, LatestPathelogyReport = LatestPathelogyReport, ProblemSinceMonths = ProblemSinceMonths, Diseases = Diseases, Symptoms = Symptoms)
        data.save()


    return render(request, 'formhandle.html')
def contact(request):
    return render(request, 'contact.html')