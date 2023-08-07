from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import AppUserSerializer
from drf_spectacular.utils import extend_schema
from django.http import JsonResponse


User = get_user_model()


class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AppUserSerializer


class UserView(generics.RetrieveAPIView):
    serializer_class = AppUserSerializer

    @extend_schema(responses=AppUserSerializer)
    def get_object(self):
        slug = self.kwargs["slug"]
        profile = get_object_or_404(User, profile__slug=slug)
        return profile


class UserDeleteView(generics.DestroyAPIView):
    serializer_class = AppUserSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(responses=AppUserSerializer)
    def destroy(self, request, *args, **kwargs):
        slug = self.kwargs.get("slug")
        profile = get_object_or_404(User, profile__slug=slug)
        profile.delete()
        return JsonResponse({"message": "User and Profile deleted successfully."})
