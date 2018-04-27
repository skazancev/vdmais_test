from rest_framework import viewsets, status
from rest_framework.response import Response

from vdmais.calculation.serializers import CalcSerializer


class CalcViewSet(viewsets.GenericViewSet):

    serializer_class = CalcSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.child.calc(serializer.data), status=status.HTTP_200_OK)
