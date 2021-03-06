---
layout: default
title: SEQR Instant Checkout
description: SEQR Instant Checkout
---

# SEQR Instant Chekout introduction

SEQR Instant Checkout is service that allows you to pay with SEQR on web-shops without need of going through all that steps required for standard checkout.
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
| createPurchase | web-shop | [SEQR Instant Checkout](/merchant/reference/instantcheckoutapi.html) | REST service called by SEQR Instant chekout service once user scanned QR Code from web-shop page. URL has to be HTTPS and end with "createPurchase" (for example https://yourdomain.name.com/seqr/createPurchase).  |
| sendInvoice | SEQR | [SEQR Payment](/merchant/reference/api.html) | SOAP method called by web-shop triggered by CreatePurchase request. This method creates invoice on SEQR side and returns it's reference number (invoiceReference). By calling this method web-shop provides also <b>notificationUrl</b> to be used for callbacks. |
| notification callback service | web-shop | [SEQR Payment](/merchant/reference/api.html) | <b>notificationUrl</b> will be called (empty HTTPS POST responded with HTTP 200 OK code) by SEQR once customer confirmed payment. |
| getPaymentStatus | SEQR | [SEQR Payment](/merchant/reference/api.html) | SOAP method called by web-shop after receiving request to <b>notificationUrl</b>. This method will return status of payment. If returned status is "PAID" this is also commit of transaction. Once payment is commited you have to take care of product stock level. |
| refundPayment | SEQR | [SEQR Payment](/merchant/reference/api.html) | Refunds a previous payment, partly or the whole sum. |
|--- | --- | --- | --- |

<b>All above methods/services are mandatory to implement.</b>

# Flow description

1. Customer scanns QRCode placed on web-shop page using SEQR app.
2. Delivery address details stored in SEQR are presented to customer.
3. Customer confirms delivery address in SEQR app by pressing "Confirm" button.
4. SEQR Instant Checkout service calls createPurchase exposed by web-shop sending JSON with purchaseToken (product or productBundle id) and customer's delivery address details.
5. web-shop calls sendInvoice exposed by SEQR.
6. Purchase details are presented to customer.
7. Customer confirms purchase with PIN number.
8. SEQR calls notificationUrl provided in sendInvoice request.
9. web-shop calls getPaymentStatus exposed by SEQR.
10. Transaction committed. Customer sees confirmation on phone screen.


# Overview of integration steps
To achieve a full integration between SEQR Instant Chekout and web shoop these steps must be covered:

1. Create and expose REST service implementing SEQR Instant Checkout API (createPurchase). API details can be found [here](/merchant/reference/instantcheckoutapi.html).
2. Implement methods from SEQR Payment API (sendInvoice, getPaymentStatus). API details and test endpoint URL can be found [here](/merchant/reference/api.html).
3. Expose service for notifications (notificationUrl).
4. Put SEQR Instant Checkout QRCodes on product details page.
5. Test that integration works.

# Create and expose REST service
SEQR Instant Checkout API description can be found [here](/merchant/reference/instantcheckoutapi.html).
Test creadentials can be found [here](/merchant/reference/signup.html).

# Implement methods from SEQR Payment API
There have to be two methods of SEQR Payment API implemented on your web-shop's backend side - sendInvoice and getPaymentStatus.
More details you can find [here](/merchant/reference/api.html).

# Expose service for notifications
<b>notificationUrl</b> is one of the parameters of sendInvoice request. This parameter tells SEQR where to send notification once invoice is paid.
This url has to be unique for diffferent purchases. Let say customer bought product with id 000111222, then your notificationUrl can look like this:

{% highlight python %}
   https://your.webshop.domain.com/orderNotif?productId=000111222
{% endhighlight %}

Once your web-shop received such request it should:

* Call getPaymentStatus and receive status PAID - this is commit of transaction.
* Update product stock level.
* It would also be good idea to send email with order confirmation to customer.

# Put SEQR Instant Checkout QRCodes on product details page (or anyware you like)
In order to put SEQR Instant Checkout QR codes on your pages you will have to:

* Import our java script qr code generator:

{% highlight python %}
<div id="qrcode"></div>

<script src="http://cdn.seqr.com/seqr-services-dev/wss-dev/seqrQRCode-0.0.3.min.js">
</script>
{% endhighlight %}

* Put this piece of code on you page:

{% highlight python %}
<div id="qrcode"></div>

<script>
    $(document).ready(function() {
        seqrQRCode.qrCode({
            selector: '#qrcode',
            purchaseToken: some_token_recognized_by_webshop,
            webshopId: 'example_shop_id',
        });
    })
</script>
{% endhighlight %}

|---|---|
| parameter | description |
|---|---|
| selector | id of the html div tag that is going to be wired as the widget. |
| purchaseToken | This is id of the product or product bundle or product SKU which will be used in CreatePurchase call. Acceptable chars: <span class="seqrhl">alphanumeric</span>, '<span class="seqrhl">-</span>', '<span class="seqrhl">_</span>', '<span class="seqrhl">.</span>'. |
| webshopId | This is the id of web-shop recognised by SEQR Instant Checkout service. |
|---|---|
