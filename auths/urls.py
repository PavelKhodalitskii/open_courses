from django.urls import path, include

from .views import (EmailLoginView,
                    CSRFSetter)

urlpatterns = [
    path('session_based_auths/login/', EmailLoginView.as_view(), name="email_login_view"),
    path('session_based_auths/', include('rest_framework.urls')),
    path('csrf/', CSRFSetter.as_view(), name="csrf_setter"),
]