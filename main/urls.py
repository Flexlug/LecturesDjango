from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<subject_slug>', views.subject_list, name='SubjectView'),
    path('create/', views.create, name='create'),
    path('create_subject/', views.creates, name='creates'),
    path('lectures/<int:pk>', views.NewsDetailView.as_view(), name='lectures-detail'),
    path('lectures/<int:pk>/update', views.NewsUpdateView.as_view(), name='lectures-update'),
    path('lectures/<int:pk>/delete', views.NewsDeleteView.as_view(), name='lectures-delete')

]
