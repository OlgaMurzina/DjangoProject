from django.contrib import admin
from . import models

# Register your models here.
class QuizCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['status', 'publish', 'author']
    search_fields = ['author', 'title']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(models.QuizCategory, QuizCategoryAdmin)

class QuizTestAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['status', 'publish', 'author']
    search_fields = ['author', 'title']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(models.QuizTest, QuizTestAdmin)

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level', 'author']
    list_filter = ['status', 'publish', 'author']
    search_fields = ['author', 'question']
    raw_id_fields = ['author']
    autocomplete_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(models.QuizQuestion, QuizQuestionAdmin)
