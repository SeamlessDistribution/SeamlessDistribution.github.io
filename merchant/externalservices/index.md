---
layout: default
title: SEQR External Service Payment
description: SEQR Merchant, webshop, Service integration
---


## SEQR payment in your Service

<img src="/assets/images/Service_flow.png" />

Follow these steps to configure your Service for integration with SEQR:

1. Create QR code URLs 
2. Create Notification URL (used instead of getPaymentStatus)
3. Go live!


### 1. Create QR code URLs

The Service must support and create all URLs to integrate with SEQR system. To be able to launch SEQR app for paying the invoice, use the schemes in the table below to create URLs. 
By either doing a redirect or letting the user click on a link to that URL, SEQR app will be triggered and intercepted according to the hierarchical part of the URL.

|--- | --- |
|  URL pattern | Description |
|--- | --- |
| SEQR://SEQR.SE/000<invoiceReference/
service ID> | Start the payment flow in the app for the invoice with reference defined by <invoiceReference> |
| SEQR-ACTION://WIZARD/CANCEL | Cancel the flow and return to the app. |
| --- | --- |

The QR code can either be printed and to-be-scanned by app or it can be just the contents of the code (a link) that the app reads and understands without having to scan it. The SEQR system has defined various types of QR codes using different URLs.
When SEQR app scans the QR code (or reads the link), SEQR server resolves the code and provides the app with all the URLs it may need. 
The URL embedded within a QR code contains the pointer to the Service definition within the SEQR system, to trigger the app. The Service definition in the QR code URL contains 4 URLs for the app to interact with, which are:

* Order URL
* Success URL 
* Failure URL
* Cancel URL

Format of QR code URL:
HTTP://SEQR.SE/000/EXTERNAL_SERVICE_ID 
Example of QR code URL with optional parameters:
HTTP://SEQR.SE/000/EXTERNAL_SERVICE_ID?parameter1=value1&parameter2=value2...

|--- | --- |
|  Item | Description |
|--- | --- |
| SEQR://SEQR.SE/ | Domain of the SEQR system. |
| 000 | Service routing key (may change soon!). Defines the type of URL to launch Service application. Payment Broker retrieves 4 URLs. |
| EXTERNAL_SERVICE_ID | Unique identifier of the Service. SEQR server locates the status and other information about the Service using this ID. |
| parameters | Optional: These parameters in the URL are optional and can be sent to the interface without modification. These are particularly useful for the interface to identify different products etc. Naming convention is not imposed by SEQR server for these parameters. Note that these parameters will be returned when calling getClientSessionInfo. |
| --- | --- |


**Order URL**


Accessed by the app using an HTTP GET request on the Order URL. The page hosted on this URL is supposed to issue the Payment request to SEQR server upon the choice of the user. 

Example URL:
http://url/order#TOKEN

|--- | --- |
|  URL part | Description |
|--- | --- |
| http://url | Domain of the Service system. |
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
| http://url | Domain of the Service system. |
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
| http://thirdparty.com | Domain of the Service system. |
| /fail | Path to page for URL type “fail”. |
| TOKEN | The key to get customer information (i.e. msisdn and subscriberKey) using getClientSessionInfo. |
| --- | --- |


**Cancel URL** 

Should be provided by the Service. When the payment is canceled by the user, SEQR app brings up the page on this cancel URL. This URL is accessed using HTTP GET request by SEQR app. 
Example URL:
http://url/cancel#TOKEN

|--- | --- |
|  URL part | Description |
|--- | --- |
| http://thirdparty.com | Domain of the Service system. |
| /cancel | Path to page for URL type “cancel”. |
| TOKEN | The key to get customer information (i.e. msisdn and subscriberKey) using getClientSessionInfo. |
| --- | --- |


### 2. Create Notification URL 
Once an order is issued, the Service must know whether the payment is approved by the user or if cancelled. 
As soon as the order is placed, Service must call getPaymentStatus, which may require several calls of getPaymentStatus until the payment is approved by SEQR user. This polling can be avoided by sending a notification URL as arameter to getPaymentStatus. 
SEQR server notifies payment status change using this URL, and Service must again query the payment status to see order state. SEQR server issues a post request for this URL supplying invoiceReference and clientInvoiceId as parameters. This notification URL is optional and it follows the fire and forget technique. There are no retries associated with this notification. 
Example URL:
http://thirdparty.com/paymentStateChanged?parameter1=value1&parameter2=value2
Description of the Notification URL:

|--- | --- |
|  URL part | Description |
|--- | --- |
| http://thirdparty.com | Domain of the Service system. |
| paymentStateChanged | Path of the call back handler. |
| parameters | These are the optional parameters which can be used by the third party to for any purpose. SEQR server simply returns them while issuing the notification request. Naming convention is not imposed by SEQR server for these parameters. |
| values | These are values associated with parameters. The values are returned un-changed. |
| --- | --- |


Along with HTTP GET parameters, SEQR server appends HTTP post parameters, which can be useful for Service.
Description of the Notification URL HTTP post parameters:

|--- | --- |
|  URL parameter | Description |
|--- | --- |
| invoiceReference | Unique identifier of the paid invoice. The invoice number does not change once issued by SEQR server. |
| clientInvoiceId | The invoice id provided by the third party service while calling sendInvoice function. |
| msisdn | The telephone number used to rout calls on the mobile network to the subscriber. |
| subscriberKey | Unique identifier of the subscriber within SEQR server. |
| --- | --- |


### 3. Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html) and receive the credentials to your Service.



