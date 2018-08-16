from django.conf.urls import url
from rest_framework import routers

from .views import *
from .views.auth_token import AuthTokenView

router = routers.DefaultRouter()
# router.register(r'users', query_views.UserViewSet)
# router.register(r'groups', query_views.GroupViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'search-sets', SearchSetViewSet)
router.register(r'queries', QueryViewSet)
router.register(r'query-results', QueryResultViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'video-clips', VideoClipViewSet)
router.register(r'final-reports', FinalReportViewSet)
# router.register(r'users', UserViewSet)

urlpatterns = [
    url('api-token-auth/', AuthTokenView.as_view()),
    url(r'^matches-list/$', match_list),
    url(r'^query-state/compute-finalize', compute_finalized_state, name='compute_finalized_state'),
    url(r'^query-state/compute-new', compute_new_state, name='compute_new_state'),
    url(r'^query-state/compute-revised', compute_revised_state, name='compute_revised_state'),
    url(r'^search-sets-all', search_sets_all, name='search_sets_all')
]
