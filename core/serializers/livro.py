from rest_framework.serializers import ModelSerializer

from core.models import Livro
from uploader.models import Image
from uploader.serializers import ImageSerializer


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ('id', 'titulo', 'preco')

class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1

