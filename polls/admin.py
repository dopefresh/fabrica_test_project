from django.contrib import admin

from .models import User, Quiz, Question, Choice


admin.site.register(User)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)



# from django.contrib import admin

# from .models import User, Quiz, Question, Choice


# class ChoiceTabular(admin.TabularInline):
#     fields = ['title', 'description', 'price', 'sub_category', 'slug']
#     model = Choice
#     prepopulated_fields = {'slug': ('title',)}
#     extra = 1
#     list_display = ('title', 'price', 'sub_category')  
#     list_filter = ['sub_category', 'price', 'title']
#     search_fields = ['sub_category', 'price', 'title']


# class QuestionTabular(admin.ModelAdmin):
#     fields = ['title', 'slug']
#     model = Category
#     prepopulated_fields = {'slug': ('title',)}
#     list_display = ('title',)
#     list_filter = ['title']
#     search_fields = ['title']
#     inlines = [SubCategoryInline]


# class QuizTabular(admin.ModelAdmin):
#     fields = ['title', 'slug']
#     model = Category
#     prepopulated_fields = {'slug': ('title',)}
#     list_display = ('title',)
#     list_filter = ['title']
#     search_fields = ['title']
#     inlines = [SubCategoryInline]


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['title', 'slug']
#     model = Category
#     prepopulated_fields = {'slug': ('title',)}
#     list_display = ('title',)
#     list_filter = ['title']
#     search_fields = ['title']
#     inlines = [SubCategoryInline]


# class QuizTabular(admin.ModelAdmin):
#     fields = ['title', 'slug']
#     model = Category
#     prepopulated_fields = {'slug': ('title',)}
#     list_display = ('title',)
#     list_filter = ['title']
#     search_fields = ['title']
#     inlines = [SubCategoryInline]


# admin.site.register(User, UserAdmin)
# admin.site.register(Quiz, QuizAdmin)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)