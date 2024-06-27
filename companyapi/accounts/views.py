# djangho default login , logout
from django.contrib.auth import login, logout

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
# for tokens -----------------------------------
from rest_framework.authtoken.models import Token

# *******************************************************
#   http://localhost:8085/api/auth/register/
# *******************************************************
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)  # ??

    # ========= override the post() =============
    def post(self, request, *args, **kwargs):
        # setting DATA to the selected serializer
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        # get any existing token or create one
        token, created = Token.objects.get_or_create(user=user) # why this?

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    # ========= override the post() =============
    def post(self, request, *args, **kwargs):
        # setting DATA to the selected serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data

        login(request, user) # XXXXXXXXXXXXX --> Must authenticate(). login() just sets user if to the session
        # get any existing token or create one
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })

class LogoutAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            logout(request)  # XXXXXXXXXXXXX --> not req. for token based auth
            # return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

"""
Authorization: Token <your-token>
"""
