from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^add$', views.add, name='add'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)