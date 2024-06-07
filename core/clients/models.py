from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=128, null=False)
    cellphone = models.CharField(max_length=128, null=False)
    email = models.CharField(max_length=128, null=True, default=None)
    birthday = models.DateField(null=False)

    history = HistoricalRecords(
        history_id_field=models.BigAutoField(
            auto_created=True, primary_key=True, editable=False
        ),
        related_name="historic",
        table_name="client_historic",
    )

    # Foreign Keys
    boss = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    class Meta:
        managed = True
        unique_together = [("email", "boss")]