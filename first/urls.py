from django.urls import path

from . import views

urlpatterns = [
path('',views.welcome,name='welcome'),
path('login',views.login,name='login'),
#teacher path
path('teachers',views.teachers,name='teachers'),
path('teach',views.teach,name='teach'),
path('t_login',views.t_login,name='t_login'),
path('teacher_login',views.teacher_login,name='teacher_login'),
path('teacher',views.teacher,name='teacher'),
#student path
path('stud',views.stud,name='stud'),
path('stud_log',views.stud_log,name='stud_log'),
path('student_login',views.student_login,name='student_login'),
path('study',views.study,name='study'),
path('student_sign',views.student_sign,name='student_sign'),
path('about',views.about,name='about'),
path('section',views.section,name='section'),
]