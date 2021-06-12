from datetime import datetime
from django.db import models


# Create your models here.

loan_statuses = (
        (0, 'Pending'),
        (1, 'Funded'),
        (2, 'Completed'),
    )
user_types = (
        (0, 'Borrower'),
        (1, 'Investor'),
    )


class User(models.Model):
    name = models.CharField(max_length=60)
    type = models.IntegerField(choices=user_types)
    sufficient_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Loan_Request(models.Model):
    FK_user_borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_amount = models.IntegerField(default=0)
    loan_period = models.IntegerField(default=0)
    loan_status = models.IntegerField(choices=loan_statuses, default=0)


class Offer(models.Model):
    FK_user_investor = models.ForeignKey(User, on_delete=models.CASCADE)
    FK_loan_request = models.ForeignKey(Loan_Request, on_delete=models.CASCADE)
    annual_interest_rate = models.IntegerField(default=0)
    approved_offer = models.BooleanField(default=False)


class Loan_Installments(models.Model):
    FK_loan = models.ForeignKey(Loan_Request, on_delete=models.CASCADE)
    installment_date = models.DateTimeField(default=datetime.now, blank=True)
    installment_amount = models.IntegerField(default=0)
