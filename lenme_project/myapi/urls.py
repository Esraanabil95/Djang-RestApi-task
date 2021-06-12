from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'loans', views.LoanRequestViewSet)
router.register(r'offers', views.OfferViewSet)
router.register(r'installments', views.LoanInstallmentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('loan/', views.LoanRequest.as_view()),
    path('offer/', views.test.as_view()),
]
