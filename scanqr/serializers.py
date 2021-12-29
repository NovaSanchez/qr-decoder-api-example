from rest_framework import serializers




class QrDecoderSerializer(serializers.Serializer):

    img = serializers.ImageField()

