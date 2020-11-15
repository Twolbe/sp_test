from django.shortcuts import render
from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework.decorators import action
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from .serializer import RequestSerializer
from .models import Request


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Request.objects.none()

        return Request.objects.all()

    # @swagger_auto_schema(method="get", responses={"200": RequestSerializer(many=True)})
    # @action(detail=True, methods=["get"])
    # def team(self, request, pk, *args, **kwargs):
    #     task = self.get_object()

    #     if not (
    #         taskteam := task.taskteam_set.filter(
    #             status__in=[TASK_TEAM_STATUS.ACCEPT, TASK_TEAM_STATUS.SEND]
    #         ).first()
    #     ):
    #         raise MethodNotAllowed("Get team")

    #     serializer = TaskTeamForCompanySerializer(taskteam)
    #     return Response(serializer.data)
