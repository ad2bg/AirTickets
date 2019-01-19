# django-rest-action-permissions
# https://github.com/apirobot/django-rest-action-permissions
# pip install django-rest-action-permissions
# The superuser has all permissions.
# enough_perms = IsSuperUser()
# delete_perms = IsAdminUser()
# none_perms = DenyAll()
# full access => AllowAny()

from rest_framework import permissions as p

from rest_action_permissions.components import (
    ActionPermissionComponent,
    IsAuthenticated,
    IsAdminUser,
)
from rest_action_permissions.permissions import ActionPermission


# IS OWNER
class IsOwner(ActionPermissionComponent):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


# READ-ONLY OR ADMIN #
class IsReadOnlyOrAdmin(p.BasePermission):
    def has_permission(self, request, view):
        u = request.user
        is_admin = u and u.is_active and u.is_staff
        return (request.method in p.SAFE_METHODS) or is_admin


# OWNER OR ADMIN
class IsOwnerOrAdmin(p.BasePermission):
    def has_object_permission(self, request, view, obj):
        u = request.user
        is_admin = u and u.is_active and u.is_staff
        return obj.owner == request.user or is_admin


# IS OWNER OR READ ONLY
class IsOwnerOrReadOnly(p.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in p.SAFE_METHODS:
            return True
        return obj.customer == request.user


# TICKET PERMISSIONS
class TicketPermissions(ActionPermission):
    create_perms = IsAdminUser()
    list_perms = IsAdminUser()
    retrieve_perms = IsOwner() or IsAdminUser()
    write_perms = IsOwner() or IsAdminUser()
    destroy_perms = IsOwner() or IsAdminUser()
    read_perms = IsAdminUser()
    none_perms = IsAdminUser()


class TicketPurchasePermissions(ActionPermission):
    create_perms = IsAuthenticated()
    list_perms = IsAuthenticated()
    retrieve_perms = IsOwner() or IsAdminUser()
    write_perms = IsOwner() or IsAdminUser()
    destroy_perms = IsOwner() or IsAdminUser()
    read_perms = IsAuthenticated()
    none_perms = IsAuthenticated()
