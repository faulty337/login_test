from rest_framework import generics
from sign.permissions import IsAuthenticatedOrCreate
from sign.serializers import SignUpSerializer
from django.contrib.auth.models import User

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)