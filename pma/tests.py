from django.test import TestCase
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


class MuseumModelTestCase(TestCase):
    def test_create_museum_model(self):
        Museum.objects.create(
            property_name='Museum1',
            property_id=1,
            street_address_1='123 Main St',
            city='Cityville',
            state='Stateville',
            postal_code=12345,
            country='Countryland',
            year_built=2000,
            type='Art',
            construction_status='Completed',
            gross_floor_area=1000,
            gfa_units='Square Feet',
            occupancy=50,
            number_of_buildings='1',
            no_of_building=1
        )
        Museum.objects.create(
            property_name='Museum2',
            property_id=1,
            street_address_1='test',
            city='TEST',
            state='test',
            postal_code=12345,
            country='Countryland',
            year_built=2000,
            type='Art',
            construction_status='Completed',
            gross_floor_area=1000,
            gfa_units='Square Feet',
            occupancy=50,
            number_of_buildings='1',
            no_of_building=4
        )
        self.assertEqual(Museum.objects.count(), 2)

    def test_model_str_representation(self):
        museum_instance = Museum.objects.create(
            property_name='Museum1',
            property_id=1,
            street_address_1='123 Main St',
            city='Cityville',
            state='Stateville',
            postal_code=12345,
            country='Countryland',
            year_built=2000,
            type='Art',
            construction_status='Completed',
            gross_floor_area=1000,
            gfa_units='Square Feet',
            occupancy=50,
            number_of_buildings='1',
            no_of_building=1
        )
        self.assertEqual(str(museum_instance), 'Museum1')

    def test_model_update(self):
        museum_instance = Museum.objects.create(
            property_name='Museum1',
            property_id=1,
            street_address_1='123 Main St',
            city='Cityville',
            state='Stateville',
            postal_code=12345,
            country='Countryland',
            year_built=2000,
            type='Art',
            construction_status='Completed',
            gross_floor_area=1000,
            gfa_units='Square Feet',
            occupancy=50,
            number_of_buildings='1',
            no_of_building=1
        )
        museum_instance.year_built = 2020
        museum_instance.save()
        updated_instance = Museum.objects.get(pk=museum_instance.pk)
        self.assertEqual(updated_instance.year_built, 2020)

    def test_model_deletion(self):
        museum_instance = Museum.objects.create(
            property_name='Museum1',
            property_id=1,
            street_address_1='123 Main St',
            city='Cityville',
            state='Stateville',
            postal_code=12345,
            country='Countryland',
            year_built=2000,
            type='Art',
            construction_status='Completed',
            gross_floor_area=1000,
            gfa_units='Square Feet',
            occupancy=50,
            number_of_buildings='1',
            no_of_building=1
        )
        museum_instance.delete()
        self.assertEqual(Museum.objects.count(), 0)


class UsageModelTestCase(TestCase):
    def test_create_usage_model(self):
        Usage.objects.create(
            u_id=1,
            property_name='Museum1',
            property_id=1,
            meter_id=1,
            meter_name='Electricity',
            meter_type='Electric',
            meter_consumption_id=1,
            start_date='2023-01-01',
            end_date='2023-01-31',
            delivery_date='2023-02-01',
            quantity=100.5,
            quantity_units='kWh',
            cost='50.00',
            estimation='Estimated',
            demand='High',
            demand_cost='10.00',
            last_modified_date='2023-02-01',
            last_modified_by='Admin',
            age=2.5,
            common_usage_units=20.0,
            date='2023-02-01',
            units='kWh',
            usage_per_sq_feet=0.05
        )
        self.assertEqual(Usage.objects.count(), 1)

    def test_model_str_representation(self):
        usage_instance = Usage.objects.create(
            u_id=1,
            property_name='Museum1',
            property_id=1,
            meter_id=1,
            meter_name='Electricity',
            meter_type='Electric',
            meter_consumption_id=1,
            start_date='2023-01-01',
            end_date='2023-01-31',
            delivery_date='2023-02-01',
            quantity=100.5,
            quantity_units='kWh',
            cost='50.00',
            estimation='Estimated',
            demand='High',
            demand_cost='10.00',
            last_modified_date='2023-02-01',
            last_modified_by='Admin',
            age=2.5,
            common_usage_units=20.0,
            date='2023-02-01',
            units='kWh',
            usage_per_sq_feet=0.05
        )
        self.assertEqual(str(usage_instance), 'Museum1 - Electricity - 2023-02-01')

    def test_model_update(self):
        usage_instance = Usage.objects.create(
            u_id=1,
            property_name='Museum1',
            property_id=1,
            meter_id=1,
            meter_name='Electricity',
            meter_type='Electric',
            meter_consumption_id=1,
            start_date='2023-01-01',
            end_date='2023-01-31',
            delivery_date='2023-02-01',
            quantity=100.5,
            quantity_units='kWh',
            cost='50.00',
            estimation='Estimated',
            demand='High',
            demand_cost='10.00',
            last_modified_date='2023-02-01',
            last_modified_by='Admin',
            age=2.5,
            common_usage_units=20.0,
            date='2023-02-01',
            units='kWh',
            usage_per_sq_feet=0.05
        )
        usage_instance.quantity = 150.0
        usage_instance.save()
        updated_instance = Usage.objects.get(pk=usage_instance.pk)
        self.assertEqual(updated_instance.quantity, 150.0)

    def test_model_deletion(self):
        usage_instance = Usage.objects.create(
            u_id=1,
            property_name='Museum1',
            property_id=1,
            meter_id=1,
            meter_name='Electricity',
            meter_type='Electric',
            meter_consumption_id=1,
            start_date='2023-01-01',
            end_date='2023-01-31',
            delivery_date='2023-02-01',
            quantity=100.5,
            quantity_units='kWh',
            cost='50.00',
            estimation='Estimated',
            demand='High',
            demand_cost='10.00',
            last_modified_date='2023-02-01',
            last_modified_by='Admin',
            age=2.5,
            common_usage_units=20.0,
            date='2023-02-01',
            units='kWh',
            usage_per_sq_feet=0.05
        )
        usage_instance.delete()
        self.assertEqual(Usage.objects.count(), 0)
