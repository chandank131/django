from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]



# from django.conf.urls import url
# from ..core import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^$', views.UsersListView.as_view(), name='users_list'),
#     url(r'^generate/$', views.GenerateRandomUserView.as_view(), name='generate'),
# ]
#
