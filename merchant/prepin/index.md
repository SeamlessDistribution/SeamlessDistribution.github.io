---
layout: default
title: Preliminary Payments
description: SEQR Merchant, webshop, POS integration
---

# SEQR preliminary payments

SEQR Preliminary Payment allows you to reserve some amount on customer's account for future payment when exact amount is unknown at the beginning of payment flow.

# Integration procedure

1. Implement the required methods.
2. Install test [mobile app](/app/).
3. Test your implementation against preliminary payment flow.
4. Introduce your implementation to your system.
5. Verify your integration.
6. Go live!

# Implement the required methods


The methods required in a basic integration are:

|--- | --- |
|  Method | Description |
|--- | --- |
| registerTerminal | Registers a new terminal in SEQR server (required in POS systems) |
| unregisterTerminal | Unregisters an already registered terminal (required in POS systems) |
| assignSeqrId | Assigns a SEQR ID to a terminal (required in POS systems) |
| sendInvoice | Sends an invoice to SEQR server |
| getPaymentStatus | Obtains status of a previously submitted invoice |
| updateInvoice | Updates an already sent invoice with new set of invoice rows or attributes |
| commitReservation | commits reservation with final amount to be taken from customer's account |
| cancelInvoice | Cancels an unpaid invoice (required in POS systems) |
| --- | --- |


For an extended integration, also these methods can be used:

|--- | --- |
|  Method | Description |
|--- | --- |
| refundPayment | Refunds a previous payment, partly or the whole sum |
| markTransactionPeriod | Marks the end of one and the beginning of a new transaction period; used in reporting |
| executeReport | Executes a report on SEQR server |
| --- | --- |


Main difference is to additionally implement commitReservation method.

Other differences are:

* in sendInvoice request paymentMode is RESERVATION_REQUIRED_PRELIMINARY_AMOUNT and you have to set commitReservationTimeout;
* when reservation is confirmed payment goes to RESERVED status;

# Flow diagram

<img src="/assets/images/prepin/prepinflow.jpeg" />


# Flow description

1. Merchant send sendInvoice request to SEQR backend.
2. If OK starts polling with getPaymentStatus requests. Payment status is ISSUED at this moment.
3. User scan QR code and confirm payment (or just confirm if SEQR app was open from merchant's app).
4. Merchant gets RESERVED in response to getPaymentStatus and stops polling.
5. After service/shopping is complete merchant update informations about order with updateInvoice request.
6. Merchant end payment flow with commitReservation request with final transaction amount.  