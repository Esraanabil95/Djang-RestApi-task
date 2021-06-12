from rest_framework import serializers
from .models import User, Loan_Request, Offer, Loan_Installments


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'type', 'sufficient_balance')


class LoanRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loan_Request
        fields = ('id', 'FK_user_borrower', 'loan_amount', 'loan_period', 'loan_status')


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'FK_user_investor', 'FK_loan_request', 'annual_interest_rate')
        read_only_fields = ('approved_offer',)


class testing(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = ('FK_user_investor', 'FK_loan_request', 'annual_interest_rate')


def get_serializer_class(self):
    if self.request.user.type == 0:
        return OfferSerializer
    return testing


class LoanInstallmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loan_Installments
        fields = ('id', 'FK_loan', 'installment_date', 'installment_amount')
