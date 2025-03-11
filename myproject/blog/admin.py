from django.contrib import admin
from .models import Job, Category  # Добавляем модели

admin.site.register(Job)
admin.site.register(Category)


from django.contrib import admin
from .models import Vacancy

from django.contrib import admin
from .models import Vacancy

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'status')
    list_filter = ('status',)
    actions = ['approve_vacancies', 'reject_vacancies']

    def approve_vacancies(self, request, queryset):
        queryset.update(status='published')
    approve_vacancies.short_description = "Одобрить выбранные вакансии"

    def reject_vacancies(self, request, queryset):
        queryset.update(status='rejected')
    reject_vacancies.short_description = "Отклонить выбранные вакансии"