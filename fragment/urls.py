from django.urls import path, include
from fragment.views import CustomAuthToken, TaskViews
from rest_framework import routers

router = routers.SimpleRouter()
router.register('tasks',TaskViews)

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login')
]

urlpatterns += router.urls