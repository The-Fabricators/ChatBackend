from rest_framework.routers import DefaultRouter

from .views import ChatViewSet, ChatMessageViewSet

router = DefaultRouter()

router.register(r"chats", ChatViewSet)
router.register(r"messages", ChatMessageViewSet)