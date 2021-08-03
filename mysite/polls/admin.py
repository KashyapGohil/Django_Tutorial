from django.contrib import admin
from . models import Question,Choice 

# Register your models here.

# from . models import Question, Choice 
# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice 
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fileds = ['pub_date','question_text']
    filedsets = [
        (None,{'fileds':['question_text']}),
        ('Date information',{'fileds':['pub_date'],
        'classes':['collapse']}),
        
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
admin.site.register(Question,QuestionAdmin)

admin.site.register(Choice)
