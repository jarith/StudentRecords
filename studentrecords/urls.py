from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^(index.html)?$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^\.*/?', include('app.urls', namespace='app')),
]