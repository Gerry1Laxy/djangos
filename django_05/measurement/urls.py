from django.urls import path

from measurement.views import SensorView, SensorUpdateView, MeasurementCreateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', SensorView.as_view()),
    path('sensor/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view())
]
