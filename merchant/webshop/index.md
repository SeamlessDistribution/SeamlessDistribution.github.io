---
layout: default
title: SEQR Webshop Payments
description: SEQR Merchant, webshop, POS integration
---


# SEQR payment in a Webshop

To integrate your webshop with SEQR, you need to add SEQR payment in your “Check out” process where your customer normally selects between payment methods. This is an example of a checkout that supports SEQR:

<img src="/assets/images/seqr_webshop.png" />

[See a live demo!](http://devapi.seqr.com/seqr-webshop-sample/)


## Integration procedure

Follow these steps to integrate your webshop with SEQR:

1. Add API parameters
2. Add SEQR as payment in your webshop
2. Present the receipt
3. Verify your integration
4. Go live!

### Add API parameters

The flow for a webshop SEQR payment is very similar to [Basic SEQR
payment](/merchant/payment), with the **sendInvoice** request.
The difference is that polling for payment status is handled by a payment view,
which also handles showing the QR code to the SEQR user. You still need to request
the status of the payment after the payment view returns, but only once to find
out the final status of the invoice.

The methods required in a basic integration are:

|--- | --- |
|  Method | Description |
|--- | --- |
| sendInvoice | Sends an invoice to SEQR server |
| getPaymentStatus | Obtains status of a previously submitted invoice |
| markTransactionPeriod | Marks the end of one and the beginning of a new transaction period; used in reporting |
| --- | --- |


For an extended integration, also these methods can be used:

|--- | --- |
|  Method | Description |
|--- | --- |
| updateInvoice | Updates an already sent invoice with new set of invoice rows or attributes |
| cancelInvoice | Cancels an unpaid invoice |
| submitPaymentReceipt | Sends the receipt document of a payment |
| executeReport | Executes a report on SEQR server |
| --- | --- |


Refer to section [API](/merchant/reference/api.html) for detailed description.


### Add SEQR as payment in your webshop  

#### 1. Integrate the payment view
There are two payment views that you can choose from, standard payment view and small payment view:

#### Standard Payment View
<img src="/assets/images/paymentview-standard.png" />

#### Small Payment View
<img src="/assets/images/paymentview-small.png" />

#### Payment View - When SEQR doesn't support the user's phone
<img src="/assets/images/paymentview-nosupport.png" width="50%"/>

To integrate with SEQR, insert the following script tag into your checkout
page. The script will insert SEQR payment views at the same location.

{% highlight html %}
<script
 id="seqrShop"
 src="http://devapi.seqr.com/seqr-webshop-plugin/js/seqrShop.js#!invoiceReference=[invoiceReference]">
</script>
{% endhighlight %}

#### View parameters 

| Name             | Description | Values | Default |
|------------------|-----------|---------|-----|
| invoiceReference | (required) invoice reference that you received from sendInvoice request | - | - |
| layout           | (optional) layout for the payment view | standard, small | standard |
| language         | (optional) language for texts in payment view | en, sv, ... | detected from browser, falls back to English if not available |
| paidCallback     | (optional) this javascript method is invoked after the payment is successful | - | - |

**Note:** when your webshop is browsed on mobile phones, you provide the backUrl in
 **sendInvoice** request. After a successful/cancelled payment, the app will redirect
the SEQR user to the URL specified in the invoice.


#### 2. Get payment status

Once the payment is completed, your webshop should query the status of the invoice
from SEQR by calling **getPaymentStatus**. 

**Note!** The web server must check the status each second, to verify that payment is completed. Otherwise SEQR server does not receive any notification that transaction is finalized and the payment will then be reversed!
This request should be triggered from a javascript timer on the website, so when SEQR user closes the window or moves away from the payment page, the polling stops. Another benefit is that you do not need to have a polling-loop on your backend, which will improve your webshop’s server performance.


### Present the receipt

If the invoice was successfully paid, a reference number (ersReference) is obtained from 
SEQR. Save the reference number for follow-ups and for print on the SEQR user's 
online confirmation receipt.

### Verify your integration

Verify that your integration works and run validation tests towards SEQR servers. [Contact](/contact) Seamless for more information. 

### Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html).
