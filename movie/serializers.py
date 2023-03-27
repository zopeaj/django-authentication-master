from rest_framework import serializers
from movie.models import Model


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        exlude = ('comment', )

