from rest_framework import serializers
from base.models import ApplicationUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = ('email', 'password')

    def save_object(self, obj, **kwargs):
        password = kwargs.pop('password')
        obj.set_password(password)
        obj.save()