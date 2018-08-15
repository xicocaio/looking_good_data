from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.lgd import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('admin/', admin.site.urls),
    url(r'^lgds/ctr', views.CTR.as_view(), name='ctr'),
]

urlpatterns = format_suffix_patterns(urlpatterns)