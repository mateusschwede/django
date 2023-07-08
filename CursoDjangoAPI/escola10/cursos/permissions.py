from rest_framework import permissions

class EhSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE': # Somente super usuário pode deletar
            if request.user.is_superuser:
                return True
            return False
        return True