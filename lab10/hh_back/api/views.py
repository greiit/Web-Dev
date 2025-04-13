from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    return JsonResponse([c.to_json() for c in companies], safe=False)

def company_detail(request, id):
    company = get_object_or_404(Company, id=id)
    return JsonResponse(company.to_json())

def vacancy_by_company(request, id):
    vacancies_by_company = Vacancy.objects.filter(company__id=id)
    return JsonResponse([v.to_json() for v in vacancies_by_company], safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return JsonResponse([v.to_json() for v in vacancies], safe=False)

def vacancy_detail(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    return JsonResponse(vacancy.to_json())

def top_ten_vacancies(request):
    sorted_vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    return JsonResponse([v.to_json() for v in sorted_vacancies], safe=False)
