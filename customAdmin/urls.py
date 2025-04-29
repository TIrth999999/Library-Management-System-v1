from django.urls import path
from customAdmin import view
from app import views
urlpatterns = [
    path('admin/', view.admin, name='admin'),
    path('adminIndex',view.adminIndex,name='adminIndex'),
    path('addBook/',view.addBook,name='addBook'),
    path('adminUpdate/<int:id>/',view.adminUpdate,name='adminUpdate'),
    path('adminReject/<int:id>/',view.adminReject,name='adminReject'),
    path('adminLogout/',view.adminLogout,name='adminLogout'),
]