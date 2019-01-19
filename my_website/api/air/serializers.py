from rest_framework import serializers

from air import models as air_models


# AIRCRAFT
class AircraftSerializer(serializers.HyperlinkedModelSerializer):
    """Aircraft Serializer"""

    class Meta:
        model = air_models.Aircraft
        fields = [
            'name',
            'url',
        ]


# AIRLINE
class AirlineSerializer(serializers.HyperlinkedModelSerializer):
    """Airline Serializer"""

    class Meta:
        model = air_models.Airline
        fields = 'name url code country active routes'.split()
        read_only_fields = ('routes',)
        search_fields = 'name code country'.split()


# AIRPORT
class AirportSerializer(serializers.HyperlinkedModelSerializer):
    """Airport Serializer"""

    class Meta:
        model = air_models.Airport
        fields = 'name url city country code offset dst'.split()


# COUNTRY
class CountrySerializer(serializers.HyperlinkedModelSerializer):
    """Country Serializer"""

    class Meta:
        model = air_models.Country
        fields = 'name url nice_name iso iso3 code phone_code'.split()


# FLIGHT
class FlightSerializer(serializers.HyperlinkedModelSerializer):
    """Flight Serializer"""

    class Meta:
        model = air_models.Flight
        fields = 'route depart_utc arrive_utc aircraft url'.split()


# FLIGHT CLASS
class FlightClassSerializer(serializers.HyperlinkedModelSerializer):
    """FlightClass Serializer"""

    class Meta:
        model = air_models.FlightClass
        fields = 'name url flight capacity'.split()


# ROUTE
class RouteSerializer(serializers.HyperlinkedModelSerializer):
    """Route Serializer"""

    class Meta:
        model = air_models.Route
        fields = 'url airline number origin destination'.split()


# SEAT
class SeatSerializer(serializers.HyperlinkedModelSerializer):
    """Seat Serializer"""

    class Meta:
        model = air_models.Seat
        fields = 'url code flight_class aisle window'.split()


class SeatPKField(serializers.PrimaryKeyRelatedField):
    """
    This is used by the TicketPurchaseSerializer
    to filter the seats that do NOT have attached tickets.
    """

    def get_queryset(self):
        # user = self.context['request'].user
        queryset = air_models.Seat.objects.filter(ticket=None)
        return queryset


# TICKET
class TicketSerializer(serializers.HyperlinkedModelSerializer):
    """Ticket Serializer"""

    class Meta:
        model = air_models.Ticket
        fields = 'url customer seat passenger'.split()
        read_only_fields = ['customer']


class TicketPurchaseSerializer(serializers.HyperlinkedModelSerializer):
    """
    Ticket Purchase Serializer
    Uses the SeatPKField to get only the seats that do NOT have attached tickets yet.
    """

    seat = SeatPKField(many=False)

    class Meta:
        model = air_models.Ticket
        fields = 'url customer seat passenger'.split()
        read_only_fields = ['customer']
