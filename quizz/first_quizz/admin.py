from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.QuizCategory)


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level']


admin.site.register(models.QuizQuestion, QuizQuestionAdmin)
