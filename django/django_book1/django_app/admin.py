from django.contrib import admin
from .models import Question, Choice


# class ChoiceInLine(admin.StackedInline):
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']  # 필드 순서 변경
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}), \
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
         # fieldset name, field corresponding to model
    ]
    inlines = [ChoiceInLine]    # Choice 모델 클라스 같이 보기
    list_display = ('question_text', 'pub_date')    # 레코드 리스트 컬럼 지정
    list_filter = ['pub_date']  # 필터 사이드바 추가
    search_fields = ['question_text']   # 검색 박스 추가    # 지정한 필드에서 search함. like로...

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)