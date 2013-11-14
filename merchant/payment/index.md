---
layout: default
title: First SEQR Payment
description: SEQR Merchant, webshop, POS integration
---

<img src="/assets/images/cash_register_bw.png" align="right" width="200px"/>

## Get SEQR Payments

Feel hungry for real payments now? Just make sure you have the following in place:
1. [the SEQR app installed](../app/) before following.
2. For python sample, you will need PIL and qrpython library (pip install qrcode PIL)


## SEQR Payment in Python

Create a a bill and publish it to the app (python): 

{% highlight python %}
# create an invoice
invoice = client.factory.create("ns0:invoice")
invoice.paymentMode = "IMMEDIATE_DEBIT"
invoice.acknowledgmentMode = "NO_ACKNOWLEDGMENT"
invoice.title="Thai Massage Center"
# our invoice has just one row
invoice.invoiceRows = client.factory.create('ns0:invoiceRows')
row1 = invoice.invoiceRows.invoiceRow = client.factory.create('ns0:invoiceRow')
row1.itemDescription = "Thai Massage"
row1.itemTotalAmount = client.factory.create('ns0:itemTotalAmount')
row1.itemTotalAmount.value, row1.itemTotalAmount.currency = "500", "SEK"
invoice.totalAmount = client.factory.create('ns0:totalAmount')
invoice.totalAmount.value, invoice.totalAmount.currency = "500", "SEK"
# publish the invoice to the app
invoiceResponse = client.service.sendInvoice(context, invoice)
{% endhighlight %}

Querying for payment status:

{% highlight python %}
response = client.service.getPaymentStatus(context,
            invoiceResponse.invoiceReference)
while response.resultCode == 0 and response.status == "ISSUED":
    time.sleep(1)
    response = client.service.getPaymentStatus(context,
                invoiceResponse.invoiceReference)
{% endhighlight %}

Putting it all together, following is a basic sample for a payment:

{% highlight python %}
{% include payment.py %}
{% endhighlight %}
 
### Try more functions
So this is the core of SEQR payments. The same flow, more or less, can be used
in all the payment scenarios you see in the next section.