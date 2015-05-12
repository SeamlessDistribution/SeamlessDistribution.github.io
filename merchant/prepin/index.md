---
layout: default
title: Preliminary Payments
description: SEQR Merchant, webshop, POS integration
---

# SEQR preliminary payments

SEQR Preliminary Payment allows you to reserve some amount on customer's account for future payment when exact amount is unknown at the beginning of payment flow.

# Integration procedure

Integration procedure depends on what kind of system you are integrating with SEQR. Basically you can follow procedure for [webshop](/merchant/webshop/index.html), [POS](/merchant/pos/index.html) or [mobile app](/merchant/inapp/index.html).

# Implement the required methods

Just follow instructions for your kind of system where you can find which methods are required.

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