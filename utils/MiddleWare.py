from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class LastActivityMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if request.path == '/users/current_user/':  # Check path
            user = User.objects.get(id=request.user.id)  # Get request.user
            user.last_activity = timezone.now()  # Change last activity time
            user.save()  # Saving

        return response
