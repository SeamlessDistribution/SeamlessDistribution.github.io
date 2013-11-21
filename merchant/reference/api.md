---
layout: default
title: SEQR Merchant API
description: API reference
---

# Payment API / WSDL

For test purpose we use this [WSDL](http://extdev4.seqr.se/extclientproxy/service/v2?wsdl).
For complete details, refer to the [API documentation](/downloads/ersifextclient-2.4.2.1-manual-SEQR.pdf)
and to the [javadoc](/downloads/ersifextclient-2.4.2.1-javadoc/). 

## Methods used for webshop integration 

<table>
<tr><th>Method</th><th>Description</th></tr>
<tr><td>sendInvoice</td>
    <td>Sends an invoice to the SEQR service 
        <li>ClientContext context</li>
        <li>Invoice invoice</li>
        <li>java.util.List<CustomerToken> tokens</li>
    </td></tr>
<tr><td>updateInvoice</td>
    <td>Updates an already sent invoice with new set of invoice rows or attributes (e.g. total invoice amount); used also to support loyalty
        <li>ClientContext context</li>
        <li>Invoice invoice</li>
        <li>java.util.List<CustomerToken> tokens</li>    
    </td></tr>
<tr><td>getPaymentStatus</td>
     <td>Obtains status of a previously submitted invoice
        <li>ClientContext context</li>
        <li>String invoiceReference</li>
        <li>int invoiceVersion</li>
     </td></tr>
<tr><td>cancelInvoice</td>
    <td>Cancels an unpaid invoice
        <li>ClientContext context</li>
        <li>String invoiceReference</li>
    </td></tr>
<tr><td>commitReservation</td>
    <td>Commits a payment, if a payment reservation successfully executed.
        We are working on support for reservations in cooperation with more banks
        <li>ClientContext context</li>
        <li>String invoiceReference</li>
    </td></tr>
<tr><td>submitPaymentReceipt</td>
    <td>Confirm that you have gotten a PAID response from getPaymentStatus, and adds an optional 
        receipt document to a payment or refund
        <li>ClientContext context</li>
        <li>String ersReferenc</li>
        <li>ReceiptDocument receiptDocument</li>
    </td></tr>
<tr><td>refundPayment</td>
    <td>Refunds a previous payment (Available in production from 2014)
        <li>ClientContext context</li>
        <li>java.lang.String ersReference</li>
        <li>Invoice invoice</li>
    </td></tr>
<tr><td>markTransactionPeriod</td>
    <td>Marks the end of one and the beginning of a new transaction period; used in reporting</td></tr>
<tr><td>executeReport</td>
    <td>Executes a report on the SEQR service</td></tr>
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
    <td> Used for authentication of the principal and contains the id and type, as well as an optional user id. 
         Use TERMINALID except when you regsister a new terminal, then you need RESELLERUSER (as provided from seamless). 
    </td></tr>
<tr><td>password</td>
    <td>The password used to authenticate the initiator principal.</td></tr>
<tr><td>clientReference </td>
    <td>The client reference for the transaction.
        Recommended: the clientReference should be unique at least for the specific client id.
        Note: SEQR service does not check this field. The field has a maximum length of 32 characters. 
        The field is mandatory for troubleshooting purposes.
    </td></tr>
<tr><td>clientComment </td>
    <td>Client comment included within the request. Optional.</td></tr>
</table>

## Invoice data 

Invoice is used in sending, updating and receiving status on a payment. What you need to set is: 

sendInvoice request fields

| Field | Description |
|Context | The ClientContext object |
|Invoice | Invoice data, which contains the amount and other invoice information. |
| --- | --- |

sendInvoice response fields
| Field | Description |
| ersReference | Not used by this method (will be null after this method). |
| resultCode | Request result code |
| invoiceQRCode | SEQR generated QR Code (used for webshops; not relevant for cash registers) |
| resultDescription | A textual description of resultCode  |
|invoiceReference  | The SEQR service reference to the registered invoice.

 |
updateInvoice request fields
| Field | Description |
| context | The ClientContext object |
| invoice | Invoice data, which contains the amount and other invoice information |
| invoiceReference | The SEQR service reference to the registered invoice. |
| tokens |The customer tokens applied to this invoice. |






