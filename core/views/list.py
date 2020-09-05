from core.models import Category
from core.serializers import CategorySerializer
from core.paginators import CategoryPaginator
from core.permissions import IsOwnerOrStaff, ReadOnly

from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework.generics import ListCreateAPIView

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie



class CategoryList(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPaginator

    @method_decorator(cache_page(30))
    @method_decorator(vary_on_cookie)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)