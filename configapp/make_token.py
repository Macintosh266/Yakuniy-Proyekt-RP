from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'is_active':user.is_active,
        'is_admin':user.is_admin,
        'is_student':user.is_student,
        'is_teacher':user.is_teacher,
    }