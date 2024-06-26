from django.db import models

class InvestmentInfo(models.Model):
    objects = models.Manager()
    key = models.AutoField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=255)
    totalInvestmentAmount = models.IntegerField()
    genzaiAmount = models.IntegerField()

    class Meta:
        app_label = 'KJFinanceAceApp'
