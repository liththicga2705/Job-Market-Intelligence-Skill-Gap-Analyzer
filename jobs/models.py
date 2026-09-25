from django.db import models

# Create your models here.

class Job(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    experience = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    salary_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    skills = models.TextField()
    employment_type = models.CharField(max_length=100)
    posted_date = models.DateField()

    def __str__(self):
        return self.job_title