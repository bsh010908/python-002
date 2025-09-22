from django.urls import path
from . import views   # ✅ views.py 에서 가져오기

urlpatterns = [
    path("hello/", views.hello),   # ✅ 반드시 리스트 형태
]
