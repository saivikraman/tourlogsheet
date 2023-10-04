from django.urls import path
from . import views
# from .views import register_view


app_name = 'tourlog'  # Add this line to define the app namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('signup.html', views.signup, name='signup'),
    path('reg.html', views.reg, name='reg'),
    path('logout',views.logoutUser,name='logout'),
    path('finalreg.html', views.finalreg, name='finalreg'),
    path('updateData/<int:EmpCode>', views.updateData, name='updateData'),
    path('final/<int:EmpCode>', views.final, name='final'),
    path('detail',views.det,name='det'),
    path('first',views.first,name='first'),
    # path('refid',views.refid,name='refid'),
]



