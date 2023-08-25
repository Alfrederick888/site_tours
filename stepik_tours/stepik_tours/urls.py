from django.contrib import admin
from django.urls import path
from tours.views import MainView, MskView
from tours.views import SpbView, NskView
from tours.views import EkbView, KazanView
from tours.views import TourView


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('msk/', MskView.as_view(), name='msk'),
    path('spb/', SpbView.as_view(), name='spb'),
    path('nsk/', NskView.as_view(), name='nsk'),
    path('ekb/', EkbView.as_view(), name='ekb'),
    path('kazan/', KazanView.as_view(), name='kazan'),
    path('tour/', TourView.as_view(), name='tour'),
]
