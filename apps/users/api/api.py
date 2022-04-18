from rest_framework import generics, viewsets
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer


class GeneralUserViewSet(viewsets.ModelViewSet):
    serializer_class = None

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()


# class UserList(generics.ListCreateAPIView):
class UserViewSet(GeneralUserViewSet):
    # queryset = User.objects.all().values('username', 'email')
    # queryset = User.objects.filter(state=True)
    serializer_class = UserSerializer
    # serializer_class = UserListSerializer




# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserAPIView(APIView):
#
#     def get(self, request):
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return Response(users_serializer.data)
#
#     def post(self, request):
#         user_serializer = UserSerializer(data=request.data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response(user_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             User.objects.filter(id=pk).first()
#         except User.DoesNotExist:
#             raise Http404
#
#
#     def get(self, request, pk):
#         user = self.get_object(pk)
#         user_serializer = UserSerializer(user)
#         return Response(user_serializer.data)
#
#
#     def put(self, request, pk):
#         user = self.get_object(pk)
#         user_serializer = UserSerializer(user, data=request.data)
#         print(user_serializer)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response(user_serializer.data)
#         return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
