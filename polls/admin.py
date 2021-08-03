from django.contrib import admin

from .models import User, Quiz, Question, UserChoice, AvailableChoice


class UserChoiceTabular(admin.TabularInline):
    fields = ('answer', 'user',)
    model = UserChoice
    extra = 1


class AvailableChoiceTabular(admin.TabularInline):
    fields = ('answer',)
    model = AvailableChoice
    extra = 1


class QuestionTabular(admin.TabularInline):
    fields = ('quiz', 'title', 'choice_type',)
    model = Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ('quiz', 'title', 'choice_type',)
    model = Question
    list_display = ('title',)
    list_filter = ['title']
    search_fields = ['title']
    inlines = [UserChoiceTabular, AvailableChoiceTabular]


class QuizAdmin(admin.ModelAdmin):
    fields = ('title', 'start_date', 'end_date', 'description', 'users',)
    model = Quiz
    list_display = ('title', 'start_date', 'end_date',)
    list_filter = ['title', 'start_date', 'end_date']
    search_fields = ['title', 'start_date', 'end_date']
    inlines = [QuestionTabular]


class UserAdmin(admin.ModelAdmin):
    fields = ('id',)
    model = User


admin.site.register(User, UserAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(AvailableChoice)