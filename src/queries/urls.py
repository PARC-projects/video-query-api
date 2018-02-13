from django.conf.urls import url
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# router.register(r'users', query_views.UserViewSet)
# router.register(r'groups', query_views.GroupViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'datasets', SearchSetViewSet)
router.register(r'queries', QueryViewSet)
router.register(r'query-results', QueryResultViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'signatures', SignatureViewSet)

urlpatterns = [
    url(r'^matches-list/$', match_list),
]
