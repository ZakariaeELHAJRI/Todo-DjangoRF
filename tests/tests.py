from django.test import TestCase
from django.urls import reverse
from api.models import Task
from api.serializers import TaskSerializer

class TaskTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data for the test
        self.task = Task.objects.create(title="Test Task", completed=False)

    def test_model_fields(self):
        # Retrieve the model instance created in the setUp method
        task = Task.objects.get(title="Test Task")

        # Assert that the model fields are correct
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.completed)

    def test_model_str_method(self):
        # Retrieve the model instance created in the setUp method
        task = Task.objects.get(title="Test Task")

        # Call the __str__ method and assert the expected result
        self.assertEqual(task.__str__(), "Test Task")

    def test_api_overview_view(self):
        # Use Django's reverse function to get the URL for the view you want to test
        url = reverse('api-Overview')

        # Issue a GET request to the view URL and assert the expected response status code
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_task_list_view(self):
        # Use Django's reverse function to get the URL for the view you want to test
        url = reverse('task-list')

        # Issue a GET request to the view URL and assert the expected response status code
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_task_detail_view(self):
        # Use Django's reverse function to get the URL for the view you want to test
        url = reverse('task-detail', args=[str(self.task.id)])

        # Issue a GET request to the view URL and assert the expected response status code
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_task_create_view(self):
        # Use Django's reverse function to get the URL for the view you want to test
        url = reverse('task-create')

        # Issue a POST request to the view URL with valid data and assert the expected response status code
        data = {'title': 'New Task', 'completed': False}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_task_update_view(self):
        # Use Django's reverse function to get the URL for the view you want to test
        url = reverse('task-update', args=[str(self.task.id)])

        # Issue a POST request to the view URL with valid data and assert the expected response status code
        data = {'title': 'Updated Task', 'completed': True}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_task_delete_view(self):
        # Use Django's reverse function to get the URL for the view you want to test
        url = reverse('task-delete', args=[str(self.task.id)])

        # Issue a DELETE request to the view URL and assert the expected response status code
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
