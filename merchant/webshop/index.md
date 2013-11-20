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

The flow for a webshop SEQR payment is very similar to the [Making your first SEQR
payment](/merchant/payment).
The difference is in how the SEQR QR code is presented to the SEQR
user. To integrate SEQR, follow these steps:
1. Integrate the payment view 
2. Present the QR code 
3. Present the receipt

### 1. Integrate the Payment View
There are two payment views that you can choose from:

* Standard Payment View
<img src="/assets/images/webshop_module1.png" />

* Small Payment View
<img src="/assets/images/webshop_module2.png" />

Embed the HTML file in your webshop checkout and replace the dynamic parts with
the responses you get from SEQR service.


### 2. Present the QR Code

The payment method for SEQR is displayed with the SEQR logotype and when 
selecting SEQR, the QR code to scan is displayed, or if the 
user is using a smartphone, a link will be shown to press to open the SEQR app.

The invoice rows are sent from the webshop to SEQR service with the sendInvoice
request, which returns invoiceQRCode in the response, for example
 HTTP://SEQR.SE/R12345 . 

To provide the payment view with required information, follow these steps:

1. Create the QR code using the following URL:
[http://seqr.com/se-qr-web/qrgenerator?code=HTTP://SEQR.SE/R1234](http://seqr.com/se-qr-web/qrgenerator?code=HTTP://SEQR.SE/R1234)
and put it in the specified place in the payment view

2. Generate the in-app link, you need to replace HTTP in the beginning
of invoiceQRCode with SEQR, for example: SEQR://SEQR.SE/R12345 , and put it in
the specified place in the payment view

<div id="qrcode-frame-wrapper1">
    <iframe id="qr-code-frame1" width="100%" height="450px"
        src="/downloads/webshop_modules/module1/seqr-payment-module1.html">
    </iframe>
</div>

Each module contains three different sizes to be used depending on type (size) of device 
that is used for payment (smartphone, tablet, etc.). Two of the sizes contain a QR code to 
scan, whilst the third contains a link that forwards the payer to SEQR app.
The latter is
used in case of browsing the webshop using a smartphone, that's why it is using SEQR protocol.
The difference between the modules is that one contains an introduction film about 
SEQR. Both modules contain download links to SEQR app.


After showing the QR code to the SEQR user, the webshop should start polling the SEQR
system to check if payment is completed. This request should be triggered from a
javascript timer on the website, so when SEQR 
user closes the window or moves away from the payment page, the polling stops. 
Another benefit is that you do not need to have a polling-loop on your backend, which 
will improve your webshop’s server performance. 





### 3. Present the Receipt

Once the payment is completed a reference number (ersReference) is obtained from 
SEQR. Save the reference number for follow-ups and for print on the customer 
online confirmation receipt.



