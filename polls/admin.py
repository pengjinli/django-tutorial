from django.contrib import admin

from .models import Question, Choice


# Construct choice inline with question
class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 1


# Construct question
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # Date information is collapsed by default
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # Modify the admin change list view.
    # PS: Value below also can be constructed by tuple. by Vokey
    list_display = ['question_text', 'pub_date']
    # Add list view filter
    list_filter = ['pub_date']
    # Add search fields
    search_fields = ['question_text']


# Question register
admin.site.register(Question, QuestionAdmin)