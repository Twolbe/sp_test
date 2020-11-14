from rest_framework import viewsets
from .serializer import BannerSerializer
from .models import Banner


class BannerViewSet(viewsets.ModelViewSet):
    serializer_class = BannerSerializer
    
    def get_queryset(self):
        print("chlen")
        return Banner.objects.all()