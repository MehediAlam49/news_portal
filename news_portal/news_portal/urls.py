
from django.contrib import admin
from django.urls import path
from newsApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # --------------Authentication-------------------->
    path('registerPage/', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    # ---------------CRUD--------------------------->
    path('', home, name='home'),
    path('addNews/', addNews, name='addNews'),
    path('editNews/', editNews, name='editNews'),
    path('viewNews/', viewNews, name='viewNews'),
    path('deleteNews/', deleteNews, name='deleteNews'),
]
