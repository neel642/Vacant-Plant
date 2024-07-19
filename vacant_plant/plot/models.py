from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


PLOT_CHOICES = (
    ("20x30", "20x30"),
    ("30x40", "30x40"),
    ("40x60", "40x60"),
    ("50x80", "50x80"),
    ("80x100", "80x100"),
)

SAPLING_CHOICES = (
    ("oak", "oak"),
    ("coconut", "coconut"),
    ("olive", "olive"),
    ("papaya", "papaya"),
    ("neem", "neem"),
    ("maple", "maple"),
)


class PlotDetail(models.Model):
    plot_no = models.CharField(max_length=10)
    dimension = models.CharField(max_length=20, choices=PLOT_CHOICES)
    address = models.TextField()
    landmark = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sapling = models.CharField(max_length=20, choices=SAPLING_CHOICES)
    num_of_sapling = models.IntegerField(editable=False)
    
    def __str__(self):
        return str(self.user) + ' - ' + self.plot_no
    
    def save(self, *args, **kwargs):
        if self.dimension == "20x30":
            self.num_of_sapling = 4
        elif self.dimension == "30x40":
            self.num_of_sapling = 6
        elif self.dimension == "40x60":
            self.num_of_sapling = 8
        elif self.dimension == "50x80":
            self.num_of_sapling = 10
        else:
            self.num_of_sapling = 12
        return super().save(*args, **kwargs)
