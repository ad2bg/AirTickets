from enum import Enum
import datetime

from django.db import models
# from django.urls import reverse

from my_website import settings

DT_FORMAT = "%Y-%m-%d %H:%M"  # YYYY-MM-DD HH:mm
SPR = ' | '  # separator in strings
NL = '\n'  # new line


# AIRCRAFT
class Aircraft(models.Model):
    name = models.CharField(max_length=50)

    @property
    def total_flights_count(self):
        return f'{len(self.flights.all())}'

    @property
    def past_flights_count(self):
        now = datetime.datetime.now()
        return f'{len(self.flights.filter(depart_utc__lt=now))}'

    @property
    def future_flights(self):
        """
        Return a list of the future flights objects
        """
        now = datetime.datetime.now()
        return self.flights.filter(depart_utc__gte=now)

    @property
    def future_flights_count(self):
        """
        Return the count of the future flights objects
        """
        return f'{len(self.future_flights)}'

    @property
    def future_flights_list(self):
        """
        Return a string with the future flights: code, depart_utc, origin, destination
        """
        return (SPR + NL).join([f'{f.code} {f.depart_utc.strftime(DT_FORMAT)} {f.origin.code}-{f.destination.code}'
                                for f in self.future_flights])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


# AIRLINE
class Airline(models.Model):
    name = models.CharField('Airline Name', max_length=255, unique=True)
    code = models.CharField('Airline Code', max_length=10, unique=True)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, related_name='airlines')
    active = models.BooleanField()

    @property
    def routes_objects(self):
        return self.routes.all()

    @property
    def routes_list(self):
        return SPR.join([f'{r.code} {r.origin.code}-{r.destination.code}' for r in self.routes_objects])

    @property
    def routes_details(self):
        return NL.join([f'{r.__str__()}' for r in self.routes_objects])

    def __str__(self):
        return f'({self.code}) {self.name} - {self.country}'

    class Meta:
        ordering = ('name',)


# AIRPORT
class Airport(models.Model):
    name = models.CharField(
        max_length=255)  # leaving it NOT unique, because different airports with the same name do exist
    city = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, related_name='airports')
    code = models.CharField(max_length=50, null=True)
    offset = models.FloatField('Time Zone', blank=True, null=True)
    dst = models.CharField('DST start/end', max_length=10, blank=True, null=True)

    @property
    def routes_arriving_list(self):
        return SPR.join([f'{r.code} {r.origin.code}-{r.destination.code}' for r in self.routes_arriving.all()])

    @property
    def routes_departing_list(self):
        return SPR.join([f'{r.code} {r.origin.code}-{r.destination.code}' for r in self.routes_departing.all()])

    @property
    def routes_arriving_details(self):
        return NL.join([f'{r.__str__()}' for r in self.routes_arriving.all()])

    @property
    def routes_departing_details(self):
        return NL.join([f'{r.__str__()}' for r in self.routes_departing.all()])

    def __str__(self):
        return f'({self.code}) {self.name} - {self.city}, {self.country}'

    class Meta:
        ordering = ('name',)


# COUNTRY
class Country(models.Model):
    iso = models.CharField(max_length=5, null=True)
    name = models.CharField(max_length=255, unique=True)
    nice_name = models.CharField(max_length=255, unique=True)
    iso3 = models.CharField(max_length=5, null=True)
    code = models.IntegerField(null=True)
    phone_code = models.IntegerField(null=True)

    @property
    def airlines_list(self):
        return SPR.join([f'{a.code}' for a in self.airlines.all().order_by('code')])

    @property
    def airports_list(self):
        return SPR.join([f'{a.code}' for a in self.airports.all().order_by('code')])

    @property
    def airlines_details(self):
        return NL.join([f'{a.__str__()}' for a in self.airlines.all().order_by('code')])

    @property
    def airports_details(self):
        return NL.join([f'{a.__str__()}' for a in self.airports.all().order_by('code')])

    def __str__(self):
        return f'{self.name}'  # ({self.iso}) ({self.iso3})

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ('name',)


# FLIGHT
class Flight(models.Model):
    route = models.ForeignKey('Route', on_delete=models.PROTECT, related_name='flights')
    depart_utc = models.DateTimeField('Departure Time (UTC)')
    arrive_utc = models.DateTimeField('Arrival Time (UTC)')
    aircraft = models.ForeignKey('Aircraft', on_delete=models.PROTECT, related_name='flights')

    @property
    def airline(self):
        return self.route.airline

    @property
    def code(self):
        return self.route.code

    @property
    def origin(self):
        return self.route.origin

    @property
    def destination(self):
        return self.route.destination

    @property
    def flight_class_list(self):
        x = [f'{FlightClassOption[i.name].value}: {i.capacity}' for i in list(self.flight_classes.all())]
        return ', '.join(x)

    @property
    def economy(self):
        return self.flight_classes.get(name=FlightClassOption.ECON.name).capacity or 0

    @property
    def second(self):
        return self.flight_classes.get(name=FlightClassOption.SCND.name).capacity or 0

    @property
    def business(self):
        return self.flight_classes.get(name=FlightClassOption.BSNS.name).capacity or 0

    @property
    def first(self):
        return self.flight_classes.get(name=FlightClassOption.FRST.name).capacity or 0

    @property
    def sold_economy(self):
        return len(self.flight_classes.get(name=FlightClassOption.ECON.name).seats.filter(ticket__isnull=False))

    @property
    def sold_second(self):
        return len(self.flight_classes.get(name=FlightClassOption.SCND.name).seats.filter(ticket__isnull=False))

    @property
    def sold_business(self):
        return len(self.flight_classes.get(name=FlightClassOption.BSNS.name).seats.filter(ticket__isnull=False))

    @property
    def sold_first(self):
        return len(self.flight_classes.get(name=FlightClassOption.FRST.name).seats.filter(ticket__isnull=False))

    def __str__(self):
        return f'{self.route.code} | {self.depart_utc.strftime(DT_FORMAT)} | ' \
               f'{self.origin} >>> {self.destination}'

    class Meta:
        ordering = ('route', 'depart_utc',)


# FLIGHT CLASS OPTION
class FlightClassOption(Enum):
    ECON = 'Economy'
    SCND = 'Second'
    BSNS = 'Business'
    FRST = 'First'


# FLIGHT CLASS
class FlightClass(models.Model):
    name = models.CharField(max_length=4, choices=[(i.name, i.value) for i in FlightClassOption])
    flight = models.ForeignKey('Flight', on_delete=models.PROTECT, related_name='flight_classes')
    capacity = models.PositiveIntegerField()

    @property
    def aircraft(self):
        return self.flight.aircraft.name

    @property
    def sold(self):
        return len(self.seats.filter(ticket__isnull=False)) or 0

    @property
    def vacant(self):
        return (self.capacity or 0) - self.sold

    def __str__(self):
        return f'{self.flight.__str__()} | {self.flight.aircraft} | {FlightClassOption[self.name].value}'

    class Meta:
        verbose_name_plural = 'Flight Classes'
        ordering = ('flight', '-capacity',)


# ROUTE
class Route(models.Model):
    index = models.IntegerField(primary_key=True)
    airline = models.ForeignKey('Airline', on_delete=models.PROTECT, related_name='routes')
    origin = models.ForeignKey('Airport', on_delete=models.PROTECT, related_name='routes_departing')
    destination = models.ForeignKey('Airport', on_delete=models.PROTECT, related_name='routes_arriving')
    number = models.PositiveIntegerField()

    @property
    def code(self):
        return f'{self.airline.code}{self.number:04d}'

    @property
    def total_flights_count(self):
        return f'{len(self.flights.all())}'

    @property
    def past_flights_count(self):
        now = datetime.datetime.now()
        return f'{len(self.flights.filter(depart_utc__lt=now))}'

    @property
    def future_flights(self):
        """
        Return a list of the future flights objects
        """
        now = datetime.datetime.now()
        return self.flights.filter(depart_utc__gte=now)

    @property
    def future_flights_count(self):
        """
        Return the count of the future flights objects
        """
        return f'{len(self.future_flights)}'

    @property
    def future_flights_list(self):
        """
        Return a string with the future flights: code, depart_utc, origin, destination
        """
        return (SPR + NL).join([f'{f.code} {f.depart_utc.strftime(DT_FORMAT)} {f.origin.code}-{f.destination.code}'
                                for f in self.future_flights])

    def __str__(self):
        return f'{self.code} | {self.origin} >>> {self.destination}'

    class Meta:
        ordering = ('airline__code', 'number')
        unique_together = ('airline', 'origin', 'destination')


# SEAT
class Seat(models.Model):
    code = models.CharField(max_length=10)
    flight_class = models.ForeignKey('FlightClass', on_delete=models.PROTECT, related_name='seats')
    aisle = models.BooleanField()
    window = models.BooleanField()

    @property
    def flight(self):
        return self.flight_class.flight

    def aircraft_name(self):
        return self.flight_class.flight.aircraft.name

    aircraft_name.short_description = 'Aircraft'

    def flight_class_name(self):
        return FlightClassOption[self.flight_class.name].value

    flight_class_name.short_description = 'Flight Class'

    def __str__(self):
        return f'{self.flight_class} - {self.code}'

    class Meta:
        ordering = ['flight_class__flight__aircraft__name', 'flight_class__name', 'code']
        unique_together = ['code', 'flight_class']


# TICKET
class Ticket(models.Model):
    """
    This is the only model in this app that is supposed to be created by the end user,
    using the API or some kind of front-end.
    """

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='tickets')
    seat = models.OneToOneField('Seat', on_delete=models.PROTECT)
    passenger = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.seat} - {self.customer}'

    @property
    def owner(self):
        print(f'owner: {self.customer}')
        return self.customer

    class Meta:
        ordering = ('seat', 'customer',)
