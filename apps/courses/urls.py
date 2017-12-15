from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"), #GET
    url(r'^add$', views.add, name = "add"), #POST
    url(r'^warn/(?P<id>\d+)$', views.warn, name = "warn"), #GET
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name = "destroy"), #POST
]