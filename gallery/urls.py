from django.conf import settings
from django.urls import path
from django.conf.urls import url
from .import views
from django.conf.urls.static import static


urlpatterns = [
  path('',views.index,name='home'),
  path('search/',views.search_images,name='search_results'),
  url(r'^category/(?P<category_id>\d+)', views.category, name='category'),
  url(r'^location/(?P<location_id>\d+)', views.location, name='location'),
  # path('location/(P<location_id>\d+)',views.location, name='location'),
  # path('category/(P<category_id>\d+)', views.category, name='category')
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
