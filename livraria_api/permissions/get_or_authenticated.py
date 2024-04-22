from rest_framework.permissions import BasePermission


class IsGetOrAuthenticated(BasePermission):
    """
        Permite o acesso para qualquer pessoa no metodo GET,
        mas exige autentiação para outros metods (PUT,POST,DELETE,PATCH)
    """

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user and request.user.is_authenticated
