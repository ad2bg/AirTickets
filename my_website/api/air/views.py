from django.db.models import Q
from rest_framework import generics, mixins, viewsets, filters, status
from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import action
# from rest_framework.response import Response

from . import serializers as s, permissions as p
from air import models as am


# AIRCRAFT
class AircraftViewSet(viewsets.ModelViewSet):
    """CRUD for Aircraft."""

    serializer_class = s.AircraftSerializer
    queryset = am.Aircraft.objects.all()
    # Authentication and Permissions
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (p.IsReadOnlyOrAdmin,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


# AIRLINE
class AirlinesViewSet(viewsets.ModelViewSet):
    """CRUD for Airlines."""

    serializer_class = s.AirlineSerializer
    queryset = am.Airline.objects.all()
    # Authentication and Permissions
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (p.IsReadOnlyOrAdmin,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = 'name code country'.split()  # TODO: check country


# AIRPORT
class AirportsViewSet(viewsets.ModelViewSet):
    """CRUD for Airports."""

    serializer_class = s.AirportSerializer
    queryset = am.Airport.objects.all()
    # Authentication and Permissions
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (p.IsReadOnlyOrAdmin,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = 'name city country code offset dst'.split()  # TODO: check country


# COUNTRY
class CountriesViewSet(viewsets.ModelViewSet):
    """CRUD for Countries."""

    serializer_class = s.CountrySerializer
    queryset = am.Country.objects.all()
    # Authentication and Permissions
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (p.IsReadOnlyOrAdmin,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = 'name nice_name iso iso3 code phone_code'.split()


# FLIGHT
class FlightsViewSet(viewsets.ModelViewSet):
    """CRUD for Flights."""

    serializer_class = s.FlightSerializer
    queryset = am.Flight.objects.all()
    # Authentication and Permissions
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (p.IsReadOnlyOrAdmin,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'route__airline__name',
        'route__airline__code',
        'route__origin__name',
        'route__origin__city',
        'route__origin__country__name',
        'route__origin__code',
        'route__destination__name',
        'route__destination__city',
        'route__destination__country__name',
        'route__destination__code',
        'aircraft__name',
        'depart_utc',
        'arrive_utc'
    )


# FLIGHT CLASS
class FlightClassesViewSet(viewsets.ModelViewSet):
    """CRUD for FlightClass."""

    serializer_class = s.FlightClassSerializer
    queryset = am.FlightClass.objects.all()
    # Authentication and Permissions
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (p.IsReadOnlyOrAdmin,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = 'name flight__aircraft__name capacity'.split()


# ROUTE
class RoutesViewSet(viewsets.ModelViewSet):
    """CRUD for Routes."""

    serializer_class = s.RouteSerializer
    queryset = am.Route.objects.all()
    # Authentication and Permissions
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (p.IsReadOnlyOrAdmin,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'airline__name',
        'airline__code',
        'origin__name',
        'origin__city',
        'origin__country__name',
        'origin__code',
        'destination__name',
        'destination__city',
        'destination__country__name',
        'destination__code',
        'number'
    )


# SEAT
class SeatsViewSet(viewsets.ModelViewSet):
    """CRUD for Seats."""

    serializer_class = s.SeatSerializer
    queryset = am.Seat.objects.all()
    # Authentication and Permissions
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (p.IsReadOnlyOrAdmin,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = 'code flight_class__name'.split()


# TICKET
class TicketsViewSet(viewsets.ModelViewSet):
    """CRUD for Tickets."""

    # assign current user as customer ( i.e. object owner)
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    serializer_class = s.TicketSerializer
    queryset = am.Ticket.objects.all()

    # Authentication and Permissions
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (p.TicketPermissions,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'customer__name',
        'customer__email',
        'passenger',
        'seat__flight_class__flight__route__airline__name',
        'seat__flight_class__flight__route__airline__code',
        'seat__flight_class__flight__route__origin__name',
        'seat__flight_class__flight__route__origin__city',
        'seat__flight_class__flight__route__origin__country__name',
        'seat__flight_class__flight__route__origin__code',
        'seat__flight_class__flight__route__destination__name',
        'seat__flight_class__flight__route__destination__city',
        'seat__flight_class__flight__route__destination__country__name',
        'seat__flight_class__flight__route__destination__code',
        'seat__code'
    )


class TicketsPurchaseViewSet(viewsets.ModelViewSet):
    """
    Buy (Create) Tickets.
    Lists only the seats that do NOT have attached tickets yet.
    """

    # assign current user as customer ( i.e. object owner)
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    serializer_class = s.TicketPurchaseSerializer
    queryset = am.Ticket.objects.all()

    # Authentication and Permissions
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (p.TicketPurchasePermissions,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'customer__name',
        'customer__email',
        'passenger',
        'seat__flight_class__flight__route__airline__name',
        'seat__flight_class__flight__route__airline__code',
        'seat__flight_class__flight__route__origin__name',
        'seat__flight_class__flight__route__origin__city',
        'seat__flight_class__flight__route__origin__country__name',
        'seat__flight_class__flight__route__origin__code',
        'seat__flight_class__flight__route__destination__name',
        'seat__flight_class__flight__route__destination__city',
        'seat__flight_class__flight__route__destination__country__name',
        'seat__flight_class__flight__route__destination__code',
        'seat__code'
    )
