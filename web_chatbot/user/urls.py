from django.urls import path

app_name = 'user'

urlpatterns = [
    # 기본 view
    path('', views.index, name='index'),
]