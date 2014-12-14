from rest_framework import serializers
from base.models import ApplicationUser, Score


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = ('email', 'password')

    def save_object(self, obj, **kwargs):
        password = kwargs.pop('password')
        obj.set_password(password)
        obj.save()


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
