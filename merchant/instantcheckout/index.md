---
layout: default
title: SEQR Instant Checkout
description: SEQR Instant Checkout
---

# SEQR Instant Chekout introduction

SEQR Instant Checkout is service that allows you to pay with SEQR on web-shops without need of going thrugh all that steps required for standard checkout.
In fact all you have to do as customer is scanning QR code displayed on product (or product bundle) details page, confirm with PIN in SEQR application and voilà!


<img src="/assets/images/instantcheckout/productdetailssample.png" width="600px"/>


On this page you will find information how to set up integration of SEQR Instant Chekout system with your web-shop.


# Actors

* <b>web-shop</b> - your online store
* <b>SEQR Instant Checkout service</b> - SEQR service that will pass customer's address details to web-shop and will initiate purchase process on web-shop side
* <b>SEQR</b> - SEQR backend 
* <b>SEQR app</b> - SEQR mobile application


# Flow diagram

All starts with user scanning QR code on your web-shop.

<img src="/assets/images/instantcheckout/instantCkeckoutFlowDiagram.png" width="500px"/>

|---| --- | --- | --- |
| method/service | exposed by | part of API | description |
|---| --- | --- | --- |
| CreatePurchase | web-shop | [SEQR Instant Checkout](/merchant/reference/instantcheckoutapi.html) | REST service called by SEQR Instant chekout service once user scanned QR Code from web-shop page |
| sendInvoice | SEQR | [SEQR Payment](/merchant/reference/api.html) | SOAP method called by web-shop triggered by CreatePurchase request. This method creates invoice on SEQR side and returns it's reference number (invoiceReference). This by calling this method web-shop provides also <b>notificationURL</b> to be used for callbacks |
| notification callback service | web-shop | [SEQR Payment](/merchant/reference/api.html) | <b>notificationURL</b> will be called (empty HTTPS POST) by SEQR once customer confirmed payment.|
| getPaymentStatus | SEQR | [SEQR Payment](/merchant/reference/api.html) | SOAP method called by web-shop after receiving request to <b>notificationURL</b>. This method will return status of payment. If returned status is "PAID" this is also commit of transaction. Once payment is commited you have to take care of product stock level. |
|--- | --- | --- | --- |

# Flow description

1. Customer scanns QRCode placed on web-shop page using SEQR app
2. Delivery address details stored in SEQR are presented to customer
3. Customer confirms delicery address in SEQR app by pressing "Confirm" button
4. SEQR Instant Checkout service calls CreatePurchase exposed by web-shop sending JSON with purchesToken (product or productBundle id) and customer's delivery address details.
5. web-shop calls sendInvoice exposed by SEQR
6. Purchase details are presented to customer
7. Customer confirms with PIN number
8. SEQR calls notificationURL provided in sendInvoice request
9. web-shop calls getPaymebtStatus exposed by SEQR
10. Transaction committed. Customer sees confirmation on phone screen


# Overview of integration steps
To achieve a full integration between SEQR Instant Chekout and web shoop these steps must be covered:

1. Create and expose REST service implementing SEQR Instant Checkout API (CreatePurchase).
API details and test endpointURL can be found [here](/merchant/reference/instantcheckoutapi.html)
2. Implement methods from SEQR Payment API (sendInvoice, getPaymentStatus).
API details and test endpointURL can be found [here](/merchant/reference/api.html)
3. Expose service for notifications (notificationURL)
4. Put SEQR Instant Checkout QRCodes on product details page
5. Test that integration works

# Create and expose REST service
SEQR Instant Checkout API descrition can be found [here](/merchant/reference/instantcheckoutapi.html).
Test creadentials can be found [here](/merchant/reference/signup.html).

# Implement methods from SEQR Payment API
There have to be two methods of SEQR Payment API implemented on your web-shop's backend side - sendInvoice and getPaymentStatus.
More details you can find [here](/merchant/reference/api.html).

# Expose service for notifications
<b>notificationURL</b> is on of the parameters of sendInvoice request. This parameter tells SEQR where to send notification once invoice is paid.
This url has to be unique for diffferent purchases. Let say customer bought product with id 000111222, then your notificationURL can look like this:

{% highlight python %}
   https://your.webshop.domain.com/orderNotif?productId=000111222
{% endhighlight %}

Once your web-shop received such request it should:

Call getPaymentStatus and receive status PAID - this is commit of transaction
Update product stock level.
It would also be good idea to send email with order confirmation to customer.

# Put SEQR Instant Checkout QRCodes on product details page (or anyware you like)
In order to put SEQR Instant Checkout QR codes on your pages you will have to:

1. Import our java script qr code generator
<script src="http://cdn.seqr.com/seqr-services-dev/wss-dev/seqrQRCode-0.0.1.min.js"></script>

2. Put this piece of code on you page:

{% highlight python %}
<div id="qrcode"></div>
  
<script>
    $(document).ready(function() {
        seqrQRCode.qrCode({
            selector: '#qrcode',
            purchaseToken: some_token_recognized_by_webshop,
            webshopId: 'example_shop_id',
            mode: 'demo'
        });
    })
</script>

{% endhighlight %}

|---|---|
| parameter | description |
|---|---|
| selector | id of the html div tag that is going to be wired as the widget |
| purchaseToken | This is id of the product or product bundle or product SKU which will be used in CreatePurchase call |
| webshopId | This is the id of web-shop recognised by SEQR Instant Checkout service |
| mode | Version of SEQR app. Should be set to "demo" for integration purpos. On production this parameter should be removed. |
|---|---|
