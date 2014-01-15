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

This sequence diagram illustrates how payment is done when integration has been performed:

<img src="/assets/images/service_sequence.png" />

### Steps to take when integrating with SEQR


1. Create your QR codes for scanning
2. Create a web frontend
3. Create a web backend
4. Go live!


### 1. Create your QR codes for scanning

The QR code that you should use in your service must adapt to a specific pattern. To be able to launch SEQR app for paying the bill, use the schemes in the table below to create URLs. 
By either doing a redirect or letting the user click on a link to that URL, SEQR app will be triggered and intercepted according to the hierarchical part of the URL.

The URL embedded within a QR code contains the pointer to the Service definition within the SEQR system, to trigger the app.

The 'service ID' must be agreed with SEQR, since it will be used in the SEQR system to identify your service.

The QR code can either be printed and to-be-scanned by app or it can be just the contents of the code (a link) that the app reads and understands without having to scan it. The SEQR system has defined various types of QR codes using different URLs.

Example of QR code URL with optional parameters:
HTTP://SEQR.SE/000/EXTERNAL_SERVICE_ID?parameter1=value1&parameter2=value2...

|--- | --- |
|  Item | Description |
|--- | --- |
| HTTP://SEQR.SE | Domain of the SEQR system. |
| 000 | Service routing key. Defines the type of URL to launch Service application. |
| parameters | Optional: These parameters in the URL are optional and can be sent to the interface without modification. These are particularly useful for the interface to identify different products etc. Naming convention is not imposed by SEQR server for these parameters. **Note that these parameters will be returned when calling getClientSessionInfo.** |
| --- | --- |

### 2. Create a web frontend

When integration your web frontend with the SEQR App, the following functions must be supported:
1)	Implement Service URLs called by the SEQR App.
2)	Implement URL Schemas to trigger SEQR App functionality.
3)	Communicate with Service Web Backend.

### Implement Service URLs
Since your service will be integrated in the SEQR app, it must implement 4 URLs that the SEQR app needs to be able to access.

When SEQR app scans the QR code (or reads the link), SEQR server resolves the code and provides the app with all the URLs it may need.

* Order URL - Accessed by the app using an HTTP GET request on the Order URL. The page hosted on this URL is supposed to issue the Payment request to SEQR server upon the choice of the user. 
Example URL: http://url/order#TOKEN



* Success URL - When payment is processed and it is completed successfully, SEQR app brings up the page on this success URL. This URL is accessed using HTTP GET request by SEQR app. 
Example URL: http://url/success#TOKEN



* Failure URL - When the payment is processed and it fails for any reason, SEQR app brings up the page on this failure URL. This URL is accessed using HTTP GET request by SEQR app. 
Example URL: http://url/failure#TOKEN



* Cancel URL - Should be provided by the service. When the payment is canceled by the user, SEQR app brings up the page on this cancel URL. This URL is accessed using HTTP GET request by SEQR app. 
Example URL: http://url/cancel#TOKEN



|--- | --- |
|  URL part | Description |
|--- | --- |
| http://url | Domain of the service system. |
| /order | Path to page for URL type “order”. |
| TOKEN | The key to get customer information (i.e. msisdn and subscriberKey) using getClientSessionInfo. |
| --- | --- |


### Implement URL schemas

Trigger the Paymentflow in the app using the URL Schema (same as above).


### Communicate with Service Backend

Can trigger the backend to start sendInvoice request once the customer has fulfilled the order section.



### 3. Create a Web Backend

The purpose of the web backend is to serve your web frontend with necessary resources, and to handle communication with SEQR backend.

The communication with SEQR backend consists of the following:

* calling **getClientSessionInfo**, using the #TOKEN given by the app to the web frontend, in order to retrieve required customer data. Refer to the **getClientSessionInfo** request in the <a href="/merchant/reference/api.html">API</a> section.

* calling **sendInvoice**, with appropriate invoice information. Refer to the **sendInvoice** request in the <a href="/merchant/reference/api.html">API</a> section.

* calling **getPaymentStatus** and receiving status PAID, to ensure that SEQR backend can confirm that your system is aware of the payment being successful. Refer to the **getPaymentStatus** request in the <a href="/merchant/reference/api.html">API</a> section.

### 4. Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html) and receive the credentials to your service.



