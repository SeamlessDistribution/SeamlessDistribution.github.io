---
layout: default
title: SEQR In-app Payments
description: SEQR Merchant, webshop, POS, service, in-app integration
---


## SEQR payment in your app 

Add SEQR payment in your “Check out” process where your 
customer normally selects between payment methods. 

All apps offering payments typically have a backend that handles the actual service/product that is sold. It is this backend that must connect to SEQR using our interface, and the communication between your app and your backend is up to your app developer.

The flow for an app SEQR payment is very similar to [Making your first SEQR payment](/merchant/payment).
The difference is that the user presses a "pay" button or link in your app, which launches the SEQR app and presents the bill for the user to confirm the payment.
You still need to request the status of the payment after your app returns (with backURL), but only once to find out the final status of the invoice.

To integrate SEQR, follow these steps:

1. Insert the payment URL
2. Present the receipt
3. Go live!

### 1. Insert the payment URL

Make a redirection (button or link) in your app, which launches the SEQR app, using the QR code URL returned from the sendInvoice request: Replace the "HTTP:" header with "SEQR:"; that is, if sendInvoice returns HTTP://SEQR.SE/R12345, the button/link should instead use SEQR://SEQR.SE/R12345.


**Note:** when your app shop is browsed, you provide the backURL in the
 sendInvoice request. After a successful/cancelled payment, the app will redirect the SEQR user to the URL specified in sendInvoice. Typically this will be a URL with a URL scheme that will launch the calling app again.

### 2. Present the receipt

Once the payment is completed, your app should query the status of the invoice from SEQR by calling getPaymentStatus. If the invoice was successfully paid, a reference number (ersReference) is obtained from 
SEQR. Save the reference number for follow-ups and for print on the user 
online confirmation receipt.


### 3. Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html) and receive the credentials to your app.
