from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$',view=views.index),
    url(r'^result/$',view=views.showchengji),
    url(r'^loginhandle/$',view=views.loginhandle)
]
