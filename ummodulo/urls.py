from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from ummodulo.models import Pessoa

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
          model = Pessoa
          fields = ['nome', 'url']

class PessoaViewset(viewsets.ModelViewSet):
     queryset = Pessoa.objects.all()
     serializer_class = PessoaSerializer
