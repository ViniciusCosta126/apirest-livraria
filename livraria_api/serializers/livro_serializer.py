from rest_framework import serializers
from ..models import Livro


class LivroSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField(many=False)
    autor = serializers.StringRelatedField(many=False)

    class Meta:
        model = Livro
        fields = "__all__"
