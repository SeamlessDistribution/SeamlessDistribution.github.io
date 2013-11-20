---
layout: default
title: SEQR Merchant API
description: API reference
---

# Payment API / WSDL

For test purpose we use this [WSDL](http://extdev4.seqr.se/extclientproxy/service/v2?wsdl) 
that has the following methods: 

## Methods used for webshop integration 

<table>
<tr><th>Method</th><th>Description</th></tr>
<tr><td>sendInvoice</td>
    <td>Sends an invoice to the SEQR service </td></tr>
<tr><td>updateInvoice</td>
    <td>Updates an already sent invoice with new set of invoice rows or attributes (e.g. total invoice amount); used also to support loyalty programme</td></tr>
<tr><td>getPaymentStatus</td>
     <td>Obtains status of a previously submitted invoice</td></tr>
<tr><td>cancelInvoice</td>
    <td>Cancels an unpaid invoice</td></tr>
<tr><td>commitReservation</td>
    <td>Commits a payment</td></tr>
<tr><td>submitPaymentReceipt</td>
    <td>Sends the receipt document of a payment or refund</td></tr>
<tr><td>refundPayment</td>
    <td>Refunds a previous payment</td></tr>
<tr><td>markTransactionPeriod</td>
    <td>Marks the end of one and the beginning of a new transaction period; used in reporting</td></tr>
<tr><td>executeReport</td>
    <td>Executes a report on the SEQR service.</td></tr>
</table>

## Context parameter used in all calls

A principal is the main actor in each request to the SEQR service and represents either a seller or a buyer. Each request has at least an initiator principal.
The ClientContext structure is used in all requests to identify, authenticate and authorize the client initiating the transaction. For authentication the credentials of the initiator principal are used. As all transactions take place over a secure channel (typically HTTPS) the ClientContext is sent in clear text.

<table>
<tr><th>ClientContext fields</th><th>Description</th></tr>
<tr><td>clientId </td>
    <td> Client id identifies the software with which the SEQR service is communicating, for example “CashRegisterManager version 1.3.4.</td></tr>
<tr><td>channel </td>
    <td> The channel used to send a request. Always use ClientWS or WS. </td></tr>
<tr><td>clientRequestTimeout </td>
    <td> The client side timeout for the request. If the response is not received before the timeout the client will attempt to abort the request. Must be set to 0, so there will not be any client forced timeouts in the SEQR service. </td></tr>
<tr><td>initiatorPrincipalId </td>
    <td> Used for authentication of the principal and contains the id and type, as well as an optional user id. </td></tr>
</table>

Recommended: Use TERMINALID as type and the user that has been given to you by Customer Service.
password
The password used to authenticate the initiator principal.
clientReference
The client reference for the transaction. 
Recommended: the clientReference should be unique at least for the specific client id.
Note: SEQR service does not check this field. The field has a maximum length of 32 characters. The field is mandatory for troubleshooting purposes.
clientComment
Client comment included within the request. The field is optional.
Payment and loyalty membership
Payment is created with the following calls: 
sendInvoice - Sends an invoice to SEQR service.
updateInvoice - Updates an already sent invoice with new set of invoice rows or attributes, for example loyalty.
cancelInvoice - Cancels an unpaid invoice.
getPaymentStatus - Obtains status of a previously submitted invoice. When fetching the payment status, SEQR may communicate a set of customer tokens to the merchant that are applicable for the payment. The merchant must then decide which tokens are applied (such as for loyalty) and send them back with the updateInvoice call.
commitReservation - Commits the payment for an invoice that is in RESERVED state.
submitPaymentReceipt - Sends a receipt for a payment or refund which is shown on the buyer’s mobile device.
refundPayment - Refunds a previous payment. 
For complete details, refer to the API documentation, and for information on configuration for webshop, refer to sections Create QR code and Get payment status.
Parameter
Description
context
Used in all requests. The ClientContext object.
resultCode
Response from all requests. Request result code.
resultDescription
Response from all requests. A textual description of resultCode.
invoice
sendInvoice and updateInvoice request. Invoice data, which contains the amount and other invoice information.
refundPayment request: contains the data after products have been removed from original invoice.
invoiceReference
sendInvoice response. The SEQR service reference to the registered invoice.
updateInvoice, cancelInvoice, getPaymentStatus and commitReservation requests. The SEQR service reference to the registered invoice, or reference of invoice to be reserved or canceled.
invoiceQRCode
sendInvoice response. SEQR generated QR code.
tokens
updateInvoice request. The customer tokens applied to this invoice (in getPaymentStatus response). Can be used for loyalty membership, coupons, etc. The following parameters:
type
value; such as card value, coupon code
status; 0 (pending), 1 (used when updated by merchant), 90 (blocked) or 99 (invalid, unknown)
description
Note! The new token (e.g. name of loyalty card) must be added to SEQR system in advance.
invoiceVersion
getPaymentStatus request. Version of the invoice. The first time that it uses getPaymentStatus method the client sets the invoiceVersion to zero. The SEQR service increments the invoiceVersion in responce message when:
the state of the payment (invoiceStatus) changes,
or
new buyer token is provided to be considered in the invoice.
In subsequent uses of the getPaymentStatus method, the client must use the latest value of invoiceVersion as an acknowledgement that it has received the latest change.
ersReference
submitPaymentReceipt request: Reference of the payment for which the receipt is applicable.
refundPayment request: Reference of the payment to be refunded
getPaymentStatus response: The unique reference generated by the SEQR service once the invoice has been paid (null for all other invoiceStatus than PAID invoice has been paid).
receiptDocument
submitPaymentReceipt request: Receipt document, containing the full details of the receipt. Preferably in ARTS XML/HTML format
invoiceStatus
getPaymentStatus response. Status of the invoice:
0 - Pending usage (when sent from SEQR)
ISSUED - Invoice is issued, and waiting for payment
PAID Invoice is paid
PARTIALLY_PAID - Invoice is partially paid
PENDING_ISSUER_ACKNOWLEDGE – Payment is updated and waiting for issuer acknowledgement
CANCELED – Invoice is canceled
FAILED – Invoice payment has failed 
RESERVED – The invoice amount is reserved
Note! If getPaymentStatus is not queried, payment done by the customer will be refunded.
customerTokens
getPaymentStatus response. Metadata about invoice/payment. Customer tokens can be used for different purposes, loyalty memberships, coupons etc.
When fetching the payment status, SEQR may communicate a set of customer tokens to the merchant that are applicable for the payment. The merchant must then decide which tokens are applied and send them back with the updateInvoice call.
deliveryAddress
getPaymentStatus response.
receipt
getPaymentStatus response.

