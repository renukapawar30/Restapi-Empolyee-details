from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department', 'role']
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'date_joined']

    def destroy(self, request, *args, **kwargs):
        employee = self.get_object()
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import status, generics

from rest_framework.pagination import PageNumberPagination

class EmployeePagination(PageNumberPagination):
    page_size = 10

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = EmployeePagination

    def get_queryset(self):
        queryset = Employee.objects.all()
        department = self.request.query_params.get('department')
        role = self.request.query_params.get('role')
        if department:
            queryset = queryset.filter(department=department)
        if role:
            queryset = queryset.filter(role=role)
        return queryset

class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
