from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog_app.sitemaps import PostSitemap

sitemaps = {
    'post':PostSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog_app.urls')),
    path('sitemaps.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
