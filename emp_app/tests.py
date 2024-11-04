from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Employee

class EmployeeAPITest(APITestCase):
    def setUp(self):
        self.employee_data = {
            'name': 'Renuka Pawar',
            'email': 'renukapawar528@gmail.com',
            'department': 'Engineering',
            'role': 'Developer'
        }
        self.employee = Employee.objects.create(**self.employee_data)

    def test_create_employee(self):
        response = self.client.post(reverse('employee-list'), self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employee(self):
        response = self.client.get(reverse('employee-detail', kwargs={'pk': self.employee.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        update_data = {'name': 'Jane Doe'}
        response = self.client.put(reverse('employee-detail', kwargs={'pk': self.employee.id}), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        response = self.client.delete(reverse('employee-detail', kwargs={'pk': self.employee.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
