from django.urls import path
from urus_sosh1.views import *
from urus_sosh1 import views
from django.contrib.auth import views as wer



urlpatterns = [

    path('',wer.LoginView.as_view(template_name = 'urus_sosh1/register/login.html'), name='login'),
    path('logaut/',wer.LogoutView.as_view(template_name = 'urus_sosh1/register/login.html'), name='logaut'),
    path("index/", index, name='index'),
    path('register/', views.regist.as_view(), name='register'),
    path('Detail/<int:pk>', views.Detail.as_view(), name='Detail'),
    path("category/<int:cet_id>", pedagog, name='pedagog'),
    path('export/<int:id>', views.expor_csv, name='expor_csv'),
    path('export_excel/<int:id>', views.export_excel, name='export_excel'),
    path('klassy', klass, name='klaas'),
    path("zagruzka/", zagruzca_failov, name='zagruzca_failov'),
    path('klassy/<int:uch_id>/uchenic', views.uchenic, name='uchenic'),
    path('detal_uch/<int:pk>', views.detal_uch.as_view(), name='detal_uch'),
    path('export_excel_uch/<int:id>', views.export_excel_uch, name='export_excel_uch'),
    path('klassy/<int:uch_id>', views.export_excel_klass, name='export_excel_klass'),
    path('download/<int:cet_id>', download_data_ped, name='download_data'),
    path('download_uch/<int:uch_id>', download_data_uch, name='download_data_uch'),
    path('Update/<int:pk>', views.Update.as_view(), name='Update'),
#адреса администрации
    path('ikt/', ikt, name='ikt'),
    path('sekretar/', sekretar, name='sekretar'),
    path('director/', director, name='director'),
    path('don',donwlood, name='don'),
#адреса документов
    path('recvizit/', recvizit, name='recvizit'),
]
