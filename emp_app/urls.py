from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDeleteView

# urlpatterns = [
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
# ]


from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'Employee', EmployeeViewSet)

urlpatterns = router.urls

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/employees/', EmployeeListCreateView.as_view(), name='employee_list_create'),
    path('api/employees/<int:pk>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee_detail'),
]
