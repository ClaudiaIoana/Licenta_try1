from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny

from regular_user.models import RegularUser
from regular_user.serializers import RegularUserSerializerAll, RegularUserSerializer, AuthentificationSerializer


class RegularUserListView(viewsets.ModelViewSet):
    queryset = RegularUser.objects.all()
    serializer_class = RegularUserSerializerAll


class RegularUserRegisterView(RegisterView):
    serializer_class = RegularUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AuthentificationView(LoginView):
    serializer_class = AuthentificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = AuthentificationSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.user = get_object_or_404(RegularUser, username=serializer.validated_data['username'])

        token, created = Token.objects.get_or_create(user=self.user)
        return Response({
            'key': token.key,
            'id': self.user.id,
            'username': self.user.username,
        }, status=status.HTTP_200_OK)


class RegularUserList(generics.ListAPIView):
    queryset = RegularUser.objects.all()
    serializer_class = RegularUserSerializer


# class RegularUserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = RegularUser.objects.all()
#     serializer_class = RegularUserSerializer
#     permission_classes = [IsSelfOrAdmin]
