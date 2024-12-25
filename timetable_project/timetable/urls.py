from django.urls import path
from . import views

urlpatterns = [
   path('', views.landing_page, name='landing'),
    path('timetable/', views.timetable_view, name='timetable'),
]
