from rest_framework import serializers
from measurement.models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('sensor')
        return representation


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(
        source='measurement_set', read_only=True, many=True,
    )

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
