---
layout: default
title: SEQR External Service Payment
description: SEQR Merchant, webshop, Service integration
---


# SEQR payment in your Service

To use SEQR as the payment method for your service, you need to integrate your own service into the SEQR app.

This integration description is based upon the normal SEQR payment flow, refer to [Basic SEQR payment](/merchant/payment).

When integration has been performed, SEQR payment is performed according to this sequence diagram:


<img src="/assets/images/service_sequence.png" />

## Integration procedure

Follow these steps to integrate your service with SEQR:


1. Add API parameters
2. Create your QR codes for scanning
3. Create a web frontend to be integrated into SEQR app
4. Create a web backend
5. Verify your integration
6. Go live!


### Add API parameters

The methods required in a basic integration are:

|--- | --- |
|  Method | Description |
|--- | --- |
| getClientSessionInfo | Retrieves customer information |
| sendInvoice | Sends an invoice to SEQR server |
| getPaymentStatus | Obtains status of a previously submitted invoice |
| markTransactionPeriod | Marks the end of one and the beginning of a new transaction period; used in reporting |
| --- | --- |



For an extended integration, also these methods can be used:

|--- | --- |
|  Method | Description |
|--- | --- |
| updateInvoice | Updates an already sent invoice with new set of invoice rows or attributes |
| cancelInvoice | Cancels an unpaid invoice |
| commitReservation | Commits a payment |
| submitPaymentReceipt | Sends the receipt document of a payment |
| executeReport | Executes a report on SEQR server |
| --- | --- |


Refer to section [API](/merchant/reference/api.html) for detailed description.

### Create your QR codes for scanning

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
| parameters | Optional: These parameters in the URL are optional and can be sent to the interface without modification. These are particularly useful for the interface to identify different products etc. Naming convention is not imposed by SEQR server for these parameters. **Note** that these parameters will be returned when calling getClientSessionInfo. |
| --- | --- |

### Create a web frontend to be integrated into SEQR app

When integrating your web frontend with the SEQR app, the following functions must be supported:

1. Implement Service URLs called by SEQR app
2. Implement URL schemas to trigger SEQR app functionality
3. Implement design requirements
4. Communicate with Service web backend


#### Implement Service URLs
Since your service will be integrated in the SEQR app, it must implement 4 URLs that SEQR app needs to be able to access.

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


#### Implement URL schemas that trigger the app

The SEQR app is triggered by URLs using the specific SEQR URI schemes SEQR:// and SEQR-ACTION://. By constructing URLs using these schemes and either doing a redirect or letting the user click on a link to that URL, the app will be triggered and intercept according to the hierarchical part of the URL.

|--- | --- |
|  Trigger URLs | Description |
|--- | --- |
| SEQR://SEQR.SE/R< invoiceReference > | Start the payment flow in the app for the invoice with reference. |
| SEQR-ACTION://WIZARD/CANCEL | Cancel the external service flow and return to SEQR app. |
| --- | --- |


#### Implement design requirements 

* Any important information such as booking numbers/reference codes etc. must be sent to the user via an sms or be visible in the receipt. This is to avoid that any important information gets lost in case of connection issues. 

* If the service includes more than one view before the SEQR payment process, you must provide a way for the user to navigate, for example with a back button.

Consider these aspects of Android and iOS systems when creating your service:

__Navigation:__

* Android devices often have a physical back button, which the user can use to navigate back through your service.

* On iPhone, such behavior needs to be put in the service itself, since no physical back button exists.

__Display size and resolution:__

* SEQR supports Android devices with the screen size from 320x480px to 800-1280px. Examples are Sony Experia Mini and Samsung Galaxy. Note that your service must work with all the sizes.

* SEQR supports iOS devices with resolutions 320x480px, 640x960px and 640x1136px. For iOS you need to consider support for Retina resolution, meaning that your graphics must be double the size displayed.


#### Communicate with Service backend

The web frontend calls the service backend, which will send a sendInvoice request back to the SEQR system, once the customer has fulfilled the order section.



### Create a web backend

The purpose of the web backend is to serve your web frontend with necessary resources, and to handle communication with SEQR backend.

The communication with SEQR backend consists of the following:

* calling **getClientSessionInfo**, using the #TOKEN given by the app to the web frontend, in order to retrieve required customer data. Refer to the **getClientSessionInfo** request in the <a href="/merchant/reference/api.html">API</a> section.

* calling **sendInvoice**, with appropriate invoice information. Refer to the **sendInvoice** request in the <a href="/merchant/reference/api.html">API</a> section.

* calling **getPaymentStatus** and receiving status PAID, to ensure that SEQR backend can confirm that your system is aware of the payment being successful. Refer to the **getPaymentStatus** request in the <a href="/merchant/reference/api.html">API</a> section.

### Verify your integration

To verify that your integration works you can sign up to SEQR servers and run validation tests. [contact](/contact) Seamless for login credentials.

### Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html) and receive the credentials to your service.



