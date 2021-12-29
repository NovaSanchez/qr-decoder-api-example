from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import pyqrcode
import qrtools
from .serializers import QrDecoderSerializer



class QrDecoder(APIView):

    def post(self, request, format=None):
        serializer = QrDecoderSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            qr = qrtools.QR()
            qr.decode(serializer.validated_data['img'])
            return Response({qr.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )