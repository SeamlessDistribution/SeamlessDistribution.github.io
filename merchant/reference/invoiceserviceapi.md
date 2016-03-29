---
layout: default
title: SEQR Invoice Service
description: SEQR Invoice Service API
---

# SEQR Invoice Service API

At this point our SEQR Invoice Service API is based on one REST method  -  which is required to be exposed by invoice issuer.

# Notification Service

Issuer is expected to expose a URL which will be called by SEQR Invoice service using HTTP POST with JSON payload about an invoice which has just been paid. The description of JSON request payload is presented in a table below:

|---|---|---|
| Parameter name | Description |
|---|---|---|
| invoiceId | Unique identifier of an invoice in SEQR Invoice service. |
|---|---|---|

### Request example:

{% highlight python %}
	{"invoiceId": 25153}
{% endhighlight %}

That id can be used to fetch invoice from our system. It may be fetched from following url:

{% highlight python %}
	https://<host_name>/api/invoice/<id>?issuer=<issuer_name>
{% endhighlight %}

With following headers:

|---|---|---|
| Header | Content |
|---|---|---|
| X-AUTH-TOKEN | sha256 sum of issuer name concatenated with issuer secret. |
| Accept | application/json |
|---|---|---|

Query param 'issuer' and X-AUTH-TOKEN are required for authentication. It is impossible to fetch an invoice from another issuer.

Payload of the response details below. Please notice that the same information is available in a report which can be fetched by an issuer on demand.

### Response example:

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
| Parameter | Description |
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

### Notification retries

When notifying issuer about new invoice SEQR Invoice requires http response code to be 200. In case of problems with connection or issuer's system malfunction and response other than 200 it will retry several times. First 3 attempts are made right after invoice is paid with about 10 seconds delays. Than retries are scheduled with growing delay length starting from 1 minute, then 3:45, 7:30, 15, 30 minutes and so on (length is two times longer than in previous attempt). It schedules notification 10 times rising delay to 16h in last attempt. This gives around 32h total to deal with any problem regarding notification receiving on issuer's side.
<br>




