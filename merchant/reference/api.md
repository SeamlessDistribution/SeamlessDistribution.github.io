---
layout: default
title: SEQR Merchant API
description: API reference
---

# Payment API / WSDL

This is a description of our SOAP-WS-API for merchants, our test WSDL is available at: 
https://extdev4.seqr.se/extclientproxy/service/v2?wsdl

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
               <li><a href="#context-parameter-used-in-all-calls">ClientContext context</a></li>
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
               <li><a href="#context-parameter-used-in-all-calls">ClientContext context</a></li>
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
               <li><a href="#context-parameter-used-in-all-calls">ClientContext context</a></li>
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
               <li><a href="#context-parameter-used-in-all-calls">ClientContext context</a></li>
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
               <li><a href="#context-parameter-used-in-all-calls">ClientContext context</a></li>
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
               <li><a href="#context-parameter-used-in-all-calls">ClientContext context</a></li>
               <li>String ersReference</li>
               <li>ReceiptDocument receiptDocument</li>
            </ul>
         </td>
         <td>Used to confirm that the payment was received by the cashregister. 
            Adds an optional receipt document to a payment.
         </td>
      </tr>
      <tr>
         <td>
            refundPayment
            <ul>
               <li><a href="#context-parameter-used-in-all-calls">ClientContext context</a></li>
               <li>String ersReference</li>
               <li>Invoice invoice</li>
            </ul>
         </td>
         <td>Refunds a previous payment, either part of it or the whole sum. Note that this method requires that the account provider's API is able to handle refund payments.
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


### Method for retrieving user information (valid for Service integration)


|--- | --- |
|  Method | Description |
|--- | --- |
| getClientSessionInfo | Retrieves user information |
| --- | --- |



### Methods for reconciliation and reporting 


|--- | --- |
|  Method | Description |
|--- | --- |
| markTransactionPeriod | Marks the end of one and the beginning of a new transaction period; used in reporting |
| executeReport | Executes a report on the SEQR service |
| --- | --- |




## Context parameter used in all calls 

<a name="context"></a>

A principal is the main actor in each request to the SEQR service and represents either a seller or a buyer. Each request has at least an initiator principal.
The ClientContext structure is used in all requests to identify, authenticate and authorize the client initiating the transaction. For authentication the credentials of the initiator principal are used. As all transactions take place over a secure channel (typically HTTPS) the ClientContext is sent in clear text.

If no max-length is specified it is unlimited for strings.

<table>
<tr><th>ClientContext fields</th><th>Description</th><th>Type</th><th>Max-Length</th></tr>
<tr><td>clientId </td>
    <td> Client id identifies the software with which the SEQR service is communicating, for example “CashRegisterManager version 1.3.4.</td>
    <td> string </td>
    <td> </td></tr>
<tr><td>channel </td>
    <td> The channel used to send a request. Always use ClientWS or WS. </td>
    <td> string </td>
    <td> 40 </td></tr>
<tr><td>clientRequestTimeout </td>
    <td> The client side timeout for the request. If the response is not received before the timeout the client will attempt to abort the request. Must be set to 0, so there will not be any client forced timeouts in the SEQR service. </td>
    <td> long </td>
    <td>  </td></tr>
<tr><td>initiatorPrincipalId </td>
    <td> Used for authentication of the principal and contains the id and type, as well as an optional user id. 
         Use TERMINALID except when you regsister a new terminal, then you need RESELLERUSER (as provided from Seamless). 
    </td>
    <td> string </td>
    <td>  </td></tr>
<tr><td>password</td>
    <td>The password used to authenticate the initiator principal.</td>
    <td> string </td>
    <td>  </td></tr>
<tr><td>clientReference </td>
    <td>The client reference for the transaction.
        Recommended: the clientReference should be unique at least for the specific client id.
        Note: SEQR service does not check this field. The field has a maximum length of 32 characters. 
        The field is mandatory for troubleshooting purposes.
    </td>
    <td> string </td>
    <td> 32 </td></tr>
<tr><td>clientComment </td>
    <td>Client comment included within the request. Optional.</td>
    <td> string </td>
    <td> 80 </td></tr>
</table>




## Invoice data 


Invoice is used in sending, updating and receiving status on a payment. What you need to set is: 


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| acknowledgmentMode | Needs to be set to NO_ACKNOWLEDGMENT unless you provide loyalty flow | string |  |
| backURL | used in in-app or web shopping | string |  |
| cashierId | "Alice" will show on receipt | string |  |
| clientInvoiceId | Your purchase reference | string |  |
| footer | receipt footer text | string |  |
| invoiceRows | See [invoiceRow data description](#invoiceRow) | 
| issueDate | cashregsister Date  | dateTime | |
| notificationURL | optional notification/confirmation url | string |  |
| paymentMode | use IMMEDIATE_DEBIT as RESERVATION_DESIRED / RESERVATION_REQUIRED are limited in use | string |  |
| title | title displayed on bill and receipt | string |  |
| totalAmount | full amount of invoice/bill |  |  |




## invoiceRow data <a name="invoiceRow"></a>


Used to present the payment in the app. 


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| itemDescription | optional | string |  |
| itemDiscount | optional | decimal |  |
| itemEAN | optional | string |  |
| itemQuantity | should be 1 or more | decimal |  |
| itemTaxRate | optional VAT line like "0.25" | decimal |  |
| itemTotalAmount | required total decimal for this row | decimal |  |
| itemUnit | optional "dl" | string |  |
| itemUnitPrice | optional  | decimal |  |


# Requests and responses

## sendInvoice 

#### sendInvoice SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used by this method (will be null after this method). |
| resultCode | Request result code |
| invoiceQRCode | SEQR generated QR Code (used for webshops; not relevant for cash registers) |
| resultDescription | A textual description of resultCode  |
|invoiceReference  | The SEQR service reference to the registered invoice. |


#### sendInvoice SOAP request example

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
            <id>8609bf533abf4a20816e8bfe76639521</id>
            <type>TERMINALID</type>
          </initiatorPrincipalId>
          <password>N2YFUhKaB1ZSuVF</password>
       </context>
       <invoice>
       	<acknowledgmentMode>NO_ACKNOWLEDGMENT</acknowledgmentMode>
          <title>Some Invoice</title>
          <cashierId>Bob</cashierId>
          <totalAmount>
            <currency>SEK</currency>
            <value>10.22</value>
          </totalAmount>
          <!-- in case you don't want to poll for payment status -->
          <notificationUrl>http://www.thirdparty.com/notifyMeHere</notificationUrl>          
       </invoice>
     </ext:sendInvoice>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


#### sendInvoice SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:sendInvoiceResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <invoiceQRCode>HTTP://SEQR.SE/R1397222701693</invoiceQRCode>
            <invoiceReference>1397222701693</invoiceReference>
         </return>
      </ns2:sendInvoiceResponse>
   </soap:Body>
</soap:Envelope>

{% endhighlight %}


## updateInvoice

#### updateInvoice SOAP request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| invoice | Invoice data, which contains the amount and other invoice information |  |  |
| invoiceReference | The SEQR service reference to the registered invoice. | string |  |
| tokens | The customer tokens applied to this invoice. Can be used for loyalty membership, coupons, etc. The following parameters:type,value (such as card value, coupon code, status (0 - pending, 1 - used when updated by merchant, 90 - blocked or 99 - invalid, unknown), description. **Note!** The new token (e.g. name of loyalty card) must be added to SEQR system in advance.| list |  |


#### updateInvoice SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


#### updateInvoice SOAP request example


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


#### updateInvoice SOAP response example

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


## getPaymentStatus

#### getPaymentStatus SOAP request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| invoiceReference | The SEQR service reference to the registered invoice. | string |  |
| invoiceVersion | Version of the invoice. The first time that it uses getPaymentStatus method the client sets the invoiceVersion to zero. The SEQR service increments the invoiceVersion in responce message when: the state of the payment status changes, or, a new buyer token is provided to be considered in the invoice. In subsequent uses of the getPaymentStatus method, the client must use the latest value of invoiceVersion as an acknowledgement that it has received the latest change. |  |  |


#### getPaymentStatus SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | The unique reference generated by the SEQR service once the invoice has been paid (null for all other invoiceStatus than PAID invoice has been paid). | 
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| status | Status of the invoice: 0 - Pending usage (when sent from SEQR), ISSUED - Invoice is issued, and waiting for payment, PAID - Invoice is paid, PARTIALLY_PAID - Invoice is partially paid, PENDING_ISSUER_ACKNOWLEDGE - Payment is updated and waiting for issuer acknowledgement, CANCELED - Invoice is canceled, FAILED - Invoice payment has failed, RESERVED - The invoice amount is reserved. **Note!** If getPaymentStatus is not queried after a successful payment, SEQR will assume that cash register is not notified of the successful payment and will reverse the transaction after 20 seconds. |
| customerTokens | List of customer tokens relevant for this payment, for example loyalty memberships, coupons, etc. |
| deliveryAddress | If the payment should be delivered automatically, this contains the delivery address to deliver to |
| resultCode | Receipt of the payment, if the status is PAID |


#### getPaymentStatus SOAP request example

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


#### getPaymentStatus SOAP response example

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


## submitPaymentReciept

#### submitPaymentReciept SOAP request fields

This method confirms that the payment has been acknowledged and takes an optional receipt from the 
cashregisters as html. This receipt won't appear in the app automatically. 
Please contact us if you are interested in using a custom receipt in the app. 

| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| ersReference | Reference of the payment for which the receipt is applicable. |  |  |
| receiptDocument | Receipt document, containing the full details of the receipt (mimeType, receiptData, receiptType - all mandatory). Preferably in ARTS Receipt XML/HTML format. |  |  |


#### submitPaymentReceipt SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


#### submitPaymentReceipt SOAP request example


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
          <receiptType>xxx</receiptType>
       </receiptDocument>
     </ext:submitPaymentReceipt>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


#### submitPaymentReceipt SOAP response example

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


## cancelInvoice

#### cancelInvoice SOAP request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| invoiceReference | Reference of the invoice to be canceled. | string |  |


#### cancelInvoice SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


#### cancelInvoice SOAP request example

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


#### cancelInvoice SOAP response example

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


## commitReservation

#### commitReservation SOAP request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| invoiceReference | Reference of the invoice that is reserved. | string |  |


#### commitReservation SOAP response fields


| Field | Description |
| --- | --- |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


#### commitReservation SOAP examples

To be added - contact us if you plan to handle reservations. 


## refundPayment

#### refundPayment SOAP request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| ersReference | Reference of the payment to be refunded |  |  |
| invoice | Invoice data, which contains the amount and other invoice information after products have been removed from the original invoice |  |  |



#### refundPayment SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Reference to the payment that is refunded. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


#### refundPayment SOAP request example


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
          <title>Refund</title>
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


#### refundPayment SOAP response example

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



## registerTerminal

#### registerTerminal SOAP request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| externalTerminalId | The identifier of the terminal in the client system, e.g. "Store 111/Till 4". |  |  |
| password | Password for future communications with the SEQR service. | string |  |
| name | The name to appear on the buyer’s mobile device, e.g. "My Restaurant, cash register 2". | string |  |


#### registerTerminal SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| terminalId | The newly generated unique identifier for this terminal. This identifier should be used in future communications of this terminal towards the SEQR service. |


#### registerTerminal SOAP request example


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


#### registerTerminal SOAP response example

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


## unregisterTerminal

#### unregisterTerminal SOAP request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| TerminalId | The SEQR ID of the terminal to be unregistered. |  |  |


#### unregisterTerminal SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


#### unregisterTerminal SOAP request example


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


#### unregisterTerminal SOAP response example

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


## assingSeqrId

#### assignSeqrId SOAP request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| SeqrId | The SEQR ID of the terminal. |  |  |


#### assignSeqrId SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | Not used, will be null. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


#### assignSeqrId SOAP request example


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


#### assignSeqrId SOAP response example

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


## getClientSessionInfo

#### getClientSessionInfo request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| key | Authorization token, provided by SEQR server. |  |  |


#### getClientSessionInfo response fields


| Field | Description |
| --- | --- |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| parameters | Set of parameters related to the user of the Service. Will always contain the following: msisdn (the msisdn of SEQR user), subscriberKey (unique identifier of SEQR user). May contain any additional parameters embedded in the QR code: ParameterX, ParameterZ. etc. (can be any number of embedded QR code parameters supplied in the list)|


#### getClientSessionInfo SOAP request example


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


#### getClientSessionInfo SOAP response example

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



## markTransactionPeriod

#### markTransactionPeriod request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| parameters | Optional parameters that can be used in processing the request. |  |  |


#### markTransactionPeriod response fields


| Field | Description |
| --- | --- |
| ersReference | The reference to this operation. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |


#### markTransactionPeriod SOAP request example, per **shop** reconciliation


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


#### markTransactionPeriod SOAP response example, per **shop** reconciliation

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



#### markTransactionPeriod SOAP request example, per **terminal** reconciliation


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


#### markTransactionPeriod SOAP response example, per **terminal** reconciliation

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


## executeReport

For SOAP examples of different reports, refer to <a href="/merchant/reference/reporting">Reporting</a>.

#### executeReport SOAP request fields


| Field | Description | Type | Max-Length |
| --- | --- | --- | --- |
| context | See [the ClientContext object](#context) |  |  |
| reportId | The identifier of the report that should be executed/produced. | string |  |
| language | The report language (null if the default language is to be used). | string |  |
| parameters | Optional parameters that can be used in processing the request. | parameters |  |


#### executeReport SOAP response fields


| Field | Description |
| --- | --- |
| ersReference | The reference to this operation. |
| resultCode | see Result codes |
| resultDescription | A textual description of resultCode. |
| report | The executed/produced report, in binary and plain text form, if available. |


#### executeReport SOAP request example


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


#### executeReport SOAP response example

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



## Result codes

Note that this list points out the responses that are relevant, with the API request(s) that may issue the response. The other response codes are unrelevant but could occur in some cases.


| Code | Description |  Detailed description | Request that may issue this response |
| --- | --- |
| 0 | SUCCESS | Given operation ended successfully | All requests |
| 20 | AUTHENTICATION_FAILED | Wrong password | All requests |
| 21 | ACCESS_DENIED | Password assigned to terminalId is less than 4 characters | unregisterTerminal, sendInvoice, getPaymentStatus |
| 23 | INVALID_ERS_REFERENCE | Given ERS reference number cannot be found | refundPayment |
| 29 | INVALID_INITIATOR_PRINCIPAL_ID | Given id for TERMINALID in initiatorPrincipalId cannot be found | All requests |
| 37 | INITIATOR_PRINCIPAL_NOT_FOUND | Given id or userId for RESELLERUSER in initiatorPrincipalId section not found in SEQR | All requests |
| 49 | INVALID_INVOICE_DATA | For example wrong currency | sendInvoice, updateInvoice |
| 50 | CANNOT_CANCEL_PAID_INVOICE | Invoice with given reference number has already been paid | cancelInvoice |
| 51 | CANNOT_CANCEL_INVOICE_ IN_PROGRESS | | cancelInvoice |
| 53 | INVALID_SEQR_ID | Non alphanumeric segrId was used | assignSeqrId |
| 54 | INVALID_INVOICE_REFERENCE | Invoice with given reference number can't be found for given terminal id | getPaymentStatus |
| 55 | PAYMENT_ALREADY_CANCELLED | ? | cancelInvoice |
| 64 | INVALID_NOTIFICATION_URL | Not valid notificationUrl (e.g not starting with http://) | sendInvoice, updateInvoice, refundPayment |
| 90 | SYSTEM_ERROR | Unclassified errors | All requests |
| 91 | UNSUPPORTED_OPERATION | For example wrong TYPE in initiatorPrincipalId section | All requests |
| 94 | SERVICE_UNAVAILABLE | External backend system unavailable (e.g. Bank system) | All requests |
| 95 | INVOICE_ALREADY_CANCELED | Invoice with given reference number is already canceled through cancelInvoice call | cancelInvoice |










