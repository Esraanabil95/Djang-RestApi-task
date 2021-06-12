from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from .serializers import UserSerializer, LoanRequestSerializer, OfferSerializer, LoanInstallmentsSerializer, testing
from .models import User, Loan_Request, Offer, Loan_Installments
from rest_framework.permissions import AllowAny
from rest_framework import status


class LoanRequest(ListCreateAPIView):
    queryset = Loan_Request.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "Status": True,
            "Message": "Successful Request, Now Your Loan is Pending",
            "data": serializer.data
        },
            status=status.HTTP_201_CREATED, headers=headers)


class Offers(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "Status": True,
            "Message": "Successful Offer, Now Your Offer is Sent",
            "data": serializer.data
        },
            status=status.HTTP_201_CREATED, headers=headers)


class test(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = testing

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "Status": True,
            "Message": "Successful Offer, Now Your Offer is Sent",
            "data": serializer.data
        },
            status=status.HTTP_201_CREATED, headers=headers)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer


class LoanRequestViewSet(viewsets.ModelViewSet):
    queryset = Loan_Request.objects.all()
    serializer_class = LoanRequestSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class LoanInstallmentsViewSet(viewsets.ModelViewSet):
    queryset = Loan_Installments.objects.all()
    serializer_class = LoanInstallmentsSerializer
