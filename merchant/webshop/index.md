---
layout: default
title: SEQR Webshop Payments
description: SEQR Merchant, webshop, POS integration
---


## SEQR in a WebShop

Add SEQR payment in your “Check out” process where your 
customer normally selects between payment methods. This is an example of a 
checkout that supports SEQR:

<img src="/assets/images/seqr_webshop.png" />

[See a live demo!](http://devapi.seqr.com/sample)

The flow for a webshop SEQR payment is very similar to [Making your first SEQR
payment](/merchant/payment).
The difference is that polling for payment status is handled by a payment view,
which also handles showing the QR code to the SEQR user. You still need to request
the status of the payment after the payment view returns, but only once to find
out the final status of the invoice.
To integrate SEQR, follow these steps:

1. Integrate the payment view
2. Present the receipt
3. Go live!

### 1. Integrate the payment view
There are two payment views that you can choose from:

Standard Payment View
<img src="/assets/images/paymentview-standard.png" />

Small Payment View
<img src="/assets/images/paymentview-small.png" />

Payment View - When SEQR doesn't support the user's phone
<img src="/assets/images/paymentview-nosupport.png" width="50%"/>

To integrate with SEQR, insert the following script tag into your checkout
page. The script will insert SEQR payment views at the same location.

{% highlight html %}
<script
 id="seqrShop"
 src="http://devapi.seqr.com/ws/js/seqrShop.js#!invoiceId=[invoiceReference]">
</script>
{% endhighlight %}

View parameters are:

| Name        | Description | Values | Default |
|-------------|-----------|---------|-----|
| invoiceId   | (required) invoice reference that you received from sendInvoice method | - | - |
| layout      | (optional) layout for the payment view | standard, small | standard |
| language    | (optional) language for texts in payment view | en, sv, ... | detected from browser, falls back to English if not available |
| successCallback | (optional) this javascript method is invoked after the payment is successful | - | - |
| successURL  | (optional) redirect to this URL upon successful payment | - | - |

**Note:** when your webshop is browsed on mobile phones, you provide the backUrl in
 sendInvoice method. After a successful/cancelled payment, the app will redirect
the SEQR user to the URL specified in the invoice.

### 2. Present the receipt

Once the payment is completed, your webshop should query the status of the invoice
from SEQR by calling getPaymentStatus. If the invoice was successfully paid, 
a reference number (ersReference) is obtained from 
SEQR. Save the reference number for follow-ups and for print on the customer 
online confirmation receipt.

### 3. Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html) and receive the credentials to your webshop.
