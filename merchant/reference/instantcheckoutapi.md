---
layout: default
title: SEQR Instant Checkout API
description: SEQR Instant Checkout API
---

# SEQR Instant Chekout API

At this point our SEQR Instant Chekout API is base on one REST method  - createPurchase wchich is required to be exposed by web-shop.

# createPurchase

This method will be called by SEQR Instant Checkout service once customer scanned SEQR QRCode on product details page.
SEQR Instant Checkout service will sent below values to web-shop


<b>sample createPurchase JSON request</b>

{% highlight python %}
{
    "purchaseToken": "29834231890234",
    "clientName": "Kalle Karlsson",
    "street": "Storgatan 1",
    "city": "Stockholm",
    "country": "Sweden",
    "state": "",
    "zip": "11122",
    "email": "very.happy@shopping.com"
}
{% endhighlight %}

|--|---|
| parameter | description |
|--|---|
| purchaseToken | This is purchase indentifier which has to unambiguously identify the purchese (product, size, color etc). |
| clientName | Name of customer |
| street | street of delivery address |
| city | city/town of delivery address |
| country | country of delivery address |
| state | street of delivery address |
| zip | zip or postal code of delivery addres |
| email | email address of customer |
|--|---|

<b>sample createPurchase response</b>
{% highlight python %}
{
   "invoiceReferenceId":"20150306072260070"
}
{% endhighlight %}


|---|---|
| parameter | description |
|---|---|
| invoiceReferenceId | invoiceReference from  sendInvoice response ([SEQR Payment API](/merchant/reference/api.html)) |
|---|---|

# Testing

You can use [curl](http://curl.haxx.se/download.html) library to do some testing.

<b>Sample request</b>

{% highlight python %}
curl
-X POST
-H 'Accept: application/json'
-H 'Content-Type: application/json;charset=UTF-8'
-d '{"purchaseToken": "29834231890234", "clientName": "Kalle Karlsson", 
"street": "Storgatan 1", "city": "Stockholm", "country": "Sweden", 
"state": "", "zip": "11122", "email": "very.happy@shopping.com"}'
https://your.pretty.webshop.com/webshop/createPurchase
{% endhighlight %}

<b>Sample response</b>
{% highlight python %}
{"invoiceReferenceId":"20150306072260070"}
{% endhighlight %}


