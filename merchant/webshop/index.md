---
layout: default
title: SEQR Webshop Payments
description: SEQR Merchant, webshop, POS integration
---


## SEQR in a WebShop

Add SEQR as a new payment method in the “Check out” process where the 
customer selects between different methods of payment. This is an example of a 
checkout that supports SEQR:

<img src="/assets/images/seqr_webshop.png" />

The flow for a webshop SEQR payment is very similar to the [basic SEQR
payment](/merchant/payment).
The difference is in how the SEQR QR code is presented to the SEQR
user. To integrate SEQR, follow these steps:
1. Integrate the payment view 
2. Present the QR code 
3. Present receipt

### 1. Integrate the Payment View
There are two payment views that you can choose from:

* Standard Payment View
* Slim Payment View

Embed the HTML file in your webshop checkout and replace the SEQR QR code image
and SEQR link with the response you receive from SEQR service.


### 2. Present the QR Code

The payment method for SEQR is displayed with the SEQR logotype and when 
selecting SEQR the QR code to scan is displayed (see example picture below), or if the 
user is using a smartphone, a link will be shown to press to open the SEQR app (see 
Mobile example in the Module pictures above)

<div id="qr-code-frame-wrapper">
    <iframe id="qr-code-frame"
      src="/downloads/webshop_modules/module1/seqr-payment-module1.html"></iframe>
</div>
<script>
$("#qr-code-frame-wrapper").resizable({
    alsoResize : '#qr-code-frame'
});
</script>

The invoice rows are sent from the webshop to SEQR service with the sendInvoice
request, which returns (in the sendInvoice response) invoiceQRCode string such as
 HTTP://SEQR.SE/R12345 . 

You can create the QR code using the following URL:
[http://seqr.com/se-qr-web/qrgenerator?code=HTTP://SEQR.SE/R1234](http://seqr.com/se-qr-web/qrgenerator?code=HTTP://SEQR.SE/R1234)

To generate the in-app link, you need to replace HTTP in the beginning
of invoiceQRCode with SEQR, for example: SEQR://SEQR.SE/R12345 .

Each module contains three different sizes to be used depending on type (size) of device 
that is used for payment (smartphone, tablet, etc.) Two of the sizes contain a QR code to 
scan, whilst the third contains a link that forwards the payer to SEQR app. The latter is
used in case of browsing the webshop using a smartphone, that's why it is using SEQR protocol.
The difference between the modules is that one contains an introduction film about 
SEQR. Both modules contain download links to SEQR app.


### 3. Present Receipt

After a SEQR payment,
