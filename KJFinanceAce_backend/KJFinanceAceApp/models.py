from django.db import models

class InvestmentInfo(models.Model):
    objects = models.Manager()
    date = models.DateField()
    name = models.CharField(max_length=255)
    total_investment_amount = models.IntegerField()
    genzai_amount = models.IntegerField()

    class Meta:
        app_label = 'KJFinanceAceApp'
