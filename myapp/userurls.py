from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('login_request/', views.login_request, name='login_request'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # ****user start here *****
    path('view_all_users/', views.view_all_users, name='view_all_users'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_regi/', views.user_regi, name='user_regi'),
    path('delete_user/<id>', views.delete_user, name='delete_user'),
    path('user_update/<id>', views.user_update, name='user_update'),
    # ****user end here ******

    path('select_branch/',views.select_branch,name='select_branch'),
    path('admin_home/',views.admin_home,name='admin_home'),

    # logout
    path('logout/', views.logout, name='logout'),


]