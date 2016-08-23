from django.contrib import admin

# Register your models here.

from models import Question, Choice

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    #This line is for reordering the fields

    #Make subfield group
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
        ]
    inlines = [ChoiceInLine]
    #Add inline choices

admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)