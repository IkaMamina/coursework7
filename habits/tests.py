from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User
from django.shortcuts import reverse


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test@test.pro', password='123')
        self.habit = Habit.objects.create(
            user=self.user,
            place='на берегу',
            duration=20,
            periodicity=3,
            action='бег',
            pleasant_habit=True,
            reward='сладкое',
            is_public=True
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_list(self):
        """Тестирование на вывод привычек."""

        url = reverse("habits:habits")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("count"), 1)

    def test_habit_create(self):
        """Тестирование на создание привычек."""

        url = reverse('habits:habits')
        data = {
            "user": "self.user",
            "place": "на берегу",
            "duration": 25,
            "periodicity": 3,
            "action": "бег",
            "pleasant_habit": True,
            "reward": "сладкое",
            "is_public": True
        }
        response = self.client.post(
            url, data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Habit.objects.all().count(), 2
        )

    def test_habit_update(self):
        """Тестирование на обновление привычек."""

        url = reverse('habits:habit_update', args=(self.habit.pk,))
        data = {
            "action": "бег",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "бег")

    def test_habit_delete(self):
        """Тестирование на удаление привычек."""

        url = reverse('habits:habit_delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_my_habits(self):
        url = reverse("habits:my_habits")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("count"), 1)





