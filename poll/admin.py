from django.contrib import admin
from .models import Question , Choice


class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class OuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None , {'fields':['question_text']}),
                ('Date Information',{'fields':['pub_dates'],'classes':['collapse']}),]
    
    inlines = [ChoiceInline]

admin.site.register(Question , OuestionAdmin)

