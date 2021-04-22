from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import InterrogationViewSet, QuestionViewSet, AnswerViewSet


router = DefaultRouter()

router.register('interrogations', InterrogationViewSet)
router.register('questions', QuestionViewSet)
router.register('answers', AnswerViewSet, basename='answers')

urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        'v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
