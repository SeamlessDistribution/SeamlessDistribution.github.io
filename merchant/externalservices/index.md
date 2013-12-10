---
layout: default
title: SEQR External Service Payment
description: SEQR Merchant, webshop, POS integration
---

<img src="/assets/images/cash_register_bw.png" align="right" width="200px"/>

## SEQR Payments in External Services


Follow these steps to configure your Service for integration with SEQR:

1. Create QR code URLs 
2. Create Notification URL (used instead of getPaymentStatus)
2. Create payment button
3. Go live!


### 1. Create QR code URLs

The Service must support and create all URLs to integrate with SEQR system. To be able to launch SEQR app for paying the invoice, use the schemes in the table below to create URLs. 
By either doing a redirect or letting the user click on a link to that URL, SEQR app will be triggered and intercepted according to the hierarchical part of the URL.

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



#### Order URL

Accessed by the app using an HTTP GET request on the Order URL. The page hosted on this URL is supposed to issue the Payment request to SEQR server upon the choice of the user. 

Example URL:
http://url/order#TOKEN


#### Success URL 
When payment is processed and it is completed successfully, SEQR app brings up the page on this success URL. This URL is accessed using HTTP GET request by SEQR app. 
Example URL:
http://url/success#TOKEN


#### Failure URL 
When the payment is processed and it fails for any reason, SEQR app brings up the page on this failure URL. This URL is accessed using HTTP GET request by SEQR app. 
Example URL:
http://url/failure#TOKEN


#### Cancel URL 
Should be provided by the Service. When the payment is canceled by the user, SEQR app brings up the page on this cancel URL. This URL is accessed using HTTP GET request by SEQR app. 
Example URL:
http://url/cancel#TOKEN


### 2. Create Notification URL 
Once an order is issued, the Service must know whether the payment is approved by the user or if cancelled. 
As soon as the order is placed, Service must call getPaymentStatus, which may require several calls of getPaymentStatus until the payment is approved by SEQR user. This polling can be avoided by sending a notification URL as arameter to getPaymentStatus. 
SEQR server notifies payment status change using this URL, and Service must again query the payment status to see order state. SEQR server issues a post request for this URL supplying invoiceReference and clientInvoiceId as parameters. This notification URL is optional and it follows the fire and forget technique. There are no retries associated with this notification. 
Example URL:
http://thirdparty.com/paymentStateChanged?parameter1=value1&parameter2=value2
Description of the Notification URL:






### 3. Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html) and receive the credentials to your Service.



