from django.conf.urls import url, include
from api.users.views import UserModelViewSet, LoginViewSet
from api.air.views import (
    AircraftViewSet,
    AirlinesViewSet,
    AirportsViewSet,
    CountriesViewSet,
    FlightsViewSet,
    FlightClassesViewSet,
    RoutesViewSet,
    SeatsViewSet,
    TicketsViewSet,
    TicketsPurchaseViewSet,
    # TicketCreateListSearchApiView,
    # TicketRetrieveApiView,
    # TicketUpdateApiView,
    # TicketDestroyApiView,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# users
router.register('users', UserModelViewSet)
router.register('login', LoginViewSet, base_name='login')
# air
router.register('air/aircraft', AircraftViewSet)
router.register('air/airlines', AirlinesViewSet)
router.register('air/airports', AirportsViewSet)
router.register('air/countries', CountriesViewSet)
router.register('air/flights', FlightsViewSet)
router.register('air/classes', FlightClassesViewSet)
router.register('air/routes', RoutesViewSet)
router.register('air/seats', SeatsViewSet)
router.register('air/tickets', TicketsViewSet)
router.register('air/purchase', TicketsPurchaseViewSet, 'ticket-detail')

urlpatterns = [
    # url(r'^air/tickets/$', TicketCreateListSearchApiView.as_view(), name='ticket-create-list-search'),
    # url(r'^air/tickets/(?P<pk>\d+)/$', TicketRetrieveApiView.as_view(), name='ticket-detail'),
    # url(r'^air/tickets/(?P<pk>\d+)/$', TicketUpdateApiView.as_view(), name='ticket-update'),
    # url(r'^air/tickets/(?P<pk>\d+)/$', TicketDestroyApiView.as_view(), name='ticket-destroy'),
    url(r'', include(router.urls)),
]
