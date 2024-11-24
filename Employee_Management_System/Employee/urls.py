from django.urls import path
from .import views
urlpatterns = [
    path('',views.display_employee , name='display'),
    path('details/<int:pk>',views.display_employee_details,name='employee_data'),
    path('add/',views.add_employee,name='add'),
    path('update/<int:pk>',views.update_employee,name='update_data'),
    path('update/',views.update,name='update_first'),
    path('delete/<int:pk>',views.delete_employee,name='delete_data'),
    path('delete/',views.delete,name='delete_first'),
    path('register/',views.registration,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('demo/',views.demo_view,name='demo')
]  