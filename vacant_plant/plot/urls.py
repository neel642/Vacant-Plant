from django.urls import path
from .views import PlotDetailView


urlpatterns = [
    path('', PlotDetailView.as_view(), name='plot-create')
]
