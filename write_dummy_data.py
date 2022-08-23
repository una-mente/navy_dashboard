import pandas as pd
import numpy as np
from records.models import Piracy, IUU, DrugTrafficking, ShipToShip, StowAway, MaritimeAccidents

# Piracy.objects.all().delete()
# IUU.objects.all().delete()
# DrugTrafficking.objects.all().delete()
# ShipToShip.objects.all().delete()
# StowAway.objects.all().delete()
# MaritimeAccidents.objects.all().delete()

dummy_df = pd.read_csv('dummy_data.csv')
dummy_df['type_of_incident__piracy'] = dummy_df['type_of_incident__piracy'].replace(np.nan, '')
dummy_df['culprit_vessel_entity'] = dummy_df['culprit_vessel_entity'].replace(np.nan, '')
dummy_df['culprit_vessel_entity'] = dummy_df['culprit_vessel_entity'].apply(lambda x: '' if x == '' else str(int(x)))
all_piracy = []
all_iuu = []
all_drug_trafficking = []
all_ship_to_ship = []
all_stow_away = []
all_maritime_accidents = []
for index_row in range(len(dummy_df)):
    print(index_row + 1)
    all_piracy.append(
        Piracy(
            country_of_incidence=dummy_df['country_of_incidence'][index_row],
            sub_region=dummy_df['sub_region'][index_row],
            incidence_datetime=dummy_df['incidence_datetime'][index_row],
            incident_details=dummy_df['incident_details'][index_row],
            culprit_vessel_entity=dummy_df['culprit_vessel_entity'][index_row],
            victim_vessel_entity=dummy_df['victim_vessel_entity'][index_row],
            type_of_incident=dummy_df['type_of_incident__piracy'][index_row],
            location_lat=dummy_df['location_lat'][index_row],
            location_lon=dummy_df['location_lon'][index_row],
        )
    )
    all_iuu.append(IUU(
        country_of_incidence=dummy_df['country_of_incidence'][index_row],
        sub_region=dummy_df['sub_region'][index_row],
        incidence_datetime=dummy_df['incidence_datetime'][index_row],
        incident_details=dummy_df['incident_details'][index_row],
        culprit_vessel_entity=dummy_df['culprit_vessel_entity'][index_row],
        type_of_incident=dummy_df['type_of_incident__iuu'][index_row],
    )
    )
    all_drug_trafficking.append(
        DrugTrafficking(
            country_of_incidence=dummy_df['country_of_incidence'][index_row],
            sub_region=dummy_df['sub_region'][index_row],
            incidence_datetime=dummy_df['incidence_datetime'][index_row],
            incident_details=dummy_df['incident_details'][index_row],
            culprit_vessel_entity=dummy_df['culprit_vessel_entity'][index_row],
            type_of_drug=dummy_df['type_of_drug'][index_row],
            total_tonnage_seized=dummy_df['total_tonnage_seized'][index_row],
        )
    )
    all_ship_to_ship.append(
        ShipToShip(
            country_of_incidence=dummy_df['country_of_incidence'][index_row],
            sub_region=dummy_df['sub_region'][index_row],
            incidence_datetime=dummy_df['incidence_datetime'][index_row],
            incident_details=dummy_df['incident_details'][index_row],
            type_of_vessel=dummy_df['type_of_vessel'][index_row],
        )
    )
    all_stow_away.append(
        StowAway(
            country_of_incidence=dummy_df['country_of_incidence'][index_row],
            sub_region=dummy_df['sub_region'][index_row],
            incidence_datetime=dummy_df['incidence_datetime'][index_row],
            incident_details=dummy_df['incident_details'][index_row],
            incident_category=dummy_df['incident_category'][index_row],
            source_port=dummy_df['source_port'][index_row],
            destination_port=dummy_df['destination_port'][index_row],
            no_individuals_involved=dummy_df['no_individuals_involved'][index_row],
        )
    )
    all_maritime_accidents.append(
        MaritimeAccidents(
            country_of_incidence=dummy_df['country_of_incidence'][index_row],
            sub_region=dummy_df['sub_region'][index_row],
            incidence_datetime=dummy_df['incidence_datetime'][index_row],
            incident_details=dummy_df['incident_details'][index_row],
            accident_category=dummy_df['accident_category'][index_row],
            vessel_involved=dummy_df['vessel_involved'][index_row],
        )
    )

Piracy.objects.bulk_create(all_piracy)
IUU.objects.bulk_create(all_iuu)
DrugTrafficking.objects.bulk_create(all_drug_trafficking)
ShipToShip.objects.bulk_create(all_ship_to_ship)
StowAway.objects.bulk_create(all_stow_away)
MaritimeAccidents.objects.bulk_create(all_maritime_accidents)
