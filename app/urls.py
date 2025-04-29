from django.urls import path
from app import views
from customAdmin import view
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('signup/',views.signupUser,name='signup'),
    path('index',views.index,name='index'),
    path('logout',views.logoutUser,name='logout'),
    path('borrowAsk',views.borrowAsk,name='borrowAsk'),
    path('admin/', view.admin, name='admin'),
]