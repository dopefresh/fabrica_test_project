# from django.contrib import admin

# from .models import User, Quiz, Question, Choice


# admin.site.register(User)
# admin.site.register(Quiz)
# admin.site.register(Question)
# admin.site.register(Choice)



from django.contrib import admin

from .models import User, Quiz, Question, Choice


class ChoiceTabular(admin.TabularInline):
    fields = ('answer', 'user',)
    model = Choice
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
    inlines = [ChoiceTabular]


class QuizAdmin(admin.ModelAdmin):
    fields = ('title', 'start_date', 'end_date', 'description', 'users',)
    model = Quiz
    list_display = ('title',)
    list_filter = ['title']
    search_fields = ['title']
    inlines = [QuestionTabular]


class UserAdmin(admin.ModelAdmin):
    fields = ('id',)
    model = User


admin.site.register(User, UserAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)