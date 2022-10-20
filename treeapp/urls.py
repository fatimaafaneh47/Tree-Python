
from django.urls import path     
from . import views
urlpatterns = [
    path('',views.main_page),
    path('register',views.registration),
    path('login',views.login),
    path('logout',views.logout),
    path('dashboard',views.success),
    path('newTree',views.add_tree_page),
    path('addtree',views.add_tree),
    path('show/<int:tree_id>',views.details_page),
    path('user/account',views.account_page),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.Update_page),
    path('update/<int:id>',views.edit),

    
]