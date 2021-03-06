from django.conf.urls import url
# from . import views
from boycotted.views import *

urlpatterns = [
    url(r'^boycott/add/', AddBoycott, name='AddBoycott'),
    url(r'^boycott/edit/(?P<boycott_id>[0-9]+)', EditBoycott, name='EditBoycott'),
    url(r'^boycotted/edit/(?P<boycotted_id>[0-9]+)', EditBoycotted, name='EditBoycotted'),
    url(r'^boycotted/view/all/', ViewAllBoycotted),
    url(r'^boycotted/view/(?P<boycotted_id>[0-9]+)', ViewBoycotted),
    url(r'^boycotted/incrementComment/(?P<identifier>[A-z0-9-]+)', IncrementComment),
    url(r'^boycott/delete/(?P<boycott_id>[0-9]+)', DeleteBoycott),
    url(r'^boycotted/delete/(?P<boycotted_id>[0-9]+)', DeleteBoycotted)
]
