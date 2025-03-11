from django.shortcuts import render, get_object_or_404, redirect
from .forms import VacancyForm
from .models import Category, Job, Vacancy



# Список вакансий
def vacancy_list(request):
    vacancies = Vacancy.objects.filter(status='published')  # Показываем только одобренные вакансии
    return render(request, 'vacancy_list.html', {'vacancies': vacancies})

# Просмотр конкретной вакансии
def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy})

# Добавление вакансии
def vacancy_create(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.status = 'moderation'
            vacancy.save()
            return redirect('home_page')
    else:
        form = VacancyForm()
    return render(request, 'vacancy_form.html', {'form': form})

# Редактирование вакансии
def vacancy_update(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == "POST":
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy_detail', pk=vacancy.pk)
    else:
        form = VacancyForm(instance=vacancy)
    return render(request, 'vacancy_form.html', {'form': form})

# Удаление вакансии
def vacancy_delete(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == "POST":
        vacancy.delete()
        return redirect('vacancy_list')
    return render(request, 'vacancy_confirm_delete.html', {'vacancy': vacancy})

# Список работ
def job_list(request):
    query = request.GET.get('q')  # Получаем запрос из формы
    salaries = Job.objects.values_list('salary', flat=True).distinct().order_by('salary')
    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(title__icontains=query)  # Фильтр по названию вакансии

    return render(request, 'job_list.html', {'jobs': jobs, 'salaries': salaries})

# Детали работы
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_detail.html', {'job': job})

# Главная страница
def home_page(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()
    vacancies = Vacancy.objects.all()

    context = {
        'categories': categories,
        'jobs': jobs,
        'vacancies': vacancies
    }
    return render(request, "home.html", context)

# О нас
def about_page(request):
    return render(request, "about.html")

# Контакты
def contact_page(request):
    return render(request, "contact.html")

from django.shortcuts import render
from .models import Vacancy

def home_page(request):
    vacancies = Vacancy.objects.filter(status='published')  # Только опубликованные вакансии

    # Фильтрация по зарплате
    selected_salary = request.GET.get('salary')
    if selected_salary:
        vacancies = vacancies.filter(salary=selected_salary)

    # Фильтрация по опыту
    selected_experience = request.GET.get('experience')
    if selected_experience:
        vacancies = vacancies.filter(experience=selected_experience)

    # Получаем уникальные значения зарплат и опыта для фильтров
    salaries = Vacancy.objects.values_list('salary', flat=True).distinct().order_by('salary')
    experiences = Vacancy.objects.values_list('experience', flat=True).distinct().order_by('experience')

    context = {
        'vacancies': vacancies,
        'salaries': salaries,
        'experiences': experiences,
        'selected_salary': selected_salary,
        'selected_experience': selected_experience,
    }
    return render(request, 'home.html', context)