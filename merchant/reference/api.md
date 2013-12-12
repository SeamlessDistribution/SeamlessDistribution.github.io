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
         <td>Updates an already sent invoice with new set of invoice rows and amount or attributes, for example loyalty.
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
         <td>Obtains status of a previously submitted invoice. When fetching the payment status, SEQR may communicate a set of customer tokens to the merchant that are applicable for the payment. The merchant must then decide which tokens are applied (such as for loyalty) and send them back with the updateInvoice request.
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
               <li>String ersReference</li>
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




### Method for retrieving user information (valid for Service integration)


|--- | --- |
|  Method | Description |
|--- | --- |
| getClientSessionInfo | Retrieves user information |
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
         Use TERMINALID except when you regsister a new terminal, then you need RESELLERUSER (as provided from Seamless). 
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


## sendInvoice SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used by this method (will be null after this method). |
| resultCode | Request result code |
| invoiceQRCode | SEQR generated QR Code (used for webshops; not relevant for cash registers) |
| resultDescription | A textual description of resultCode  |
|invoiceReference  | The SEQR service reference to the registered invoice. |


## sendInvoice SOAP request example, for **Webshop** and **POS**

{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:sendInvoice>
       <context>
          <channel>extWS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>87e791f9e24148a6892c52aa85bb0331</id>
            <type>TERMINALID</type>
          </initiatorPrincipalId>
          <password>1234</password>
       </context>
       <invoice>
          <title>Some Invoice</title>
          <cashierId>Bob</cashierId>
          <totalAmount>
            <currency>SEK</currency>
            <value>10.22</value>
          </totalAmount>
       </invoice>
     </ext:sendInvoice>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## sendInvoice SOAP request example, for **Service**

{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:sendInvoice>
       <context>
          <channel>service</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>87e791f9e24148a6892c52aa85bb0331</id>
            <type>TERMINALID</type>
          </initiatorPrincipalId>
          <password>1234</password>
       </context>
       <invoice>
          <title>Some Invoice</title>
          <cashierId>Bob</cashierId>
          <totalAmount>
            <currency>SEK</currency>
            <value>10.22</value>
          </totalAmount>
          <notificationUrl>http://www.thirdparty.com/notifyMeHere</notificationUrl>
       </invoice>
     </ext:sendInvoice>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



## sendInvoice SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:sendInvoiceResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <invoiceQRCode>http://seqr.se/R1328543027208</invoiceQRCode>
            <invoiceReference>1328543027208</invoiceReference>
         </return>
      </ns2:sendInvoiceResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}




## updateInvoice SOAP request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| invoice | Invoice data, which contains the amount and other invoice information |
| invoiceReference | The SEQR service reference to the registered invoice. |
| tokens | The customer tokens applied to this invoice. Can be used for loyalty membership, coupons, etc. The following parameters:type,value (such as card value, coupon code, status (0 - pending, 1 - used when updated by merchant, 90 - blocked or 99 - invalid, unknown), description. **Note!** The new token (e.g. name of loyalty card) must be added to SEQR system in advance.
|


## updateInvoice SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## updateInvoice SOAP request example


{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:updateInvoice>
       <context>
          <channel>extWS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>87e791f9e24148a6892c52aa85bb0331</id>
            <type>TERMINALID</type>
          </initiatorPrincipalId>
          <password>1234</password>
       </context>
       <invoice>
          <title>Some Invoice</title>
          <cashierId>Bob</cashierId>
          <totalAmount>
            <currency>SEK</currency>
            <value>10.22</value>
          </totalAmount>
       </invoice>
     </ext:updateInvoice>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



## updateInvoice SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:updateInvoiceResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
         </return>
      </ns2:updateInvoiceResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



## getPaymentStatus SOAP request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| invoiceReference | The SEQR service reference to the registered invoice. |
| invoiceVersion | Version of the invoice. The first time that it uses getPaymentStatus method the client sets the invoiceVersion to zero. The SEQR service increments the invoiceVersion in responce message when: the state of the payment (invoiceStatus) changes, or, a new buyer token is provided to be considered in the invoice. In subsequent uses of the getPaymentStatus method, the client must use the latest value of invoiceVersion as an acknowledgement that it has received the latest change. |


## getPaymentStatus SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | The unique reference generated by the SEQR service once the invoice has been paid (null for all other invoiceStatus than PAID invoice has been paid). |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| invoiceStatus | Status of the invoice: 0 - Pending usage (when sent from SEQR), ISSUED - Invoice is issued, and waiting for payment, PAID - Invoice is paid, PARTIALLY_PAID - Invoice is partially paid, PENDING_ISSUER_ACKNOWLEDGE - Payment is updated and waiting for issuer acknowledgement, CANCELED - Invoice is canceled, FAILED - Invoice payment has failed, RESERVED - The invoice amount is reserved. **Note!** If getPaymentStatus is not queried after a successful payment, SEQR will assume that cash register is not notified of the successful payment and will reverse the transaction after 20 seconds. |
| customerTokens | List of customer tokens relevant for this payment |
| deliveryAddress | If the payment should be delivered automatically, this contains the delivery address to deliver to |
| resultCode | Receipt of the payment, if the status is PAID |


## getPaymentStatus SOAP request example

{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:getPaymentStatus>
       <context>
         <channel>extWS</channel>
         <clientComment>comment</clientComment>
         <clientId>testClient</clientId>
         <clientReference>12345</clientReference>
         <clientRequestTimeout>0</clientRequestTimeout>
         <initiatorPrincipalId>
           <id>87e791f9e24148a6892c52aa85bb0331</id>
           <type>TERMINALID</type>
         </initiatorPrincipalId>
         <password>123456</password>
       </context>
       <invoiceVersion>0</invoiceVersion>
       <invoiceReference>123123</invoiceReference>
     </ext:getPaymentStatus>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## getPaymentStatus SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:getPaymentStatusResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
        <return>
           <resultCode>0</resultCode>
           <resultDescription>SUCCESS</resultDescription>
           <status>ISSUED</status>
           <version>1</version>
        </return>
      </ns2:getPaymentStatusResponse>
   </soap:Body>
</soap:Envelope>

{% endhighlight %}



## cancelInvoice SOAP request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| invoiceReference | Reference of the invoice to be canceled. |


## cancelInvoice SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## cancelInvoice SOAP request example

{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:cancelInvoice>
       <context>
          <channel>extWS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>87e791f9e24148a6892c52aa85bb0331</id>
            <type>TERMINALID</type>
          </initiatorPrincipalId>
          <password>1234</password>
       </context>
       <invoiceReference>123123</invoiceReference>
     </ext:cancelInvoice>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## cancelInvoice SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:cancelInvoiceResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
         </return>
      </ns2:cancelInvoiceResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## registerTerminal SOAP request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| externalTerminalId | The identifier of the terminal in the client system, e.g. "Store 111/Till 4". |
| password | Password for future communications with the SEQR service. |
| name | The name to appear on the buyer’s mobile device, e.g. "My Restaurant, cash register 2". |


## registerTerminal SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| terminalId | The newly generated unique identifier for this terminal. This identifier should be used in future communications of this terminal towards the SEQR service. |


## registerTerminal SOAP request example


{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:registerTerminal>
       <context>
          <channel>WS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>fredellsfisk</id>
            <type>RESELLERUSER</type>
            <userId>9900</userId>
          </initiatorPrincipalId>
          <password>2009</password>
       </context>
       <externalTerminalId>Shop 1/POS 2</externalTerminalId>
       <password>secret</password>
       <name>My Shop's Name</name>
     </ext:registerTerminal>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## registerTerminal SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:registerTerminalResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <terminalId>87e791f9e24148a6892c52aa85bb0331</terminalId>
         </return>
      </ns2:registerTerminalResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## unregisterTerminal SOAP request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| TerminalId | The SEQR ID of the terminal to be unregistered. |


## unregisterTerminal SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## unregisterTerminal SOAP request example


{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:unregisterTerminal>
       <context>
          <channel>WS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>87e791f9e24148a6892c52aa85bb0331</id>
            <type>TERMINALID</type>
          </initiatorPrincipalId>
          <password>secret</password>
       </context>
     </ext:unregisterTerminal>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## unregisterTerminal SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:registerTerminalResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
         </return>
      </ns2:unregisterTerminalResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}





## assignSeqrId SOAP request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| SeqrId | The SEQR ID of the terminal. |


## assignSeqrId SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## assignSeqrId SOAP request example


{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:assignSeqrId>
       <context>
          <channel>WS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>87e791f9e24148a6892c52aa85bb0331</id>
            <type>TERMINALID</type>
          </initiatorPrincipalId>
          <password>secret</password>
       </context>
       <seqrId>ABC123456</seqrId>
     </ext:assignSeqrId>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## assignSeqrId SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:assignSeqrIdResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
         </return>
      </ns2:assignSeqrIdResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}





## commitReservation SOAP request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| invoiceReference | Reference of the invoice that is reserved. |


## commitReservation SOAP response fields


| Field | Description |
| --- | --- |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## commitReservation SOAP examples
To be added!


## submitPaymentReciept SOAP request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| ersReference | Reference of the payment for which the receipt is applicable. |
| receiptDocument | Receipt document, containing the full details of the receipt (mimeType, receiptData, receiptType). Preferably in ARTS Receipt XML/HTML format. |


## submitPaymentReceipt SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## submitPaymentReceipt SOAP request example


{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:submitPaymentReceipt>
       <context>
          <channel>WS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>87e791f9e24148a6892c52aa85bb0331</id>
            <type>TERMINALID</type>
          </initiatorPrincipalId>
          <password>secret</password>
       </context>
       <ersReference>2012050100000000000000001</ersReference>
       <receiptDocument>
          <mimeType>plain/xml</mimeType>
          <receiptData>Cjw/eG1sIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IlVURi04Ij8+Cjx</receiptData>
       </receiptDocument>
     </ext:submitPaymentReceipt>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



## submitPaymentReceipt SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:submitPaymentReceiptResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
           <ersReference>2012050100000000000000002</ersReference>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
         </return>
      </ns2:submitPaymentReceiptResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## refundPayment SOAP request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| ersReference | Reference of the payment to be refunded. |
| invoice | Invoice data, which contains the amount and other invoice information after products has been removed from the original invoice. |


## refundPayment SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | The reference of the refund. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


## refundPayment SOAP request example


{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:refundPayment>
       <context>
          <channel>WS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>87e791f9e24148a6892c52aa85bb0331</id>
            <type>TERMINALID</type>
          </initiatorPrincipalId>
          <password>secret</password>
       </context>
       <ersReference>2012050100000000000000001</ersReference>
       <invoice>
          <title>Some Invoice</title>
          <cashierId>Bob</cashierId>
          <totalAmount>
            <currency>SEK</currency>
            <value>10.22</value>
          </totalAmount>
       </invoice>
     </ext:refundPayment>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## refundPayment SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:refundPaymentResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
           <ersReference>2012050100000000000000002</ersReference>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
         </return>
      </ns2:refundPaymentResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



## getClientSessionInfo request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| key | Authorization token, provided by SEQR server. |


## getClientSessionInfo response fields


| Field | Description |
| --- | --- |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| parameters | Set of parameters related to the user of the Service. Will always contain the following: msisdn (the msisdn of SEQR user), subscriberKey (unique identifier of SEQR user). May contain any additional parameters embedded in the QR code: ParameterX, ParameterZ. etc. (can be any number of embedded QR code parameters supplied in the list)|


## getClientSessionInfo SOAP request example


{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:getClientSessionInfo>
       <context>
          <channel>WEBSERVICE</channel>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>987654321</id>
            <type>TERMINALID</type>
          </initiatorPrincipalId>
          <password>1111</password>
       </context>
       <key>0000002012-63506374</key>
     </ext:getClientSessionInfo>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## getClientSessionInfo SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:getClientSessionInfoResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <parameters>
               <entry>
                  <key>f</key>
                  <value>6</value>
               </entry>
               <entry>
                  <key>e</key>
                  <value>5</value>
               </entry>
               <entry>
                  <key>authKey</key>
                  <value>0000002010-51702372</value>
               </entry>
               <entry>
                  <key>msisdn</key>
                  <value>46700643933</value>
               </entry>
               <entry>
                  <key>subscriberKey</key>
                  <value>132</value>
               </entry>
            </parameters> 
         </return>
      </ns2:getClientSessionInfoResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



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


## markTransationPeriod SOAP request example, per **shop** reconciliation


{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:markTransactionPeriod>
       <context>
          <channel>WS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>fredellsfisk</id>
            <type>RESELLERUSER</type>
            <userId>9900</userId>
          </initiatorPrincipalId>
          <password>secret</password>
       </context>
     </ext:markTransactionPeriod>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## markTransationPeriod SOAP response example, per **shop** reconciliation

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:markTransactionPeriodResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <transactionPeriodId>2012053119463656301000002</transactionPeriodId>
         </return>
      </ns2:markTransactionPeriodResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



## markTransationPeriod SOAP request example, per **terminal** reconciliation


{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:markTransactionPeriod>
       <context>
          <channel>WS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>fredellsfisk</id>
            <type>RESELLERUSER</type>
            <userId>9900</userId>
          </initiatorPrincipalId>
          <password>secret</password>
       </context>
   <entry>
          <key>TERMINALID</key>
          <value>2469e0bf14214797880cafb0eda1b535</value>
       </entry>
     </ext:markTransactionPeriod>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## markTransationPeriod SOAP response example, per **terminal** reconciliation

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:markTransactionPeriodResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <transactionPeriodId>2012053119463656301000002</transactionPeriodId>
         </return>
      </ns2:markTransactionPeriodResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



## executeReport SOAP request fields


| Field | Description |
| --- | --- |
| context | The ClientContext object |
| reportId | The identifier of the report that should be executed/produced. |
| language | The report language (null if the default language is to be used). |
| parameters | Optional parameters that can be used in processing the request. |


## executeReport SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | The reference to this operation. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| report | The executed/produced report, in binary and plain text form, if available. |


## executeReport SOAP request example


{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
     <ext:executeReport>
       <context>
          <channel>WS</channel>
          <clientComment>comment</clientComment>
          <clientId>testClient</clientId>
          <clientReference>12345</clientReference>
          <clientRequestTimeout>0</clientRequestTimeout>
          <initiatorPrincipalId>
            <id>fredellsfisk</id>
            <type>RESELLERUSER</type>
            <userId>9900</userId>
          </initiatorPrincipalId>
          <password>secret</password>
       </context>
       <reportId>SOME_REPORT</reportId>
     </ext:executeReport>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


## executeReport SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:executeReportResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <report>
               <content>MTE1Nzky</content>
               <contentString>115792</contentString>
               <mimeType>text/plain</mimeType>
               <title>Number of transfers today</title>
            </report> 
         </return>
      </ns2:executeReportResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


### For SOAP examples of different reports, refer to <a href="/merchant/reference/reporting">Reporting</a>.

   
   


## Result codes

| Code | Description |
| --- | --- |
| 0 | SUCCESS |
| 1 | PENDING_APPROVAL |
| 10 | REJECTED_BUSINESS_LOGIC |
| 11 | REJECTED_AMOUNT |
| 12 | REJECTED_PAYMENT |
| 13 | REJECTED_TOPUP |
| 20 | AUTHENTICATION_FAILED |
| 21 | ACCESS_DENIED |
| 22 | INVALID_NEW_PASSWORD |
| 23 | INVALID_ERS_REFERENCE |
| 29 | INVALID_INITIATOR_PRINCIPAL_ID |
| 30 | INVALID_RECEIVER_PRINCIPAL_ID |
| 31 | INVALID_SENDER_PRINCIPAL_ID |
| 32 | INVALID_TOPUP_PRINCIPAL_ID |
| 33 | INVALID_INITIATOR_PRINCIPAL_STATE |
| 34 | INVALID_RECEIVER_PRINCIPAL_STATE |
| 35 | INVALID_SENDER_PRINCIPAL_STATE |
| 36 | INVALID_TOPUP_PRINCIPAL_STATE |
| 37 | INITIATOR_PRINCIPAL_NOT_FOUND |
| 38 | RECEIVER_PRINCIPAL_NOT_FOUND |
| 39 | SENDER_PRINCIPAL_NOT_FOUND |
| 40 | TOPUP_PRINCIPAL_NOT_FOUND |
| 41 | INVALID_PRODUCT |
| 42 | INVALID_RECEIVER_ACCOUNT_TYPE |
| 43 | INVALID_SENDER_ACCOUNT_TYPE |
| 44 | INVALID_TOPUP_ACCOUNT_TYPE |
| 45 | RECEIVER_ACCOUNT_NOT_FOUND |
| 46 | SENDER_ACCOUNT_NOT_FOUND |
| 47 | TOPUP_ACCOUNT_NOT_FOUND |
| 48 | PAYMENT_IN_PROGRESS |
| 49 | INVALID_INVOICE_DATA |
| 50 | CANNOT_CANCEL_PAID_INVOICE |
| 51 | CANNOT_CANCEL_INVOICE_IN_PROGRESS |
| 52 | INVALID_CUSTOMER |
| 53 | INVALID_SEQR_ID|
| 54 | INVALID_INVOICE_REFERENCE |
| 55 | PAYMENT_ALREADY_CANCELLED |
| 56 | REGISTRATION_NOT_POSSIBLE |
| 60 | AUTHORIZATION_EXPIRED |
| 61 | AUTHORIZATION_CANCELLED |
| 62 | AUTHORIZATION_IN_PROGRESS |
| 64 | INVALID_NOTIFICATION_URL |
| 90 | SYSTEM_ERROR |
| 91 | UNSUPPORTED_OPERATION |
| 92 | LICENSE_REJECTION |
| 93 | SYSTEM_BUSY |
| 94 | SERVICE_UNAVAILABLE |












