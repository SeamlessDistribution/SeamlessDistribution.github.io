---
layout: default
title: SEQR Merchant API
description: API reference
---

# Payment API / WSDL

For test purpose we use this [WSDL](http://extdev4.seqr.se/extclientproxy/service/v2?wsdl).
For complete details, refer to the [API documentation](/downloads/ersifextclient-2.4.2.1-manual-SEQR.pdf)
and to the [javadoc](/downloads/ersifextclient-2.4.2.1-javadoc/). 

## Methods for payments

<table>
   <tbody>
      <tr>
         <th>Method</th>
         <th>Description</th>
      </tr>
      <tr>
         <td>
            sendInvoice
            <ul>
               <li>ClientContext context</li>
               <li>Invoice invoice</li>
               <li>
                  List
                  <customertoken> tokens</customertoken>
               </li>
            </ul>
         </td>
         <td>Sends an invoice to the SEQR service. Tokens are optional and only for loyalty.
         </td>
      </tr>
      <tr>
         <td>
            updateInvoice
            <ul>
               <li>ClientContext context</li>
               <li>Invoice invoice</li>
               <li>
                  List
                  <customertoken> tokens</customertoken>
               </li>
            </ul>
         </td>
         <td>Updates an already sent invoice with new set of invoice rows and amount; used in loyalty.
         </td>
      </tr>
      <tr>
         <td>
            getPaymentStatus
            <ul>
               <li>ClientContext context</li>
               <li>String invoiceReference</li>
               <li>int invoiceVersion</li>
            </ul>
         </td>
         <td>Obtains status of a previously submitted invoice
         </td>
      </tr>
      <tr>
         <td>
            cancelInvoice
            <ul>
               <li>ClientContext context</li>
               <li>String invoiceReference</li>
            </ul>
         </td>
         <td>Cancels an unpaid invoice
         </td>
      </tr>
      <tr>
         <td>
            commitReservation
            <ul>
               <li>ClientContext context</li>
               <li>String invoiceReference</li>
            </ul>
         </td>
         <td>Commits a payment, if a payment reservation successfully executed.
            We are working on support for reservations in cooperation with more banks.
         </td>
      </tr>
      <tr>
         <td>
            submitPaymentReceipt
            <ul>
               <li>ClientContext context</li>
               <li>String ersReferenc</li>
               <li>ReceiptDocument receiptDocument</li>
            </ul>
         </td>
         <td>
            Used to confirm that the payment was received by the cashregister. 
            Adds an optional receipt document to a payment or refund.
         </td>
      </tr>
      <tr>
         <td>
            refundPayment
            <ul>
               <li>ClientContext context</li>
               <li>String ersReference</li>
               <li>Invoice invoice</li>
            </ul>
         </td>
         <td>Refunds a previous payment (Available in production from 2014)
         </td>
      </tr>
   </tbody>
</table>


### Methods specific for POS (terminal) registration 


|--- | --- |
|  Method | Description |
|--- | --- |
| registerTerminal | Registers a new terminal in the SEQR service |
| unRegisterTerminal | Unregisters an already registered terminal |
| assignSeqrId | Assigns a SEQR ID to a terminal |
| --- | --- |

### Methods for reconciliation and reporting 


|--- | --- |
|  Method | Description |
|--- | --- |
| markTransactionPeriod | Marks the end of one and the beginning of a new transaction period; used in reporting |
| executeReport | Executes a report on the SEQR service |
| --- | --- |



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


| Field | Description |
| --- | --- |
| acknowledgementMode | Needs to be set to NO_ACKNOWLEDGMENT unless you provide loyalty flow |
| backURL | used in app-to-app or web shopping |
| cashierId | "Alice" will show on receipt |
| clientInvoiceId | Your purchase reference |
| footer | receipt footer text |
| invoiceRows | See invoiceRow description |
| issueDate | cashregsister Date  |
| notificationURL | optional notification/confirmation url |
| paymentMode | use IMMEDIATE_DEBIT as RESERVATION_DESIRED/RESERVATION_REQUIRED are limited in use  |
| title | title displayed on bill and receipt |
| totalAmount | full amount of invoice/bill |


## InvoiceRow data 


Used to present the payment in the app. 


| Field | Description |
| --- | --- |
| itemDescription | optional |
| itemDiscount | optional |
| itemEAN | optional |
| itemQuantity | should be 1 or more |
| itemTaxRate | optional VAT line like "0.25" |
| itemTotalAmount | required total amount for this row |
| itemUnit | optional "dl" |
| itemUnitPrice | optional  |


## sendInvoice response fields


| Field | Description |
| --- | --- |
| ersReference | Not used by this method (will be null after this method). |
| resultCode | Request result code |
| invoiceQRCode | SEQR generated QR Code (used for webshops; not relevant for cash registers) |
| resultDescription | A textual description of resultCode  |
|invoiceReference  | The SEQR service reference to the registered invoice. |

## sendInvoice SOAP examples
To be added!


## updateInvoice request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| invoice | Invoice data, which contains the amount and other invoice information |
| invoiceReference | The SEQR service reference to the registered invoice. |
| tokens | The customer tokens applied to this invoice. |


## updateInvoice response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## updateInvoice SOAP examples
To be added!


## getPaymentStatus request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| invoiceReference | The SEQR service reference to the registered invoice. |
| invoiceVersion | Version of the invoice. The first time that it uses getPaymentStatus method the client sets the invoiceVersion to zero. The SEQR service increments the invoiceVersion in responce message when: the state of the payment (invoiceStatus) changes, or, a new buyer token is provided to be considered in the invoice. In subsequent uses of the getPaymentStatus method, the client must use the latest value of invoiceVersion as an acknowledgement that it has received the latest change. |


## getPaymentStatus response fields


| Field | Description |
| --- | --- |
| ersReference | The unique reference generated by the SEQR service once the invoice has been paid (null for all other invoiceStatus than PAID invoice has been paid). |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| invoiceStatus | Status of the invoice: 0 - Pending usage (when sent from SEQR), ISSUED - Invoice is issued, and waiting for payment, PAID Invoice is paid, PARTIALLY_PAID - Invoice is partially paid, PENDING_ISSUER_ACKNOWLEDGE - Payment is updated and waiting for issuer acknowledgement, CANCELED - Invoice is canceled, FAILED - Invoice payment has failed, RESERVED - The invoice amount is reserved |
| customerTokens | List of customer tokens relevant for this payment |
| deliveryAddress | If the payment should be delivered automatically, this contains the delivery address to deliver to |
| resultCode | Receipt of the payment, if the status is PAID |


## getPaymentStatus SOAP examples
To be added!


## cancelInvoice request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| invoiceReference | Reference of the invoice to be canceled. |


## cancelInvoice response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## cancelInvoice SOAP examples
To be added!


## registerTerminal request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| externalTerminalId | The identifier of the terminal in the client system, e.g. "Store 111/Till 4". |
| password | Password for future communications with the SEQR service. |
| name | The name to appear on the buyer’s mobile device, e.g. "My Restaurant, cash register 2". |


## registerTerminal response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| terminalId | The newly generated unique identifier for this terminal. This identifier should be used in future communications of this terminal towards the SEQR service. |


## registerTerminal SOAP examples
To be added!


## unregisterTerminal request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| TerminalId | The SEQR ID of the terminal to be unregistered. |


## unregisterTerminal response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## unregisterTerminal SOAP examples
To be added!


## assignSeqrId request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| SeqrId | The SEQR ID of the terminal. |


## assignSeqrId response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## assignSeqrId SOAP examples
To be added!


## commitReservation request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| invoiceReference | Reference of the invoice that is reserved. |


## commitReservation response fields


| Field | Description |
| --- | --- |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## commitReservation SOAP examples
To be added!


## submitPaymentReciept request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| ersReference | Reference of the payment for which the receipt is applicable. |
| receiptDocument | Receipt document, containing the full details of the receipt. NOTES Preferably in ARTS Receipt XML format. |


## submitPaymentReceipt response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## submitPaymentReceipt SOAP examples
To be added!


## refundPayment request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| ersReference | Reference of the payment to be refunded. |
| invoice | Invoice data, which contains the amount and other invoice information after products has been removed from the original invoice. |


## refundPayment response fields


| Field | Description |
| --- | --- |
| ersReference | The reference of the refund. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## refundPayment SOAP examples
To be added!



## markTransactionPeriod request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| parameters | Optional parameters that can be used in processing the request. |


## markTransactionPeriod response fields


| Field | Description |
| --- | --- |
| ersReference | The reference to this operation. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## markTransationPeriod SOAP examples
To be added!



## executeReport request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| reportId | The identifier of the report that should be executed/produced. |
| language | The report language (null if the default language is to be used). |
| parameters | Optional parameters that can be used in processing the request. |


## executeReport response fields


| Field | Description |
| --- | --- |
| ersReference | The reference to this operation. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| report | The executed/produced report, in binary and plain text form, if available. |


## executeReport SOAP examples
To be added!














