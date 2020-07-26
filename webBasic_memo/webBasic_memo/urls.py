from django.contrib import admin
from django.urls import path
from memo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('memo/', views.memo, name="memo" ),
    path('memo/create', views.createMemo, name='createMemo'),
]
