from django.contrib import admin

from .models import (
    Aircraft,
    Airline,
    Airport,
    Country,
    Flight,
    FlightClass,
    Route,
    Seat,
    Ticket,
)

LIST_PER_PAGE = 10
SAVE_AS = True


# AIRCRAFT
class AircraftAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'total_flights_count',
        'past_flights_count',
        'future_flights_count',
        'future_flights_list',
    ]
    search_fields = ('name',)

    fields = 'name total_flights_count past_flights_count future_flights_count future_flights_list'.split()
    readonly_fields = 'total_flights_count past_flights_count future_flights_count future_flights_list'.split()

    list_per_page = LIST_PER_PAGE
    save_as = SAVE_AS


# AIRLINE
class AirlineAdmin(admin.ModelAdmin):
    list_display = 'name code country routes_list'.split()
    list_editable = 'code country'.split()
    list_filter = ['country']
    search_fields = 'name code country__name country__iso country__iso3'.split()
    fields = 'name code country active routes_details'.split()
    readonly_fields = ('routes_details',)

    list_per_page = LIST_PER_PAGE
    save_as = SAVE_AS


# AIRPORT
class AirportAdmin(admin.ModelAdmin):
    list_display = 'code name city country offset dst routes_arriving_list routes_departing_list'.split()
    list_editable = 'name city country offset dst'.split()
    list_filter = 'country city offset'.split()
    search_fields = 'country__name country__iso country__iso3 city offset'.split()

    fields = 'name city country code offset dst routes_arriving_details routes_departing_details'.split()
    readonly_fields = 'routes_arriving_details routes_departing_details'.split()

    list_per_page = LIST_PER_PAGE
    save_as = SAVE_AS


# COUNTRY
class CountryAdmin(admin.ModelAdmin):
    list_display = 'name nice_name iso iso3 code phone_code airlines_list airports_list'.split()
    list_editable = 'nice_name iso iso3 code phone_code'.split()
    list_filter = 'name nice_name iso iso3 code phone_code'.split()
    search_fields = list_filter

    fields = 'name nice_name iso iso3 code phone_code airlines_details airports_details'.split()
    readonly_fields = 'airlines_details airports_details'.split()

    list_per_page = LIST_PER_PAGE
    save_as = SAVE_AS


# FLIGHT
class FlightAdmin(admin.ModelAdmin):
    list_display = 'route depart_utc arrive_utc aircraft ' \
                   'sold_economy sold_second sold_business sold_first ' \
                   'economy second business first'.split()
    list_editable = 'depart_utc arrive_utc aircraft'.split()
    autocomplete_fields = 'route '.split()
    list_filter = 'depart_utc arrive_utc'.split()
    search_fields = [
        'depart_utc',
        'arrive_utc',

        'route__airline__name',
        'route__airline__code',

        'route__origin__name',
        'route__origin__city',
        'route__origin__country__name',
        'route__origin__country__iso',
        'route__origin__country__iso3',
        'route__origin__code',

        'route__destination__name',
        'route__destination__city',
        'route__destination__country__name',
        'route__destination__country__iso',
        'route__destination__country__iso3',
        'route__destination__code',
    ]

    fields = 'route depart_utc arrive_utc aircraft flight_class_list'.split()
    readonly_fields = ('flight_class_list',)

    list_per_page = LIST_PER_PAGE
    save_as = SAVE_AS


# FLIGHT CLASS
class FlightClassAdmin(admin.ModelAdmin):
    list_display = 'flight aircraft name capacity sold vacant'.split()
    list_display_links=['flight']
    list_editable = 'name capacity'.split()
    list_filter = 'name flight'.split()
    search_fields = [
        'name',
        'flight__aircraft__name',
        'flight__route__number',
        'flight__route__airline__name',
        'flight__route__airline__code',
        'flight__route__origin__name',
        'flight__route__origin__code',
        'flight__route__origin__city',
        'flight__route__origin__country__name',
        'flight__route__origin__country__iso',
        'flight__route__origin__country__iso3',
        'flight__route__destination__name',
        'flight__route__destination__code',
        'flight__route__destination__city',
        'flight__route__destination__country__name',
        'flight__route__destination__country__iso',
        'flight__route__destination__country__iso3',
    ]

    fields = 'name flight aircraft capacity sold vacant'.split()
    readonly_fields = 'aircraft sold vacant'.split()

    list_per_page = LIST_PER_PAGE
    save_as = SAVE_AS


# ROUTE
class RouteAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'airline',
        'origin',
        'destination',
        'total_flights_count',
        'past_flights_count',
        'future_flights_count',
        'future_flights_list',
    ]

    list_editable = 'airline origin destination'.split()
    list_filter = 'airline origin destination'.split()
    search_fields = [
        'airline__name',
        'airline__code',

        'origin__name',
        'origin__city',
        'origin__country__name',
        'origin__country__iso',
        'origin__country__iso3',
        'origin__code',

        'destination__name',
        'destination__city',
        'destination__country__name',
        'destination__country__iso',
        'destination__country__iso3',
        'destination__code',
    ]
    exclude = ['index']

    fields = 'airline origin destination number ' \
             'total_flights_count past_flights_count future_flights_count future_flights_list'.split()
    readonly_fields = 'total_flights_count past_flights_count future_flights_count future_flights_list'.split()

    list_per_page = LIST_PER_PAGE
    save_as = SAVE_AS


# SEAT
class SeatAdmin(admin.ModelAdmin):
    search_fields = [
        'code',
        'ticket__customer__name',
        'ticket__customer__email',
        'ticket__passenger',
        'flight_class__name',
        'flight_class__flight__aircraft__name',
        'flight_class__flight__route__number',
        'flight_class__flight__route__airline__name',
        'flight_class__flight__route__airline__code',
        'flight_class__flight__route__origin__name',
        'flight_class__flight__route__origin__code',
        'flight_class__flight__route__origin__city',
        'flight_class__flight__route__destination__name',
        'flight_class__flight__route__destination__code',
        'flight_class__flight__route__destination__city',
    ]
    list_display = 'code flight aircraft_name flight_class_name aisle window'.split()
    list_editable = 'aisle window'.split()
    list_filter = 'flight_class__flight__aircraft__name flight_class__name aisle window'.split()

    list_per_page = LIST_PER_PAGE
    save_as = SAVE_AS


# TICKET
class TicketAdmin(admin.ModelAdmin):

    search_fields = [
        'customer__name',
        'customer__email',
        'passenger',
        'seat__code',
        'seat__flight_class__name',
        'seat__flight_class__flight__aircraft__name',
        'seat__flight_class__flight__route__number',
        'seat__flight_class__flight__route__airline__name',
        'seat__flight_class__flight__route__airline__code',
        'seat__flight_class__flight__route__origin__name',
        'seat__flight_class__flight__route__origin__code',
        'seat__flight_class__flight__route__origin__city',
        'seat__flight_class__flight__route__destination__name',
        'seat__flight_class__flight__route__destination__code',
        'seat__flight_class__flight__route__destination__city',
    ]

    list_per_page = LIST_PER_PAGE
    save_as = SAVE_AS


# REGISTER ALL MODELS
admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(FlightClass, FlightClassAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Ticket, TicketAdmin)
