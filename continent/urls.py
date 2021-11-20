from django.urls import path, include

from continent import views

urlpatterns = [
    path('', views.ContinentView.as_view()),
    path('<int:continent_id>/', views.ContinentDetailView.as_view()),
    path('<int:continent_id>/countries/', include('country.urls')),
]
