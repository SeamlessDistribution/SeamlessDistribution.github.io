---
layout: default
title: Implement SEQR Payments
description: SEQR Merchant, webshop, POS integration
---

<img src="/assets/images/cash_register_bw.png" align="right" width="200px"/>

# Basic SEQR payment

Make a test purchase:

1. Create a bill and publish it to the app
2. Pay using SEQR app
3. Check the payment status

The example uses [public credentials](../reference/signup.html) that you can use for testing. 

## Sequence (simplified)

<div class="diagram">
@startuml
skinparam monochrome true
participant "SEQR App" as SEQRApp
Seller->SEQR: sendInvoice
SEQR-->Seller: (invoice reference)
Seller->SEQR: getPaymentStatus
SEQR-->Seller: ISSUED
SEQRApp->SEQR: ask for invoice at QR-code
SEQR->SEQR App: retry until you get SUCCESS
SEQRApp->SEQR: payment
Seller->SEQR: getPaymentStatus
SEQR-->Seller: PAID
Note right of Seller: Payment cleared!
SEQR->SEQRApp: Done (show receipt)
Seller-->SEQRApp: Happy!
@enduml
</div>

## Create a bill and publish it to the app 

You will need PIL and qrpython library (pip install qrcode PIL suds)

{% highlight python %}
# create an invoice
invoice = client.factory.create("ns0:invoice")
invoice.paymentMode = "IMMEDIATE_DEBIT"
invoice.acknowledgmentMode = "NO_ACKNOWLEDGMENT"
invoice.title="Grand Cinema"
# our invoice has just one row
invoice.invoiceRows = client.factory.create('ns0:invoiceRows')
row1 = invoice.invoiceRows.invoiceRow = client.factory.create('ns0:invoiceRow')
row1.itemDescription = "Movie Tickets"
row1.itemTotalAmount = client.factory.create('ns0:itemTotalAmount')
row1.itemTotalAmount.value, row1.itemTotalAmount.currency = "500", "SEK"
invoice.totalAmount = client.factory.create('ns0:totalAmount')
invoice.totalAmount.value, invoice.totalAmount.currency = "500", "SEK"
# publish the invoice to the app
invoiceResponse = client.service.sendInvoice(context, invoice)
{% endhighlight %}


## Pay using SEQR app

Download and install SEQR app, refer to [Get SEQR app](../../app/).


## Check for payment status

{% highlight python %}
response = client.service.getPaymentStatus(context,
            invoiceResponse.invoiceReference)
while response.resultCode == 0 and response.status == "ISSUED":
    time.sleep(1)
    response = client.service.getPaymentStatus(context,
                invoiceResponse.invoiceReference)
{% endhighlight %}


**Note!** 
The POS must check the status each second, to verify that payment is completed. Otherwise the SEQR server does not receive any notification that transaction is finalized and the purchase will then be reversed!



* [Putting it all together](python-script.html) 



## Try more functions
So this is the core of SEQR payments. The same flow, more or less, can be used
in all the payment scenarios you see in the next section.
