"""videoQuery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from queries import views as query_views
from rest_framework import renderers
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views

router = routers.DefaultRouter()
# router.register(r'users', query_views.UserViewSet)
# router.register(r'groups', query_views.GroupViewSet)
router.register(r'videos', query_views.VideoViewSet)
router.register(r'datasets', query_views.DatasetViewSet)
router.register(r'queries', query_views.QueryViewSet)
router.register(r'query-results', query_views.QueryResultViewSet)
router.register(r'signatures', query_views.SignatureViewSet)

# dataset_videos = query_views.DatasetViewSet.as_view({
#     'get': 'videos'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token,  name='get_auth_token'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Video Query', public=False))
]
