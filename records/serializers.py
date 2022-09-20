from rest_framework import serializers
from .models import Piracy, IUU, DrugTrafficking, ShipToShip, IllegalMigrations, MaritimeAccidents
from django_countries.serializers import CountryFieldMixin


class PiracySerializer(CountryFieldMixin, serializers.ModelSerializer):
    country_name = serializers.CharField(source='country_of_incidence.name')
    month = serializers.DateTimeField(source='incidence_datetime')
    year = serializers.DateTimeField(source='incidence_datetime')

    class Meta:
        model = Piracy
        fields = ('culprit_vessel_entity', 'victim_vessel_entity', 'type_of_incident',
                  'location_lat', 'location_lon', 'country_name', 'sub_region', 'incidence_datetime',
                  'incident_details', 'edit_url', 'delete_url', 'month', 'year')


class IUUSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country_name = serializers.CharField(source='country_of_incidence.name')
    month = serializers.DateTimeField(source='incidence_datetime')
    year = serializers.DateTimeField(source='incidence_datetime')

    class Meta:
        model = IUU
        fields = (
            'culprit_vessel_entity', 'type_of_incident', 'country_name', 'sub_region', 'incidence_datetime',
            'incident_details', 'edit_url', 'delete_url', 'month', 'year')


class DrugTraffickingSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country_name = serializers.CharField(source='country_of_incidence.name')
    month = serializers.DateTimeField(source='incidence_datetime')
    year = serializers.DateTimeField(source='incidence_datetime')

    class Meta:
        model = DrugTrafficking
        fields = ('culprit_vessel_entity', 'multiple_vessels_involved', 'type_of_drug', 'total_tonnage_seized',
                  'country_name', 'sub_region', 'incidence_datetime', 'incident_details', 'edit_url',
                  'delete_url', 'month', 'year')


class ShipToShipSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country_name = serializers.CharField(source='country_of_incidence.name')
    month = serializers.DateTimeField(source='incidence_datetime')
    year = serializers.DateTimeField(source='incidence_datetime')

    class Meta:
        model = ShipToShip
        fields = (
            'type_of_vessel', 'country_name', 'sub_region', 'incidence_datetime', 'incident_details',
            'edit_url', 'delete_url', 'month', 'year')


class IllegalMigrationsSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country_name = serializers.CharField(source='country_of_incidence.name')
    month = serializers.DateTimeField(source='incidence_datetime')
    year = serializers.DateTimeField(source='incidence_datetime')

    class Meta:
        model = IllegalMigrations
        fields = ('incident_category', 'source_port', 'destination_port', 'no_individuals_involved',
                  'country_name', 'sub_region', 'incidence_datetime', 'incident_details', 'edit_url',
                  'delete_url', 'month', 'year')


class MaritimeAccidentsSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country_name = serializers.CharField(source='country_of_incidence.name')
    month = serializers.DateTimeField(source='incidence_datetime')
    year = serializers.DateTimeField(source='incidence_datetime')

    class Meta:
        model = MaritimeAccidents
        fields = (
            'accident_category', 'country_name', 'sub_region', 'incidence_datetime', 'incident_details',
            'edit_url', 'delete_url', 'month', 'year')
