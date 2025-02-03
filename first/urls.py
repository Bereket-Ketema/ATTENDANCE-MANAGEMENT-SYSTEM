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
path('item_list',views.item_list,name='item_list'),
path('values',views.sec,name='sec'),
]
#teacher login
#path('',views.t_login,name='t_login'),
# path('teacher_login',views.teacher_login,name='teacher_login')
#student sign_up
# path('',views.study,name='study'),
# path('student_sign',views.student_sign,name='student_sign'),
#teachers sign_up
#    path('',views.teach,name='teach'),
    # path('insert',views.insert,name='insert')
#    path('teacher',views.teacher,name='teacher'),