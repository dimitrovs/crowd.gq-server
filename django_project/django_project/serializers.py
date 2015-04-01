from django.contrib.auth.models import User
from rest_framework import serializers
import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'job', 'title', 'description')


class TaskAttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TaskAttachment
        fields = ('id', 'created', 'title', 'content', 'task')


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Job
        fields = ('id', 'created', 'due', 'owner', 'title', 'description', 'unit_price', 'verification_price',
                  'verifications_requested', 'budget')


class JobAttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.JobAttachment
        fields = ('id', 'created', 'title', 'content', 'job')


class AnswerAttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AnswerAttachment
        fields = ('id', 'created', 'title', 'content', 'answer')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Answer
        fields = ('id', 'created', 'creator', 'title', 'text', 'task')


class VerificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Verification
        fields = ('id', 'created', 'creator', 'successful')


class TaskCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TaskComment
        fields = ('id', 'created', 'creator', 'title', 'text', 'task')


class VerificationCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VerificationComment
        fields = ('id', 'created', 'creator', 'title', 'text', 'verification')


class JobCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.JobComment
        fields = ('id', 'created', 'creator', 'title', 'text', 'job')


class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Balance
        fields = ('id', 'owner', 'available', 'pending')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ('id', 'created', 'sender', 'receiver')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('id', 'name', 'jobs', 'followers')