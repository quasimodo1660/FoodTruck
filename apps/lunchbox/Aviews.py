from .serializers import *
from django.contrib.auth.models import User, Group
from .models import *


class LunchboxViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lunchbox.objects.all().order_by('-updated_at')
    serializer_class = LunchboxSerializer