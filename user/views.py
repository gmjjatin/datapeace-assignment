from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from user.models import *
# api views
from rest_framework import generics
# from django_filters import rest_framework as filters
from .serializers import UserSerializer


class UsersView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter ,filters.OrderingFilter,)
    ordering_fields = '__all__'
    # filterset_fields = ('id','first_name','last_name','company_name','city','state','zip','email','web','age',)
    search_fields = ('id','first_name','last_name','company_name','city','state','zip','email','web','age',)
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        company_name = self.request.query_params.get('company_name', None)
        age = self.request.query_params.get('age', None)
        state = self.request.query_params.get('state', None)
        zip = self.request.query_params.get('zip', None)
        email = self.request.query_params.get('email', None)
        web = self.request.query_params.get('web', None)
        city = self.request.query_params.get('city', None)

        queryset = User.objects.all()
        if id:
            queryset =queryset.filter(id=id)
        if first_name:
            queryset =queryset.filter(first_name=first_name)
        if last_name:
            queryset =queryset.filter(last_name=last_name)
        if company_name:
            queryset =queryset.filter(company_name=company_name)
        if city:
            queryset =queryset.filter(city=city)
        if state:
            queryset =queryset.filter(state=state)
        if zip:
            queryset =queryset.filter(zip=zip)
        if email:
            queryset =queryset.filter(email=email)
        if web:
            queryset =queryset.filter(web=web)
        if age:
            queryset =queryset.filter(age=age)
        return queryset
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
