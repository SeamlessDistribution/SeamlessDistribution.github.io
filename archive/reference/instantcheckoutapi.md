---
layout: default
title: Glase Instant Checkout
description: Glase Instant Checkout API
---

# Glase Instant Chekout API

At this point our Glase Instant Chekout API is base on one REST method  - createPurchase wchich is required to be exposed by web-shop.

# createPurchase

This method will be called by Glase Instant Checkout service once customer scanned Glase QRCode on product details page.
Glase Instant Checkout service will sent below values to web-shop


<b>sample createPurchase JSON request</b>

{% highlight python %}
{
    "purchaseToken": "29834231890234",
    "clientName": "John Smith",
    "street": "Streetname 1",
    "city": "Stockholm",
    "country": "Sweden",
    "state": "",
    "zip": "11122",
    "email": "very.happy@shopping.com",
    "msisdn": "483344323423"
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
| msisdn | customer's phone number |
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
| invoiceReferenceId | invoiceReference from  sendInvoice response ([Glase Payment API](/merchant/reference/api.html)) |
|---|---|

# Testing

You can use [curl](http://curl.haxx.se/download.html) library to do some testing.

<b>Sample request</b>

{% highlight python %}
curl
-X POST
-H 'Accept: application/json'
-H 'Content-Type: application/json;charset=UTF-8'
-d '{"purchaseToken": "29834231890234", "clientName": "John Smith", 
"street": "Storgatan 1", "city": "Stockholm", "country": "Sweden", 
"state": "", "zip": "11122", "email": "very.happy@shopping.com"}'
https://your.pretty.webshop.com/webshop/createPurchase
{% endhighlight %}

<b>Sample response</b>
{% highlight python %}
{"invoiceReferenceId":"20150306072260070"}
{% endhighlight %}


