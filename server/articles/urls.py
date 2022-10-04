from django.urls import path
from articles import views

urlpatterns = [
    path("index/", views.index),
    path("dinner/", views.dinner),
    path("lotto/", views.lotto),
    path("isoddeven/<int:number>", views.isoddeven),
    path("calculator/<int:num1>/<int:num2>", views.calculator),
    path("yourname/", views.yourname),
    path("MBTI/", views.MBTI),
    path("kipsum/", views.kipsum),
    path("kipsumpage/", views.kipsumpage),
]
