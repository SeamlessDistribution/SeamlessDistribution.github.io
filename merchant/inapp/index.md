---
layout: default
title: SEQR In-app Payments
description: SEQR Merchant, webshop, POS, service, in-app integration
---


# SEQR payment in your app 

To integrate your app with SEQR, you need to add SEQR payment in your “Check out” process where your customer normally selects between payment methods. 

All apps offering payments typically have a backend that handles the actual service/product that is sold. It is this backend that must connect to SEQR using our interface, and the communication between your app and your backend is up to your app developer.

## Example of shopping and payment flow in your app and SEQR app

<img src="/assets/images/appshop/total_flow.png" />


## Integration procedure

Follow these steps to integrate your app with SEQR:

1. Add API parameters
2. Insert the payment URL
3. Present the receipt
4. Verify your integration
4. Go live!

### Add API parameters

The flow for an app SEQR payment is very similar to [Basic SEQR payment](/merchant/payment).
The difference is that the user presses a "pay" button or link in your app, which launches the SEQR app and presents the bill for the user to confirm the payment.
You still need to request the status of the payment after your app returns (with backURL), but only once to find out the final status of the invoice.


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


### Insert the payment URL

Make a redirection (button or link) in your app, which launches the SEQR app, using the QR code URL returned from the sendInvoice request: Replace the "HTTP:" header with "SEQR:"; that is, if sendInvoice returns HTTP://SEQR.SE/R12345, the button/link should instead use SEQR://SEQR.SE/R12345.


**Note:** When your app shop is browsed, you provide the backURL in the
 sendInvoice request. After a successful/cancelled payment, the app will redirect the SEQR user to the URL specified in sendInvoice. Typically this will be a URL with a URL scheme that will launch the calling app again.

**Note2:** The invoice status will still be "ISSUED" even if the customer press cancel in the SEQR-app. The backURL will still be called and you should therefore treat "ISSUED" as canceld if you the status is still "ISSUED" after you receive a notice on your provided backURL.

### Present the receipt

Once the payment is completed, your app should query the status of the invoice from SEQR by calling getPaymentStatus. If the invoice was successfully paid, a reference number (ersReference) is obtained from 
SEQR. Save the reference number for follow-ups and for print on the user 
online confirmation receipt.

### Verify your integration

Verify that your integration works and run validation tests towards SEQR servers. [Contact](/contact) Seamless for more information.

### Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html).
