from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ListAccess
from .serializers import ListAccessSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class ListAccessViewSet(viewsets.ModelViewSet):
    queryset = ListAccess.objects.all()
    serializer_class = ListAccessSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = serializer.save()
        except ValueError as ve:
            return Response({"detail": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"detail": "Unexpected error while creating user."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": {"id": user.id, "username": user.username, "email": user.email},
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }, status=status.HTTP_201_CREATED)
        except Exception:
            return Response({"detail": "Error generating authentication tokens."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)