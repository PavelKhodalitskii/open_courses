from django.urls import path, include

from .views import (EmailLoginView,
                    CheckAuth,
                    CSRFSetter)

urlpatterns = [
    path('session_based_auths/login/', EmailLoginView.as_view(), name="email_login_view"),
    path('session_based_auths/', include('rest_framework.urls')),
    path('session_based_auths/check_auth/', CheckAuth.as_view(), name="check_auth"), 
    path('csrf/', CSRFSetter.as_view(), name="csrf_setter"),
]