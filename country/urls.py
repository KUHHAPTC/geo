from django.urls import path

from country import views

urlpatterns = [
    path('', views.CountryView.as_view()),
    path('<int:country_id>/', views.CountryDetailView.as_view()),
]