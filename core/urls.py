
from django.contrib import admin
from django.urls import path,include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls')),
    path('', include('main.urls')),
    path('api/v1/project/', include('project.urls')),

]
