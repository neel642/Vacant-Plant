from rest_framework import serializers
from .models import PlotDetail


class PlotDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotDetail
        fields = "__all__"