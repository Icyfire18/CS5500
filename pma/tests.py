from django.test import TestCase
# import pytest
from .models import Museum, Usage, Weather

class WeatherModelTestCase(TestCase):
    def test_create_weather_model(self):
        Weather.objects.create(
            date='11/02/2024',
            temperature=24.5,
            location="Portland",
            elevation=10.1,
            latitude=20,
            longitude=15.5
        )
        self.assertEqual(Weather.objects.count(), 1)

    def test_model_str_representation(self):
        weather_instance = Weather.objects.create(
            date='11/02/2024',
            temperature=24.5,
            location="Portland",
            elevation=10.1,
            latitude=20,
            longitude=15.5
        )
        self.assertEqual(weather_instance.location, 'Portland')

    def test_model_update(self):
        weather_instance = Weather.objects.create(
            date='11/02/2024',
            temperature=24.5,
            location="Portland",
            elevation=10.1,
            latitude=20,
            longitude=15.5
        )
        weather_instance.temperature = 25.0
        weather_instance.save()
        updated_instance = Weather.objects.get(pk=weather_instance.pk)
        self.assertEqual(updated_instance.temperature, 25.0)

    def test_model_deletion(self):
        weather_instance = Weather.objects.create(
            date='11/02/2024',
            temperature=24.5,
            location="Portland",
            elevation=10.1,
            latitude=20,
            longitude=15.5
        )
        weather_instance.delete()
        self.assertEqual(Weather.objects.count(), 0)
