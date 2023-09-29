import random
from django.test import TestCase
from .models import Student


class StudentModelUnitTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            student_number=random.randint(10000, 99999),
            first_name='Shivam',
            last_name='Verma',
            email='shivam.verma@test.com',
            field_of_study='Computer Science',
            gpa=9.2
        )

    def test_student_model(self):
        data = self.student
        self.assertIsInstance(data, Student)
