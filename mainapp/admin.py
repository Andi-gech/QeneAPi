from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile,Course,Enroll,Course_details,Quiz,Question,Answer,course_outlines,Completed,Quizcompleted,Grade

# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Enroll)
admin.site.register(Course_details)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(course_outlines)
admin.site.register(Completed)
admin.site.register(Quizcompleted)
admin.site.register(Grade)