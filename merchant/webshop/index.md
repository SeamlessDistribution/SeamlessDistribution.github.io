---
layout: default
title: SEQR Webshop Payments
description: SEQR Merchant, webshop, POS integration
---


# SEQR payment in a Webshop

To integrate your webshop with SEQR, you need to add SEQR payment in your “Check out” process where your customer normally selects between payment methods. This is an example of a checkout that supports SEQR:

<img src="/assets/images/seqr_webshop.png" />

##[See a live demo!](http://devapi.seqr.com/seqr-webshop-sample/)


## Integration procedure

Follow these steps to integrate your webshop with SEQR:

1. Add API parameters
2. Add SEQR as payment in your webshop
2. Present the receipt
3. Verify your integration
4. Go live!

### Add API parameters

The flow for a webshop SEQR payment is very similar to [Basic SEQR
payment](/merchant/payment), with the **sendInvoice** request.
The difference is that polling for payment status is handled by a payment view,
which also handles showing the QR code to the SEQR user. You still need to request
the status of the payment after the payment view returns, but only once to find
out the final status of the invoice.

The methods required in a basic integration are:

|--- | --- |
|  Method | Description |
|--- | --- |
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
| submitPaymentReceipt | Sends the receipt document of a payment |
| executeReport | Executes a report on SEQR server |
| --- | --- |


Refer to section [API](/merchant/reference/api.html) for detailed description.


### Add SEQR as payment in your webshop  

#### 1. Integrate the payment view
There are two payment views that you can choose from, standard payment view and small payment view:

#### Standard Payment View
<img src="/assets/images/paymentview-standard.png" />

#### Small Payment View
<img src="/assets/images/paymentview-small.png" />

#### Payment View - When SEQR doesn't support the user's phone
<img src="/assets/images/paymentview-nosupport.png" width="50%"/>

As an example, to integrate with SEQR, insert the following script tag into your checkout
page. The script will insert SEQR payment views at the same location. When running in production you only need to implement REST calls for sending invoices, getting payment status, and updating the payment receipt. For an example REST service you can see our [PHP example on github](https://github.com/SeamlessDistribution/seqr-webshop-api).

{% highlight html %}
<script
 id="seqrShop"
 src="http://devapi.seqr.com/seqr-webshop-plugin/js/seqrShop.js#!invoiceReference=[invoiceReference]">
</script>
{% endhighlight %}

#### View parameters 

| Name             | Description | Values | Default |
|------------------|-----------|---------|-----|
| invoiceReference | (required) invoice reference that you received from sendInvoice request | - | - |
| layout           | (optional) layout for the payment view | standard, small | standard |
| language         | (optional) language for texts in payment view | en, sv, ... | detected from browser, falls back to English if not available |
| paidCallback     | (optional) this javascript method is invoked after the payment is successful | - | - |

**Note:** when your webshop is browsed on mobile phones, you provide the backUrl in
 **sendInvoice** request. After a successful/cancelled payment, the app will redirect
the SEQR user to the URL specified in the invoice.


#### 2. Get payment status

Once the payment is completed, your webshop should query the status of the invoice
from SEQR by calling **getPaymentStatus**. 

**Note!** The web server must check the status each second, to verify that payment is completed. Otherwise SEQR server does not receive any notification that transaction is finalized and the payment will then be reversed!
This request should be triggered from a javascript timer on the website, so when SEQR user closes the window or moves away from the payment page, the polling stops. Another benefit is that you do not need to have a polling-loop on your backend, which will improve your webshop’s server performance.


### Present the receipt

If the invoice was successfully paid, a reference number (ersReference) is obtained from 
SEQR. Save the reference number for follow-ups and for print on the SEQR user's 
online confirmation receipt.

### Verify your integration

Verify that your integration works and run validation tests towards SEQR servers. [Contact](/contact) Seamless for more information. 

### Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html).

# Common use cases

## Use Case 1: SEQR purchase using browser

<div class="diagram">
@startuml

scale 650 width
skinparam monochrome true
autonumber

== Sample Web Shop ==

actor Customer as "Customer"
participant App as "App"
participant Browser as "Browser"
participant WebServer as "Web Server"
participant Backend as "SEQR"

Customer->Browser: Open shop page
Browser->WebServer: GET /shop
WebServer-->Browser: Shop page

Customer->Browser: Add item to cart
Browser->WebServer: POST /shop/additem
WebServer-->Browser: Updated page

Customer->Browser: Go to checkout with SEQR
Browser->WebServer: GET /shop/checkout

== SEQR Payment ==

WebServer->Backend: sendInvoice
Backend-->WebServer: Invoice Reference
WebServer-->Browser: Checkout page \nwith QR code
activate Browser
Browser->Browser: Wait for\npayment status
activate Browser
Browser->WebServer: GET /seqr/status

Customer->App: Start SEQR App
activate App
Customer->App: Press 'Tap here to scan'
App -> App: Start Camera
activate App
App ->Browser: << Scan QR code >>
Browser --> App: Invoice Reference
deactivate App

App->Backend: Fetch invoice
Backend-->App: Invoice
App -> App: Show invoice details
activate App
Customer->App: Press 'confirm'
deactivate App

App -> App: Show PIN dialog
activate App
Customer->App: Enter PIN code
App->Backend: Pay invoice
Backend-->App: Receipt
deactivate App
App -> App: Show payment confirmation
deactivate App

Backend-->WebServer: POST [notificationUrl]
WebServer->Backend: getPaymentStatus
Backend-->WebServer: PAID
WebServer-->Browser: Payment done
deactivate Browser
Browser-->WebServer: GET /shop/done
deactivate Browser
WebServer->Browser: Receipt page

@enduml
</div>

### Step 9. sendInvoice

The notificationUrl parameter is mandatory. It should contain a session id or token that enables the web server to map payment status back to a customer's session in step 31.

### Step 11. Checkout page with QR code

The QR code is using the following URL: HTTP://SEQR.SE/R[Invoice Reference]

### Step 12. GET /seqr/status

At this point the browser should start waiting for a payment status update. Ideally the browser should open a websocket over which it can receive the update. If websockets are not available a fallback to polling is required.

### Step 29. getPaymentStatus

Payment status must called immediately when the notificationUrl is called. Failing to call payment status will cause the payment to be cancelled, resulting in an SMS being sent to the customer.

### Step 31. Payment done

The customer's session must be updated with the payment status from step 30. This payment status is returned to the web browser using the mechanism from step 12.

## Use Case 2: SEQR purchase using mobile browser

<div class="diagram">
@startuml

scale 650 width
skinparam monochrome true
autonumber

== Sample Web Shop ==

actor Customer as "Customer"
participant App as "App"
participant Browser as "Mobile Browser"
participant WebServer as "Web Server"
participant Backend as "SEQR"

Customer->Browser: Open shop page
Browser->WebServer: GET /shop
WebServer-->Browser: Shop page

Customer->Browser: Add item to cart
Browser->WebServer: POST /shop/additem
WebServer-->Browser: Updated page

Customer->Browser: Go to checkout with SEQR
Browser->WebServer: GET /shop/checkout

== SEQR Payment ==

WebServer->Backend: sendInvoice
Backend-->WebServer: Invoice Reference
WebServer-->Browser: Checkout page \nwith SEQR link

Customer->Browser: Click SEQR link
Browser->App: Start SEQR App

activate App
App->Backend: Fetch invoice
Backend-->App: Invoice
App -> App: Show invoice details
activate App
Customer->App: Press 'confirm'
deactivate App

App->App: Show PIN dialog
activate App
Customer->App: Enter PIN code
App->Backend: Pay invoice
Backend-->App: Receipt

Backend-->WebServer: POST [notificationUrl]
WebServer->Backend: getPaymentStatus
Backend-->WebServer: PAID

deactivate App
App->App: Show payment confirmation
Customer->App: Press 'OK'
App->Browser: Open backURL

deactivate App

Browser-> WebServer: GET [backURL]
WebServer->Browser: Receipt page

@enduml
</div>

### Step 9. sendInvoice

A backURL parameter is optional. If it is provided the SEQR application will load the URL in a browser when the customer has confirmed payment (step 27).

### Step 27. Open backURL

This step is only triggered is a backURL was provided in the cal to sendInvoice (step 9).

### Step 23. getPaymentStatus

Payment status must called immediately when the notificationUrl is called. Failing to call payment status will cause the payment to be cancelled, resulting in an SMS being sent to the customer. The response in step 24 should be stored in the customer's session so that it can be displayed in the page that the backURL loads in step 28.
