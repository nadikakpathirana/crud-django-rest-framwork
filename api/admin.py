from django.contrib import admin

from api.models import Answer, Question, AdditionalQuestionCategory, Section, SubSection

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(AdditionalQuestionCategory)
admin.site.register(Section)
admin.site.register(SubSection)

