from django.conf.urls import url
from django.contrib import admin
from ocrapp.views import ProfileView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', ProfileView.as_view(), name='index'),

]
