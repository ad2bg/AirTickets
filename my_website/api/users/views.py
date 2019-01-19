from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from users.models import UserModel

from . import serializers, permissions


# LOGIN VIEWSET
class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer
    queryset = UserModel.objects.all()

    # Authentication and Permission
    authentication_classes = (TokenAuthentication,)
    permission_classes = []

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""
        return ObtainAuthToken().post(request)


# USER MODEL VIEWSET
class UserModelViewSet(viewsets.ModelViewSet):
    """CRUD on UserModels."""

    serializer_class = serializers.UserModelSerializer
    queryset = UserModel.objects.all()

    # Authentication and Permission
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AdminOrUpdateOwnProfile,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)  # 'email',  # email not included for privacy reasons
