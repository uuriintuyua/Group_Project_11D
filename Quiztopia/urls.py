from django.urls import path
from Quiztopia import views

app_name = 'Quiztopia'

urlpatterns = [
    path('', views.index, name = "index"),
    path('login/', views.user_login, name='login'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
    path('categories/', views.categories, name='categories'),
]
