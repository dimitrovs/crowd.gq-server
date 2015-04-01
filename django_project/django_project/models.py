from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, default='')
    unit_price = models.FloatField()
    verification_price = models.FloatField(default=0.0)
    verifications_requested = models.IntegerField(default=0)
    budget = models.FloatField()

    class Meta:
        ordering = ('created',)


class Attachment(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    content = models.BinaryField()

    class Meta:
        abstract = True


class JobAttachment(Attachment):
    job = models.ForeignKey(Job)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job)
    title = models.CharField(max_length=250, blank=True, default='')
    description = models.TextField()


class TaskAttachment(Attachment):
    task = models.ForeignKey(Task)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    task = models.ForeignKey(Task)
    title = models.CharField(max_length=250, blank=True, default='')
    text = models.TextField()


class AnswerAttachment(Attachment):
    answer = models.ForeignKey(Answer)


class Verification(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    successful = models.BooleanField(default=False)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True, default='')

    class Meta:
        abstract = True


class JobComment(Comment):
    job = models.ForeignKey(Job)


class VerificationComment(Comment):
    verification = models.ForeignKey(Verification)


class TaskComment(Comment):
    task = models.ForeignKey(Task)


class Balance(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.OneToOneField(User)
    available = models.FloatField()
    pending = models.FloatField()


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name='transactions_sent')
    receiver = models.ForeignKey(User, related_name='transactions_received')
    amount = models.FloatField()


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    #parent = models.ForeignKey('self', blank=True)
    jobs = models.ManyToManyField(Job)
    followers = models.ManyToManyField(User)

