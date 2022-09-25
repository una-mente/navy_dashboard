# from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import PiracySerializer, IUUSerializer, DrugTraffickingSerializer, ShipToShipSerializer, \
    IllegalMigrationsSerializer, MaritimeAccidentsSerializer
from .models import Piracy, IUU, DrugTrafficking, ShipToShip, IllegalMigrations, MaritimeAccidents

model_dict = {
    'piracy': {
        'model': Piracy, 'serializer': PiracySerializer
    },
    'iuu': {
        'model': IUU, 'serializer': IUUSerializer
    },
    'drug_trafficking': {
        'model': DrugTrafficking, 'serializer': DrugTraffickingSerializer
    },
    'ship_to_ship': {
        'model': ShipToShip, 'serializer': ShipToShipSerializer
    },
    'stow_away': {
        'model': IllegalMigrations, 'serializer': IllegalMigrationsSerializer
    },
    'maritime_accidents': {
        'model': MaritimeAccidents, 'serializer': MaritimeAccidentsSerializer
    },
}


@api_view(['GET'])
def my_incidents(request, model, selection_group, data_format):
    """
    <div style="font-size:1.3em">
        <strong>OPTIONS</strong><br>
        <ul>
            <li><strong>model</strong>: piracy, iuu, drug_trafficking, ship_to_ship, stow_away, maritime_accidents</li>
            <li><strong>selection_group</strong>: all, country, incidence_year, incidence_year_country, incidence_year_region, incidence_year_quarter, incidence_year_halves</li>
            <li><strong>data_format</strong>: raw, tally </li>
        </ul>
    </div>
    """
    try:
        selected_model = model_dict[model]['model']
        selected_serializer = model_dict[model]['serializer']
        all_model_objs = selected_model.objects.all()
        unique_years = [date.year for date in all_model_objs.dates('incidence_datetime', 'year')]
        unique_years.sort()
        serializer_data = {}
        if selection_group == "all":
            my_serializer = selected_serializer(all_model_objs, many=True)
            return Response(my_serializer.data) if data_format == 'raw' else Response({'all': len(my_serializer.data)})
        elif selection_group == "country":
            for country in all_model_objs.values('country_of_incidence').distinct():
                country_name = country['country_of_incidence']
                by_country = selected_serializer(
                    all_model_objs.filter(country_of_incidence=country_name),
                    many=True
                ).data
                if data_format == 'raw':
                    serializer_data[country_name] = by_country
                else:
                    serializer_data[country_name] = len(by_country)

        elif selection_group == "incidence_year":
            for year in unique_years:
                by_year = selected_serializer(all_model_objs.filter(incidence_datetime__year=year), many=True).data
                if data_format == 'raw':
                    serializer_data[year] = by_year
                else:
                    serializer_data[year] = len(by_year)
        elif selection_group == "incidence_year_quarter" or selection_group == "incidence_year_halves":
            if selection_group == "incidence_year_quarter":
                year_grouping = {'first': [1, 2, 3], 'second': [4, 5, 6], 'third': [7, 8, 9], 'fourth': [10, 11, 12]}
            elif selection_group == "incidence_year_halves":
                year_grouping = {'first': [1, 2, 3, 4, 5, 6], 'second': [7, 8, 9, 10, 11, 12]}
            else:
                raise ValueError('Unknown Selection')
            for year in unique_years:
                year_data = {}
                for year_group in year_grouping.keys():
                    by_year_group = selected_serializer(all_model_objs.filter(
                        incidence_datetime__year=year, incidence_datetime__month__in=year_grouping[year_group]),
                        many=True).data
                    if data_format == 'raw':
                        year_data[year_group] = by_year_group
                    else:
                        year_data[year_group] = len(by_year_group)
                serializer_data[year] = year_data
        elif selection_group == "incidence_year_country":
            for year in unique_years:
                location_data = {}
                for country in all_model_objs.values('country_of_incidence').distinct():
                    country_name = country['country_of_incidence']
                    by_country = selected_serializer(
                        all_model_objs.filter(incidence_datetime__year=year, country_of_incidence=country_name),
                        many=True).data
                    if data_format == 'raw':
                        location_data[country_name] = by_country
                    else:
                        location_data[country_name] = len(by_country)
                serializer_data[year] = location_data
        elif selection_group == "incidence_year_region":
            for year in unique_years:
                location_data = {}
                for sub_region in all_model_objs.values('sub_region').distinct():
                    sub_region = sub_region['sub_region']
                    by_subregion = selected_serializer(
                        all_model_objs.filter(incidence_datetime__year=year, sub_region=sub_region),
                        many=True).data
                    if data_format == 'raw':
                        location_data[sub_region] = by_subregion
                    else:
                        location_data[sub_region] = len(by_subregion)
                serializer_data[year] = location_data
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer_data)

    except Exception as e:
        print(f"\n{e}\n")
        return Response(status=status.HTTP_400_BAD_REQUEST)


def records_page(request):
    return render(request, 'records/index.html')
