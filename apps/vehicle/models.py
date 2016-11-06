import os

from django.db import models

# Create your models here.
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from core.models import UnitMeasurement, VehicleBrand, VehicleModel, VehicleEnrollment
from core import constants as core_constants
from core.utils.fields import BaseModel
from core.utils.upload_folder import upload_vehicle_image


class Vehicle(BaseModel):
    """ model Vehicle(vehiculo) """
    unit_transport = models.ForeignKey(
        UnitMeasurement, related_name="%(app_label)s_%(class)s_type_transport",
        limit_choices_to={'type_measurement__in': [core_constants.CODE_MEASUREMENT_TRANSPORT_UNIT]})
    brand = models.ForeignKey(VehicleBrand, related_name="%(app_label)s_%(class)s_brand")
    model = models.ForeignKey(VehicleModel, related_name="%(app_label)s_%(class)s_model")
    year_car = models.ForeignKey(VehicleEnrollment, related_name="%(app_label)s_%(class)s_year_car")
    plaque = models.CharField(max_length=200, null=True, blank=True, unique=True)
    color = models.CharField(max_length=200, null=True, blank=True)
    type_vehicle = models.CharField(
        max_length=20, null=True, blank=True,
        choices=core_constants.SELECT_DEFAULT + core_constants.TYPE_CLASS_VEHICLE_OPTIONS)

    class Meta:
        unique_together = ["unit_transport", "brand", "model", "plaque"]

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(str(self.unit_transport), str(self.brand), str(self.model), str(self.year_car))


class VehicleDetail(BaseModel):
    """ model Vehicle(vehiculo) """
    vehicle = models.OneToOneField(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    serie_motor = models.CharField(max_length=200, null=True, blank=True)
    soat = models.CharField(max_length=100, blank=True, null=True)
    expiration_soat = models.DateTimeField(blank=True, null=True)
    poliza = models.CharField(max_length=100, blank=True, null=True)
    expiration_poliza = models.DateTimeField(blank=True, null=True)
    technical_review = models.CharField(max_length=100, blank=True, null=True)
    expiration_technical_review = models.DateTimeField(blank=True, null=True)
    opacity_test = models.CharField(max_length=100, blank=True, null=True)
    expiration_opacity_test = models.DateTimeField(blank=True, null=True, )
    farenet_test = models.CharField(max_length=100, blank=True, null=True)
    expiration_farenet_test = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ["vehicle"]

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(
            str(self.vehicle.unit_transport), str(self.vehicle.brand), str(self.vehicle.model),
            str(self.vehicle.year_car))


class VehicleImage(BaseModel):
    """ model Vehicle(vehiculo) """
    vehicle = models.ForeignKey(
        Vehicle,related_name="%(app_label)s_%(class)s_vehicle",
        blank=True, null=True, on_delete=False)
    image = models.ImageField(upload_to=upload_vehicle_image, null=False, blank=False)

    def __str__(self):
        return self.vehicle.plaque


@receiver(pre_delete, sender=VehicleImage)
def vehicle_image_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
        instance.image.delete(False)