from rest_framework.permissions import BasePermission,SAFE_METHODS
from .models import *

class IsAdminPermission(BasePermission):
    message = "Siz admin emassiz :)"

    def has_permission(self, request, view):
        user = request.user
        if getattr(user, "is_admin", False) and user.is_active:
            return True
        return False


class IsStudentPermission(BasePermission):
    message = "Siz student emassiz."

    def has_permission(self, request, view):
        user = request.user
        if not getattr(user, "is_student", False):
            return False

        if not user.is_active:
            self.message = "Avval parolni o‘zgartiring!"
            return False

        return True


class IsTeacherPermission(BasePermission):
    message = "Siz o‘qituvchi emassiz."

    def has_permission(self, request, view):
        user = request.user
        if getattr(user, "is_teacher", False) and user.is_active:
            # Faqat GET, PATCH, PUT so‘rovlariga ruxsat
            return request.method in ['GET', 'PATCH', 'PUT']
        return False



class IsNewsPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and (request.user.is_staff or request.user.is_admin):
            return True
        return request.method in SAFE_METHODS