from django.contrib.auth.models import User
from rest_framework import viewsets
import serializers
import models


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jobs to be viewed or edited.
    """
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer


class TaskAttachmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows task attachments to be viewed or edited.
    """
    queryset = models.TaskAttachment.objects.all()
    serializer_class = serializers.TaskAttachmentSerializer


class JobAttachmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows job attachments to be viewed or edited.
    """
    queryset = models.JobAttachment.objects.all()
    serializer_class = serializers.JobAttachmentSerializer


class AnswerAttachmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows answer attachments to be viewed or edited.
    """
    queryset = models.AnswerAttachment.objects.all()
    serializer_class = serializers.AnswerAttachmentSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows answers to be viewed or edited.
    """
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer


class VerificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows verifications to be viewed or edited.
    """
    queryset = models.Verification.objects.all()
    serializer_class = serializers.VerificationSerializer


class TaskCommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows task comments to be viewed or edited.
    """
    queryset = models.TaskComment.objects.all()
    serializer_class = serializers.TaskCommentSerializer


class VerificationCommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows verification comments to be viewed or edited.
    """
    queryset = models.VerificationComment.objects.all()
    serializer_class = serializers.VerificationCommentSerializer


class JobCommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows job comments to be viewed or edited.
    """
    queryset = models.JobComment.objects.all()
    serializer_class = serializers.JobCommentSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows balance to be viewed or edited.
    """
    queryset = models.Balance.objects.all()
    serializer_class = serializers.BalanceSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transactions to be viewed or edited.
    """
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tgs to be viewed or edited.
    """
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
