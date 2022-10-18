from django.urls import path
from .import views


urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('order_form/',views.order_form,name='order'),
]