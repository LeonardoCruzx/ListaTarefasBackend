from user.models import User
from user.serializers import UserSerializer
from user.permissions import IsOwnerOrStaff, ReadOnly

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

class UserDetail(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated,IsOwnerOrStaff|ReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)