from rest_framework import viewsets

from .models import Order
from .serializers import OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from services.box_selector import BoxSelector



class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(
        detail=True,
        methods=['get']
    )
    def recommend_box(self, request, pk=None):

        order = self.get_object()

        box = BoxSelector.recommend(order)

        if not box:
            return Response({
                "message":
                "No suitable box found"
            })

        return Response({
            "recommended_box": box.name,
            "cost": box.cost
        })
    
