from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from pandas import read_csv


def get_port_choices():
    port_df = read_csv('ports.csv')
    return tuple([(port_df['name'][row_index], port_df['name'][row_index]) for row_index in range(len(port_df))])


class AllIncidentsMixin(models.Model):
    class Meta:
        abstract = True

    sub_region_choices = (
        ('EEZ', 'EEZ'), ('Territorial waters', 'Territorial waters'), ('Ports/Anchorage', 'Ports/Anchorage'),)
    created_timestamp = models.DateTimeField(default=timezone.now, null=False, blank=False)
    country_of_incidence = CountryField(null=True, blank=True, default='GH')
    sub_region = models.CharField(max_length=100, null=True, blank=True, choices=sub_region_choices)
    incidence_datetime = models.DateTimeField(null=True, blank=True)
    incident_details = models.TextField(max_length=1000, null=True, blank=True)


class Piracy(AllIncidentsMixin):
    incident_type_choices = (('kidnap', 'kidnap'), ('armed robbery', 'armed robbery'),
                             ('vessel hijacking', 'vessel hijacking'), ('theft', 'theft'), ('boarding', 'boarding'),
                             ('suspicious approach', 'suspicious approach'), ('attempted', 'attempted'),
                             ('others', 'others'))
    culprit_vessel_entity = models.CharField(max_length=50, null=True, blank=True, help_text="Enter MMSI for vessel")
    victim_vessel_entity = models.CharField(max_length=50, null=True, blank=True, help_text="Enter MMSI for vessel")
    type_of_incident = MultiSelectField(max_length=50, null=True, blank=True, choices=incident_type_choices)
    location_lat = models.FloatField(null=True, blank=True)
    location_lon = models.FloatField(null=True, blank=True)


class IUU(AllIncidentsMixin):
    incident_type_choices = (('Use of unapproved fishing methods', 'Use of unapproved fishing methods'),
                             ('Illegal Transhipment', 'Illegal Transhipment'),
                             ('Fishing in Authorized Areas', 'Fishing in Authorized Areas'),
                             ('Others', 'Others'),)
    culprit_vessel_entity = models.CharField(max_length=50, null=True, blank=True, help_text="Enter MMSI for vessel")
    type_of_incident = models.CharField(max_length=50, null=True, blank=True, choices=incident_type_choices)


class DrugTrafficking(AllIncidentsMixin):
    drug_type_choices = (('Cannabis', 'Cannabis'), ('Cocaine', 'Cocaine'), ('Others', 'Others'),)
    culprit_vessel_entity = models.CharField(max_length=50, null=True, blank=True, help_text="Enter MMSI for vessel")
    multiple_vessels_involved = models.BooleanField(default=False)
    type_of_drug = MultiSelectField(max_length=50, null=True, blank=True, choices=drug_type_choices)
    total_tonnage_seized = models.PositiveIntegerField()


class ShipToShip(AllIncidentsMixin):
    vessel_type_choices = (('Tankers', 'Tankers'), ('Fishing', 'Fishing'), ('Others', 'Others'),)
    type_of_vessel = models.CharField(max_length=70, null=True, blank=True, choices=vessel_type_choices)


class StowAway(AllIncidentsMixin):
    incident_category_choices = (('Suspected', 'Suspected'), ('Confirmed', 'Confirmed'),)
    incident_category = models.CharField(max_length=50, null=False, blank=False, choices=incident_category_choices)
    source_port = models.CharField(max_length=150, null=True, blank=True, choices=get_port_choices())
    destination_port = models.CharField(max_length=150, null=True, blank=True, choices=get_port_choices())
    no_individuals_involved = models.PositiveSmallIntegerField(default=1)


class MaritimeAccidents(AllIncidentsMixin):
    accident_category_choices = (('Man Overboard', 'Man Overboard'), ('Aground', 'Aground'), ('Sink', 'Sink'),
                                 ('Fire', 'Fire'), ('Flood', 'Flood'), ('Medical Emergency', 'Medical Emergency'),
                                 ('Other', 'Other'),)
    accident_category = MultiSelectField(max_length=100, null=True, blank=True, choices=accident_category_choices)
    vessel_involved = models.CharField(max_length=50, null=True, blank=True, help_text="Enter MMSI for vessel")
    multiple_vessels_involved = models.BooleanField(default=False)

