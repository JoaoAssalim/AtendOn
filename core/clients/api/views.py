from core.clients.models import *
from core.clients.api.serializer import *

from rest_framework import status, viewsets
from rest_framework.response import Response

from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException
from decouple import config


class ClientAPIView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    filter_fields = [f.name for f in User._meta.get_fields()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        client = Client(**serializer.validated_data)
        client.save()

        # try:
        #     send_mail(
        #         subject="Subject here",
        #         message="Here is the message.",
        #         from_email=config('EMAIL_HOST_USER'),
        #         recipient_list=[serializer.validated_data['email']],
        #         fail_silently=False,
        #     )
        #     client.save()
        # except (BadHeaderError, SMTPException) as e:
        #     print(f"Email sending failed: {e}")
        #     return Response({"detail": "Email sending failed."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)