from django.urls import path, include

from . import views
app_name="mobile_processors"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:processor_id>/', views.detail, name="detail"),
    path('load_processors', views.load_processors, name='load_processors')
]