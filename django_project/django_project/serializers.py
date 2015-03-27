from django.contrib.auth.models import User, Group, Job
from rest_framework import serializers
import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'created', 'due', 'owner', 'title', 'description')


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Job
        fields = ('id', 'created', 'due', 'owner', 'title', 'description', 'unit_price', 'verification_price',
                  'verifications_requested', 'budget')

