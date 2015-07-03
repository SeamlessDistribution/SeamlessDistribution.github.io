---
layout: default
title: SEQR Invoice Service
description: SEQR Invoice Service API
---

# SEQR Invoice Service API

At this point our SEQR Invoice Service API is based on one REST method  -  wchich is required to be exposed by invoice issuer.

# Notification Service

Invoice issuer is expected to expose a URL which will be called by SEQR Invoice service using HTTP POST with JSON payload about an invoice which has just been paid. The description of JSON payload is presented in a table below.


<b>sample JSON request</b>

{% highlight python %}
{
    "id": 576,
    "description": "Phone invoice 05.2015",
    "amount": 59.99,
    "currency": "GBP",
    "status": "PAID",
    "reference": "586930/05/2015",
    "ersReference": "892736823467823-3897474",
    "purchaseTime": "15.05.2015 15:37:33",
    "payerMsisdn": "46111222333",
    "payerFirstName": "John",
    "payerLastName": "Smith",
    "payerStreet": "34 Wellington St",
    "payerCity": "London",
    "payerZip": "74231",
    "payerCountry": "en"
}
{% endhighlight %}

|--|---|
| parameter | description |
|--|---|
| id | unique identifier of an invoice in SEQR Invoice service |
| description | description of an invoice provided by an issuer |
| amount | amount paid, format 123.45 ('.' as a decimal separator) |
| currency | 3-characters logs currency of an amount, eg. EUR |
| status | status of invoice, at the moment the only possible value is PAID |
| reference | identifier of an invoice provided by an issuer |
| ersReference | identifier of a transaction in SEQR which paid the invoice |
| purchaseTime | datetime when invoice was paid, format: dd.MM.yyyy HH24:MI:ss, eg. 24.06.2015 14:45:57 |
| payerMsisdn | MSISDN of payer if issuer requested it |
| payerFirstName | first name of payer if issuer requested delivery address of payer |
| payerLastName | last name of payer if issuer requested delivery address of payer |
| payerStreet | street of payer if issuer requested delivery address of payer |
| payerCity | city of payer if issuer requested delivery address of payer |
| payerZip | ZIP code of payer if issuer requested delivery address of payer |
| payerCountry | country code of payer if issuer requested delivery address of payer |
|--|---|

<b>sample createPurchase response</b>

SEQR Invoice Service doesn't expect any specific JSON response.
It bases on HTTP status codes. HTTP 200 code for result and any other for FAILURE of nofitication delivery.
At this moment SEQR Invoice Service sends notifications synchronously imidiately after customer's payment. 




