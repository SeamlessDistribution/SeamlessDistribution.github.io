---
layout: default
title: SEQR In-app Payments
description: How to integrate with your website
---

# Webshop Integration

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
