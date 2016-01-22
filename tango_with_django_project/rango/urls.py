from django.conf.urls import patterns, url
from rango import views
from tango_with_django_project import settings

urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^about/',views.about, name="about"),
    url(r'^add_bar/$',views.add_bar, name='add_bar'),
    url(r'^bar/(?P<bar_name_slug>[\w\-]+)/add_tapa/$',views.add_tapa, name='add_tapa'),
    url(r'^bar/(?P<bar_name_slug>[\w\-]+)/$', views.bares,name='bares'),
    url(r'^registro/$', views.register, name="registro"),
    url(r'^restringido/$', views.index, name='goto'),
    url(r'^login/$',views.user_login, name="login" ),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^bar/(?P<bar_name_slug>[\w\-]+)/tapas/(?P<tapas_name_slug>[\w\-]+)/$', views.tapas, name="tapas"),
    url(r'^bar/(?P<bar_name_slug>[\w\+]+)/tapas/(?P<tapas_name_slug>[\w\-]+)/add_votos/$', views.add_votos, name="ad_votos"),
    url(r'^datos/$', views.reclama_datos, name="reclama_datos"), 
]

if not settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
