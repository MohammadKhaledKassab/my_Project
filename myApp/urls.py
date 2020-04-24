from django.urls import path
from. import views
urlpatterns = [
    path('testcookie/', views.cookie_session),
    path('deletecookie/', views.cookie_delete),
    path('create/', views.create_session),
    path('access/', views.access_session),
]