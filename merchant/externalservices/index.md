---
layout: default
title: SEQR External Service Payment
description: SEQR Merchant, webshop, Service integration
---


## SEQR payment in your Service

This section describes how to use SEQR as the payment method for your service.

### Overview

When using SEQR as the payment method for your service, you need to integrate your solution with SEQR. 
This integration is based upon the normal SEQR payment flow, which is described in [First SEQR payment](/merchant/payment).

The following sequence diagram describes how the integration is performed:

<img src="/assets/images/Service_flow_140108.png" />

### Steps to take when integrating with SEQR


1. Create your QR codes for scanning
2. Create a web frontend
3. Create a web backend
4. Go live!


### 1. Create your QR codes for scanning

The QR-code that you should use in your service must adapt to a specific pattern.
Your service must support and create all URLs to integrate with SEQR system. To be able to launch SEQR app for paying the bill, use the schemes in the table below to create URLs. 
By either doing a redirect or letting the user click on a link to that URL, SEQR app will be triggered and intercepted according to the hierarchical part of the URL.
The 'service ID' must be agreed with SEQR, since it will be used in the SEQR system to identify your service.


### 2. Create a web frontend

Since your service will be integrated in the SEQR app, it must implement 4 URLs that the SEQR app needs to be able to access.

**Order URL**

Accessed by the app using an HTTP GET request on the Order URL. The page hosted on this URL is supposed to issue the Payment request to SEQR server upon the choice of the user. 

Example URL:
http://url/order#TOKEN

|--- | --- |
|  URL part | Description |
|--- | --- |
| http://url | Domain of the service system. |
| /order | Path to page for URL type “order”. |
| TOKEN | The key to get customer information (i.e. msisdn and subscriberKey) using getClientSessionInfo. |
| --- | --- |


**Success URL** 

When payment is processed and it is completed successfully, SEQR app brings up the page on this success URL. This URL is accessed using HTTP GET request by SEQR app. 
Example URL:
http://url/success#TOKEN

|--- | --- |
|  URL part | Description |
|--- | --- |
| http://url | Domain of the service system. |
| /success | Path to page for URL type “success”. |
| TOKEN | The key to get customer information (i.e. msisdn and subscriberKey) using getClientSessionInfo. |
| --- | --- |


**Failure URL** 

When the payment is processed and it fails for any reason, SEQR app brings up the page on this failure URL. This URL is accessed using HTTP GET request by SEQR app. 
Example URL:
http://url/failure#TOKEN

|--- | --- |
|  URL part | Description |
|--- | --- |
| http://thirdparty.com | Domain of the service system. |
| /fail | Path to page for URL type “fail”. |
| TOKEN | The key to get customer information (i.e. msisdn and subscriberKey) using getClientSessionInfo. |
| --- | --- |


**Cancel URL** 

Should be provided by the service. When the payment is canceled by the user, SEQR app brings up the page on this cancel URL. This URL is accessed using HTTP GET request by SEQR app. 
Example URL:
http://url/cancel#TOKEN

|--- | --- |
|  URL part | Description |
|--- | --- |
| http://thirdparty.com | Domain of the service system. |
| /cancel | Path to page for URL type “cancel”. |
| TOKEN | The key to get customer information (i.e. msisdn and subscriberKey) using getClientSessionInfo. |
| --- | --- |


The functionality of the frontend is totally up to you own requirements, as long as it confirms to the follwing:

* Implement the 4 URL required by SEQR app
* Can forward the #TOKEN to the web backend
* Can trigger the Paymentflow in the app using the URL Schema
* Can trigger the backend to start sendInvoice request


### 3. Create a web backend

The purpose of the web backend is to serve your web frontend with necessary resources, and to handle communication with the SEQR backend.

The communication with the SEQR backend consists of the following:

* calling **getClientSessionInfo**, using the #TOKEN given by the app to the web frontend, in order to retrieve required customer data. Refer to the **getClientSessionInfo** request in the <a href="/merchant/reference/api.html">API</a> section.

* calling **sendInvoice**, with appropriate invoice information. Refer to the **sendInvoice** request in the <a href="/merchant/reference/api.html">API</a> section.

* calling **getPaymentStatus** and receiving status PAID, to ensure that SEQR backend can confirm that your system is aware of the payment being successful. Refer to the **getPaymentStatus** request in the <a href="/merchant/reference/api.html">API</a> section.

### 4. Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html) and receive the credentials to your service.



