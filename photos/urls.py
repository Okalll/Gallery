from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
     url(r'^search/', views.search_results, name='search_results'),

    # url(r'^photo/$', views.about, name='about'),
    # url(r'^(?P<topic_name>\w+)/(?P<photo_id>[0-9]+)/$', views.info, name='info')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
