from django.shortcuts import render
from django.db.models import Q, Avg, Count
from django.db.models.functions import TruncMonth

import jobs
from .models import Job


def home(request):
    

    search = request.GET.get('search')
    location = request.GET.get('location')

    jobs = Job.objects.all()

    if search:
        jobs = jobs.filter(
            Q(job_title__icontains=search) |
            Q(company__icontains=search) |
            Q(location__icontains=search) |
            Q(skills__icontains=search)
        )

    if location:
        jobs = jobs.filter(location__iexact=location)

    average_min_salary = jobs.aggregate(Avg('salary_min'))['salary_min__avg']
    average_max_salary = jobs.aggregate(Avg('salary_max'))['salary_max__avg']
    sql_count = jobs.filter(skills__icontains='SQL').count()
    python_count = jobs.filter(skills__icontains='Python').count()
    excel_count = jobs.filter(skills__icontains='Excel').count()
    powerbi_count = jobs.filter(skills__icontains='Power BI').count()
    tableau_count = jobs.filter(skills__icontains='Tableau').count()
    pandas_count = jobs.filter(skills__icontains='Pandas').count()
    machine_learning_count = jobs.filter(skills__icontains='Machine Learning').count()
    django_count = jobs.filter(skills__icontains='Django').count()
    git_count = jobs.filter(skills__icontains='Git').count()
    
    monthly_jobs = (
    jobs
    .annotate(month=TruncMonth('posted_date'))
    .values('month')
    .annotate(total_jobs=Count('id'))
    .order_by('month')
)
    fresher_jobs = jobs.filter(experience__startswith='0').count()
    return render(
    request,
    'jobs/home.html',
    {
        'jobs': jobs,
        'job_count': jobs.count(),
        'average_min_salary': average_min_salary,
        'average_max_salary': average_max_salary,

        'sql_count': sql_count,
        'python_count': python_count,
        'excel_count': excel_count,
        'powerbi_count': powerbi_count,
        'tableau_count': tableau_count,
        'pandas_count': pandas_count,
        'machine_learning_count': machine_learning_count,
        'django_count': django_count,
        'git_count': git_count,
        'fresher_jobs': fresher_jobs,
        'monthly_jobs': monthly_jobs
    }
)
def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)

    return render(
        request,
        'jobs/job_detail.html',
        {
            'job': job
        }
    )