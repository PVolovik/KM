from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline): #добавление в вопрос вариантов при создании вопроса
     model = Choice
     extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Настройка опроса', {'fields': [('question_text', 'win_vote', 'completed')]}),
        ('Даты размещения',  {'fields': [('pub_date', 'final_date')]}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'final_date', 'completed')
    list_filter = ['pub_date']

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Участник', {'fields': [('first_name', 'last_name'), ('age', 'votes'),('bio_person', 'photo_person')]}),
        ('Участие в опросе',  {'fields': ['question_id']}),
    ]
    list_display = ('__str__', 'age')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)