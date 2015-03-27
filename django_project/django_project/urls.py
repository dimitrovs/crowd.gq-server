from django.conf.urls import include, url
from rest_framework import routers
from django.contrib import admin
import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'jobs', views.JobViewSet)
router.register(r'task_attachments', views.TaskAttachmentViewSet)
router.register(r'job_attachments', views.JobAttachmentViewSet)
router.register(r'answer_attachments', views.AnswerAttachmentViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'verifications', views.VerificationViewSet)
router.register(r'task_comments', views.TaskCommentViewSet)
router.register(r'verification_comments', views.VerificationCommentViewSet)
router.register(r'job_comments', views.JobCommentViewSet)
router.register(r'balances', views.BalanceViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'tags', views.TagViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls))
]