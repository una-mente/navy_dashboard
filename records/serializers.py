from rest_framework import serializers
from .models import Piracy, IUU, DrugTrafficking, ShipToShip, StowAway, MaritimeAccidents
from django_countries.serializers import CountryFieldMixin


class PiracySerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Piracy
        fields = ('culprit_vessel_entity', 'victim_vessel_entity', 'type_of_incident',
                  'location_lat', 'location_lon', 'country_of_incidence', 'sub_region', 'incidence_datetime',
                  'incident_details')


class IUUSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = IUU
        fields = ('culprit_vessel_entity', 'type_of_incident', 'country_of_incidence', 'sub_region', 'incidence_datetime',
                  'incident_details')


class DrugTraffickingSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = DrugTrafficking
        fields = ('culprit_vessel_entity', 'multiple_vessels_involved', 'type_of_drug', 'total_tonnage_seized',
                  'country_of_incidence', 'sub_region', 'incidence_datetime', 'incident_details')


class ShipToShipSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = ShipToShip
        fields = ('type_of_vessel', 'location_of_incident', 'country_of_incidence', 'sub_region', 'incidence_datetime',
                  'incident_details')


class StowAwaySerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = StowAway
        fields = ('incident_category', 'source_port', 'destination_port', 'no_individuals_involved',
                  'country_of_incidence', 'sub_region', 'incidence_datetime', 'incident_details')


class MaritimeAccidentsSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = MaritimeAccidents
        fields = ('accident_category', 'location_of_incident', 'country_of_incidence', 'sub_region',
                  'incidence_datetime', 'incident_details')
