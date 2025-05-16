from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroListRetrieveSerializer, LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroListRetrieveSerializer
        return LivroSerializer