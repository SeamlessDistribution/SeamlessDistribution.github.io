---
layout: default
title: SEQR Unattended Payments Service
description: SEQR Unattended Payments Service
---

# SEQR Unattended Payments Service introduction

SEQR Unattended Payments Service is service that allows your unattended POS to integrate with SEQR.

<img src="/assets/images/instantcheckout/productdetailssample.png" width="600px"/>

On this page you will find information how to set up integration of SEQR Instant Chekout system with your web-shop.

# Actors

* <b>SEQR user</b> - SEQR's and self-service machine user
* <b>reseller</b> - your backend maintaining self-service machines
* <b>SEQR Unattended Payments service</b> - SEQR service that will initiate purchase process on reseller side 
* <b>SEQR</b> - SEQR backend 
* <b>SEQR app</b> - SEQR mobile application


# Flow diagram

All starts with user scanning QR code on your web-shop.

<img src="/assets/images/ups/ups_diagram.png" width="500px"/>

|---| --- | --- | --- |
| method/service | exposed by | part of API | description |
|---| --- | --- | --- |
| createPurchase | reseller | [SEQR Instant Checkout](/merchant/reference/instantcheckoutapi.html) | REST service called by SEQR Instant chekout service once user scanned QR Code from web-shop page. URL has to be HTTPS and end with "createPurchase" (for example https://yourdomain.name.com/seqr/createPurchase).  |
| sendInvoice | SEQR | [SEQR Payment](/merchant/reference/api.html) | SOAP method called by web-shop triggered by createPurchase request. This method creates invoice on SEQR side and returns it's reference number (invoiceReference). By calling this method web-shop provides also <b>notificationUrl</b> to be used for callbacks. |
| notification callback service | web-shop | [SEQR Payment](/merchant/reference/api.html) | <b>notificationUrl</b> will be called (empty HTTPS POST responded with HTTP 200 OK code) by SEQR once customer confirmed payment. |
| updateInvoice | SEQR | SOAP method called by reseller after user choose products from self-service machine to update rows and totalAmount of final invoice. |
| commitReservation | SEQR | [SEQR Payment](/merchant/reference/api.html) | SOAP method called by reseller to finalise payment process. |
|--- | --- | --- | --- |

<b>All above methods/services are mandatory to implement.</b>

# Flow description

1. Customer scanns QRCode placed on sel-service machine using SEQR app.
2. SEQR Unattended Payments service calls createPurchase exposed by reseller sending JSON with purchaseToken (machine id).
3. Reseller calls sendInvoice exposed by SEQR and returns the invoice reference to SEQR Unattended Payments service.
4. Reservation details are presented to customer.
5. Customer confirms reservation with PIN number.
6. SEQR calls notificationUrl provided in sendInvoice request.
7. Reseller unlocks self-service machine allowing user to choose the products.
8. Customer choose products from self-service machine.
9. Reseller calls updateInvoice exposed by SEQR to change details of invoice that user will see in SEQR app.
10. Reseller calls commitReservation to commit transaction with final amount.

# SEQR Unattended Payment Service API

At this point our SEQR Unattended Payment Service API is based on one REST method - createPurchase which is required to be exposed by reseller.

## createPurchase method
This method will be called by SEQR Unattended Payment Service once customer scanned SEQR QR Code on unattended POS. SEQR Unattended Payment Service service will sent below values to reseller's backend.

### createPurchase request

{% highlight python %}
URL: https://yourdomain.name.com/seqr/createPurchase
HTTP method: POST
Headers: "Accept: application/json;Content-Type: application/json;charset=UTF-8"
Body:
{
    "reservationToken": "29834231890234",
    "reservationAmount": "20.0",
    "currency": "EUR",
    "msisdn": "483344323423"
}
{% endhighlight %}

|--|---|
| parameter | description |
|--|---|
| reservationToken | This is identifier of self-service machine or purchase. |
| reservationAmount | Max reservation amount for which invoice should be created by reseller. |
| currency | Currency of reservation amount. |
| msisdn | Customer's phone number. |
|--|---|

### createPurchase response

{% highlight python %}
Status Code: 200
Headers: "Content-Type: application/json;charset=UTF-8"
Body:
{
   "invoiceReferenceId":"20170315072260070"
}
{% endhighlight %}

|--|---|
| parameter | description |
|--|---|
| invoiceReferenceId | invoiceReference from sendInvoice response [see SEQR Payment API](/merchant/reference/api.html). |
|--|---|

### Error createPurchase response

{% highlight python %}
Status Code: 200
Headers: "Content-Type: application/json;charset=UTF-8"
Body:
{
   "errorCode":"SYSTEM_ERROR"
}
{% endhighlight %}

|--|---|
| parameter | description |
|--|---|
| errorCode | Error code specifying the error on reseller's backend. |
|--|---|

### Possible values of error code

|--|---|
| parameter | description |
|--|---|
| INSUFFICIENT_FUNDS | reservationAmount is to low to start the payment flow on reseller's side. Eg. reservationAmount is lower than cheapest product in self-service machine. |
| DEVICE_IN_USE | Device is already used by another customer. Someone else scanned qrCode, agreed for purchase but didn't choose the product yet. |
| DEVICE_UNAVAILABLE | Self-service machine is out of service. |
| INVOICING_ERROR | Error occurred while calling sendInvoice exposed by SEQR (SEQR Payment API). |
| SYSTEM_ERROR | Generic error. |
|--|---|















