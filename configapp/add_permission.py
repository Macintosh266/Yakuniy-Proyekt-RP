from rest_framework.permissions import BasePermission
from .models import *

class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_admin:
            return True
        else:
            return f"Siz admin emassiz:)"
        
class IsStudentPermission(BasePermission):
    message = "Siz student emassiz"  # default xabar

    def has_permission(self, request, view):
        if getattr(request.user, "is_student", False):
            if request.user.is_active:
                return True
            else:
                self.message = "Avval passwordni o'zgartiring!"
                return False
        return False