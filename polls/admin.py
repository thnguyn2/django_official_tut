from django.contrib import admin

# Register your models here.

from models import Question, Choice

class ChoiceInLine(admin.TabularInline):
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
    #Add inline Choices

    #Add display options instead of the str() method
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']
    #Add a filter for the publication date
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)