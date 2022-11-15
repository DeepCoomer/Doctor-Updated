from django.db import models

# Create your models here.

class DiseaseData(models.Model):
    PatientName = models.CharField(default='',max_length=100,null=False,blank=False)
    Gender = models.CharField(default='',max_length=100,null=False,blank=False)
    MobileNumber = models.CharField(default='',max_length=100,null=False,blank=False)
    EmailID = models.CharField(default='',max_length=100,null=False,blank=False)
    DrName = models.CharField(default='',max_length=100,null=False,blank=False)
    Treatment = models.CharField(default='',max_length=100,null=False,blank=False)
    LatestPathelogyReport = models.CharField(default='',max_length=100,null=False,blank=False)
    ProblemSinceMonths = models.CharField(default='',max_length=100,null=False,blank=False)
    Diseases = models.CharField(default='',max_length=100,null=False,blank=False)
    Symptoms = models.CharField(default='',max_length=100,null=False,blank=False)
    objects = models.Manager()
    
    def __str__(self):
        return self.PatientName