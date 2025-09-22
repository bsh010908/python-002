from django.db import models

# 항구 정보
class ShippingPort(models.Model):
    country = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        db_table = "shipping"  # MongoDB 컬렉션명
        verbose_name = "항구"
        verbose_name_plural = "항구 목록"

    def __str__(self):
        return f"{self.port} ({self.country})"


# 선박 정보
class Ship(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=100, default="en route")
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        db_table = "ships"  # MongoDB 컬렉션명
        verbose_name = "선박"
        verbose_name_plural = "선박 목록"

    def __str__(self):
        return f"{self.name} - {self.status}"
