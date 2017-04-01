from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^results/(?P<brand_factor>\d{1}\.?\d*)$', views.results, name = "results")
    ]