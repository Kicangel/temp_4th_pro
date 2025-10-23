from django.urls import path

app_name = 'chat'

urlpatterns = [
    # 기본 view
    path('', views.index, name='index'),
]