---
layout: default
title: Glase Merchant API
description: API reference
---
# Table of content

1. [Payment API WSDL](#payment-api)
2. [Methods for payments](#methods-for-payments)
	* [sendInvoice](#sendinvoice)
	* [updateInvoice](#updateinvoice)
	* [getPaymentStatus](#getpaymentstatus)
	* [cancelInvoice](#cancelinvoice)
	* [commitReservation](#commitreservation)
	* [submitPaymentReceipt](#submitpaymentreceipt)
	* [refundPayment](#refundpayment)
	* [creditUser](#credituser)
3. [Methods specific for point of sale (terminal) registration](#methods-specific-for-point-of-sale-terminal-registration)
	* [registerTerminal](#registerterminal)
	* [unRegisterTerminal](#unregisterterminal)
	* [assignSeqrId](#assignseqrid)
4. [Methods for reconciliation and reporting](#methods-for-reconciliation-and-reporting)
	* [markTransactionPeriod](#marktransactionperiod)
	* [executeReport](#executereport)
4. [Request objects data](#request-objects-data)
	* [ClientContext parameter used in all calls](#clientcontext-data)
	* [Invoice data](#invoice-data)
	* [InvoiceRow data](#invoicerow-data)
	* [Receipt data](#receipt-data)
5. [Result codes](#result-codes)


# Payment API

This is a description of <span class="seqrhl">SEQR SOAP-WS-API v2.6.0</span> for merchants. 
<br>Our test environment WSDL is available at: <span class="seqrhl">https://extdev.seqr.com/soap/merchant/cashregister-2?wsdl</span>

## Methods for payments

<table>
   <tbody>
   <col width="35%"/>
   <col width="65%"/>
      <tr>
         <th>Method</th>
         <th>Description</th>
      </tr>
      <tr>
         <td>
            <a href="#sendinvoice">sendInvoice</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li><a href="#invoice-data">Invoice invoice</a></li>
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
            <a href="#updateinvoice">updateInvoice</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li><a href="#invoice-data">Invoice invoice</a></li>
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
            <a href="#getpaymentstatus">getPaymentStatus</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li>String invoiceReference</li>
               <li>int invoiceVersion</li>
            </ul>
         </td>
         <td>Obtains status of a previously submitted invoice. When fetching the payment status, SEQR may communicate a set of customer tokens to the merchant that are applicable for the payment. The merchant must then decide which tokens are applied (such as for loyalty) and send them back with the updateInvoice request.
         </td>
      </tr>
      <tr>
         <td>
            <a href="#cancelinvoice">cancelInvoice</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li>String invoiceReference</li>
            </ul>
         </td>
         <td>Cancels an unpaid invoice.
         </td>
      </tr>
      <tr>
         <td>
            <a href="#commitreservation">commitReservation</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li>String invoiceReference</li>
            </ul>
         </td>
         <td>Commits a payment, if a payment reservation successfully executed.
            We are working on support for reservations in cooperation with more banks.
         </td>
      </tr>
      <tr>
        <td>
            <a href="#submitpaymentreceipt">submitPaymentReceipt</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li>String ersReference</li>
               <li>ReceiptDocument receiptDocument</li>
            </ul>
         </td>
         <td>Used to confirm that the payment was received by the point of sale. 
            Adds a receipt document to the payment.
         </td>
      </tr>
      <tr>
         <td>
            <a href="#refundpayment">refundPayment</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li>String ersReference</li>
               <li><a href="#invoice-data">Invoice invoice</a></li>
            </ul>
         </td>
         <td>Refunds a previous payment, either part of it or the whole sum.
         </td>
      </tr>
   </tbody>
</table>

## Methods specific for point of sale (terminal) registration 

<table>
   <tbody>
   <col width="35%"/>
   <col width="65%"/>
      <tr>
         <th>Method</th>
         <th>Description</th>
      </tr>
      <tr>
         <td>
            <a href="#registerterminal">registerTerminal</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li>String externalTerminalId</li>
               <li>String password</li>
               <li>String name</li>
            </ul>
         </td>
         <td>
				Registers a new terminal in the SEQR service.
         </td>
      </tr>
      <tr>
         <td>
            <a href="#unregisterterminal">unRegisterTerminal</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
            </ul>
         </td>
         <td>
				Unregisters an already registered terminal.
         </td>
      </tr>
      <tr>
         <td>
            <a href="#assignseqrid">assignSeqrId</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li>String seqrId</li>
            </ul>
         </td>
         <td>
				Assigns a SEQR ID to a terminal.
         </td>
      </tr>
   </tbody>
</table>

## Methods for reconciliation and reporting 

<table>
   <tbody>
   <col width="35%"/>
   <col width="65%"/>
      <tr>
         <th>Method</th>
         <th>Description</th>
      </tr>
      <tr>
         <td>
            <a href="#marktransactionperiod">markTransactionPeriod</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li>Map parameters</li>
            </ul>
         </td>
         <td>
				Marks the end of one and the beginning of a new transaction period. Used in reporting.
         </td>
      </tr>
      <tr>
         <td>
            <a href="#executereport">executeReport</a>
            <ul>
               <li><a href="#clientcontext-data">ClientContext context</a></li>
               <li>String reportId</li>
               <li>String language</li>
               <li>Map parameters</li>
            </ul>
         </td>
         <td>
				Executes a report on the SEQR service.
         </td>
      </tr>
   </tbody>
</table>

# Request objects data

<h2 id="clientcontext-data">ClientContext parameter used in all calls</h2>

A principal is the main actor in each request to the SEQR service and represents either a seller or a buyer. Each request has at least an initiator principal.
The client Context structure is used in all requests to identify, authenticate and authorize the client initiating the transaction. For authentication the credentials of the initiator principal are used. As all transactions take place over a secure channel (typically HTTPS) the ClientContext is sent in clear text.

If no max-length is specified it is unlimited for strings.

<table>
	<tbody>
	<tr>
		<th colspan="2">ClientContext</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>channel</td>
		<td>The channel used to send a request. Always use ClientWS or
			WS.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Max-Length: <span class="seqrhl">40</span></li>
				<li>Sample value: <span class="seqrhl">ClientWS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>clientComment</td>
		<td>Client comment included within the request.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Max-Length: <span class="seqrhl">80</span></li>
				<li>Sample value: <span class="seqrhl">My comment</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>clientId</td>
		<td>Client ID identifies the software which the SEQR service is
			communicating with.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">My POS Version 1.2.3</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>clientReference</td>
		<td>The client reference for the transaction. Recommendation: the
			clientReference should be unique at least for the specific clientId.
			Note: SEQR service does not check this field. The field is mandatory
			for troubleshooting purposes.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Max-Length: <span class="seqrhl">32</span></li>
				<li>Sample value: <span class="seqrhl">my_invoice_1234567890</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>clientRequestTimeout</td>
		<td>The client side timeout for the request. If the response is
			not received before the timeout the client will attempt to abort the
			request. Must be set to 0, so there will not be any client forced
			timeouts in the SEQR service.
			<ul>
				<li>Type: <span class="seqrhl">long</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Recommended value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>initiatorPrincipalId</td>
		<td>Used for authentication of the principal. Contains subfields id, type and optional userId. Use RESELLERUSER type when
			you register a new terminal with id provided from SEQR and userId with fixed value, otherwise use TERMINALID type with id provided from SEQR.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Samples below:
{% highlight python %}
<initiatorPrincipalId>
    <id>my_terminal_id</id>
    <type>TERMINALID</type>
</initiatorPrincipalId>
{% endhighlight %}
{% highlight python %}
<initiatorPrincipalId>
    <id>my_reseller_id</id>
    <type>RESELLERUSER</type>
    <userId>9900</userId>
</initiatorPrincipalId>
{% endhighlight %}
          		</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>password</td>
		<td>The password used to authenticate the initiator principal.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">my_password</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

## Invoice data 

Invoice is used in sending, updating and receiving status on a payment. What you need to set is: 

<table>
	<tbody>
	<tr>
		<th colspan="2">Invoice</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>paymentMode</td>
		<td>The mode of payment. For standard payments use IMMEDIATE_DEBIT.<br>Modes RESERVATION_DESIRED / RESERVATION_REQUIRED / RESERVATION_REQUIRED_PRELIMINARY_AMOUNT are used in non-standard payments. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">IMMEDIATE_DEBIT</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>acknowledgmentMode</td>
		<td>Needs to be set to NO_ACKNOWLEDGMENT unless you provide loyalty flow.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">NO_ACKNOWLEDGMENT</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>issueDate</td>
		<td>The date of invoice submit.
			<ul>
				<li>Type: <span class="seqrhl">dateTime</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">2015-12-25T12:34:56</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>title</td>
		<td>Title displayed on bill and receipt.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">My Sample Store</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>clientInvoiceId</td>
		<td>This invoice id refers to the identification number from the merchant's shop.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">Merchant34213421</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>invoiceRows</td>
		<td>Contains multiple invoiceRows. See <a href="#invoicerow-data">invoiceRow data description</a>.</td>
	</tr>
	<tr>
		<td>totalAmount</td>
		<td>Summary amount of invoice/bill. Consists of a value (in pattern #.##) and a currency. Use ISO standard currency of the country you are in. 
			<ul>
				<li>Value type: <span class="seqrhl">decimal</span></li>
				<li>Currency type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample below:
{% highlight python %}
<totalAmount>
    <value>149.99</value>
    <currency>SEK</currency>
</totalAmount>
{% endhighlight %}
          		</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>cashierId</td>
		<td>Merchant cashier id.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">John00232</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>footer</td>
		<td>Footer that you want to display in the users phone receipt.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">RFC:12389234DKJ3</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>backURL</td>
		<td>A web-site address to where the SEQR mobile application user will be redirected after a successful payment or after pressing cancel.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample value: <span class="seqrhl">http://merchant.com/displayafterpay</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>notificationUrl</td>
		<td>An optional notification/confirmation URL. If set SEQR will access this URL after successful payment by user.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample value: <span class="seqrhl">http://merchant.com/paymentConfirmation?inv=32923423423</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>commitReservationTimeout</td>
		<td>Time (in seconds) while merchant can make a commit of preliminary payment.
			<ul>
				<li>Type: <span class="seqrhl">long</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample value: <span class="seqrhl">3600</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

## InvoiceRow data

Used to present the payment in the app. 

<table>
	<tbody>
	<tr>
		<th colspan="2">InvoiceRow</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>itemDescription</td>
		<td>Description of the item that was sold. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample value: <span class="seqrhl">Coca-Cola</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>itemDiscount</td>
		<td>Total discount for listed products. Consists of a value (in pattern #.##) and a currency field. Use ISO standard currency signature of the country you are in.
			<ul>
				<li>Value type: <span class="seqrhl">decimal</span></li>
				<li>Currency type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample below:
{% highlight python %}
<itemDiscount>
    <value>2.50</value>
    <currency>SEK</currency>
</itemDiscount>
{% endhighlight %}
          		</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>itemEAN</td>
		<td>Product EAN.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample value: <span class="seqrhl">0076232342123</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>itemQuantity</td>
		<td>Should be 1 or more.
			<ul>
				<li>Type: <span class="seqrhl">decimal</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">2</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>itemSKU</td>
		<td>Product SKU.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample value: <span class="seqrhl">12345-A</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>itemTaxRate</td>
		<td>Use the tax rate of your country (in integer format: ##).
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample value: <span class="seqrhl">24</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>itemTotalAmount</td>
		<td>Total value for listed products. Consists of a value (in format #.##) and a currency field. Use ISO standard currency signature of the country you are in.
			<ul>
				<li>Value type: <span class="seqrhl">decimal</span></li>
				<li>Currency type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample below:
{% highlight python %}
<itemTotalAmount>
    <value>44.99</value>
    <currency>SEK</currency>
</itemTotalAmount>
{% endhighlight %}
          		</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>itemUnit</td>
		<td>Use the type of unit based on ISO-20022.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample value: <span class="seqrhl">kg</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>itemUnitPrice</td>
		<td>Unit price for listed products. Consists of a value (in format #.##) and a currency field. Use ISO standard currency signature of the country you are in.
			<ul>
				<li>Value type: <span class="seqrhl">decimal</span></li>
				<li>Currency type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample below:
{% highlight python %}
<itemUnitPrice>
    <value>2.99</value>
    <currency>SEK</currency>
</itemUnitPrice>
{% endhighlight %}
          	</li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

## Receipt data

Used to receipt information after payment.

<table>
	<tbody>
	<tr>
		<th colspan="2">Receipt</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>terminalId</td>
		<td>The name of the registered terminal. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">my_terminal</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>paymentDate</td>
		<td>The date of the payment.
			<ul>
				<li>Type: <span class="seqrhl">dateTime</span></li>
				<li>Sample value: <span class="seqrhl">2015-10-29T10:18:48.663+01:00</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>invoiceReference</td>
		<td>The SEQR service reference to the registered invoice.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">20151029186719114</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>paymentReference</td>
		<td>The SEQR service reference to the registered payment.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">2015102910184861801032678</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>payerTerminalId</td>
		<td>The id of the terminal registered in SEQR system.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">d613c5b8428d17248751bc101</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>receiverName</td>
		<td>The name of the receiver.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>invoice</td>
		<td>Invoice data which contains the amount and other invoice information. See <a href="#invoice-data">invoice description</a>.</td>
	</tr>
	</tbody>
</table>

# Requests and responses

## sendInvoice 

#### sendInvoice SOAP request fields

<table>
	<tbody>
	<tr>
		<th colspan="2">sendInvoice request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>.
		</td>
	</tr>
	<tr>
		<td>invoice</td>
		<td>Invoice data which contains the amount and other invoice information. See <a href="#invoice-data">invoice description</a>.
		</td>
	</tr>
	<tr>
		<td>tokens</td>
		<td>The customer tokens applied to this invoice. Can be used for loyalty membership, coupons, etc.
		Consists of following fields: description (that will be presented to a customer after scaning QR code),
		id, value (such as card value, coupon code, etc.), status (0 - pending, 1 - used when updated by
		merchant, 90 - blocked or 99 - invalid, unknown).
		<br>
		<b>Note!</b> The new token (e.g. name of loyalty card) must be added to SEQR system in advance.
			<ul>
				<li>Description type: <span class="seqrhl">string</span></li>
				<li>Id type: <span class="seqrhl">string</span></li>
				<li>Value type: <span class="seqrhl">string</span></li>
				<li>Status type: <span class="seqrhl">integer</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample below (zero or more repetitions):
{% highlight python %}
<tokens>
   <description>Loyalty card name</description>
   <id>SOME_CARD</id>
   <status>1</status>
   <value>2610411111110</value>
</tokens>
{% endhighlight %}
          		</li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### sendInvoice SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">sendInvoice response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code. 
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>invoiceQRCode</td>
		<td>SEQR generated QR Code (used for webshops; not relevant for points of sale).
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">HTTP://SEQR.SE/R1397240460668</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of the resultCode.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>invoiceReference</td>
		<td>The SEQR service reference to the registered invoice. This is the invoice reference
			a merchant should use within getPaymentStatus.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">1397240460668</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

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
          <invoiceRows>
            <invoiceRow>
              <itemDescription>Laptop Samsung Ultrabook</itemDescription>
              <itemQuantity>2</itemQuantity>
              <itemSKU>16</itemSKU>
              <itemTaxRate>24</itemTaxRate>
              <itemTotalAmount>
                <currency>SEK</currency>
                <value>500</value>
              </itemTotalAmount>
              <itemUnit></itemUnit>
              <itemUnitPrice>
                <currency>SEK</currency>
                <value>250</value>
              </itemUnitPrice>
            </invoiceRow>
            <invoiceRow>
              <itemDescription>Laptop Apple MacBook Air</itemDescription>
              <itemQuantity>1</itemQuantity>
              <itemSKU>3</itemSKU>
              <itemTaxRate>24</itemTaxRate>
              <itemTotalAmount>
                <currency>SEK</currency>
                <value>1000</value>
              </itemTotalAmount>
              <itemUnit></itemUnit>
              <itemUnitPrice>
                <currency>SEK</currency>
                <value>1000</value>
              </itemUnitPrice>
            </invoiceRow>
          </invoiceRows>
          <totalAmount>
            <currency>SEK</currency>
            <value>1500</value>
          </totalAmount>
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

<table>
	<tbody>
	<tr>
		<th colspan="2">updateInvoice request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>.
		</td>
	</tr>
	<tr>
		<td>invoice</td>
		<td>Invoice data which contains the amount and other invoice information. See <a href="#invoice-data">invoice description</a>.
		</td>
	</tr>
	<tr>
		<td>invoiceReference</td>
		<td>The SEQR service reference of the registered invoice.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">1397240460668</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>tokens</td>
		<td>The customer tokens applied to this invoice. Can be used for loyalty membership, coupons, etc.
		Contains of: description (that will be presented to a customer after scaning QR code), id, value
		(such as card value, coupon code, etc.), status (0 - pending, 1 - used when updated by merchant,
		90 - blocked or 99 - invalid, unknown).
		<br>
		<b>Note!</b> The new token (e.g. name of loyalty card) must be added to SEQR system in advance.
			<ul>
				<li>Description type: <span class="seqrhl">string</span></li>
				<li>Id type: <span class="seqrhl">string</span></li>
				<li>Value type: <span class="seqrhl">string</span></li>
				<li>Status type: <span class="seqrhl">integer</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample below (zero or more repetitions):
{% highlight python %}
<tokens>
   <description>Loyalty card name</description>
   <id>SOME_CARD</id>
   <status>1</status>
   <value>2610411111110</value>
</tokens>
{% endhighlight %}
          		</li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### updateInvoice SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">updateInvoice response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code. 
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of the resultCode.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>ersReference</td>
		<td>Not used, will be null.</td>
	</tr>
	</tbody>
</table>

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
       <invoiceReference>123123</invoiceReference>
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

<table>
	<tbody>
	<tr>
		<th colspan="2">getPaymentStatus request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>.
		</td>
	</tr>
	<tr>
		<td>invoice</td>
		<td>Invoice data which contains the amount and other invoice information. See <a href="#invoice-data">invoice description</a>.
		</td>
	</tr>
	<tr>
		<td>invoiceReference</td>
		<td>The SEQR service reference of the registered invoice.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">1397240460668</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>invoiceVersion</td>
		<td>Version of the invoice. The first time that it uses
			getPaymentStatus method the client sets the invoiceVersion to zero.
			The SEQR service increments the invoiceVersion in response message
			when: the state of the payment status changes or a new buyer token is
			provided to be considered in the invoice. In subsequent uses of the
			getPaymentStatus method, the client must use the latest value of
			invoiceVersion as an acknowledgement that it has received the latest
			change.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### getPaymentStatus SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">getPaymentStatus response</th>
	</tr>
	<col width="35%" />
	<col width="65%" />
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>ersReference</td>
		<td>The unique reference generated by the SEQR service once the invoice has been paid (null for all other invoiceStatus than PAID).
		</td>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of resultCode. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>status</td>
		<td>Status of the invoice.
			<ul>
				<li>0 - pending usage (when sent from SEQR)</li>
				<li>ISSUED - invoice is issued and waiting for payment</li>
				<li>PAID - invoice is paid</li>
				<li>PARTIALLY_PAID - invoice is partially paid</li>
				<li>PENDING_ISSUER_ACKNOWLEDGE - payment is updated and waiting for issuer acknowledgement</li>
				<li>CANCELED - invoice is canceled</li>
				<li>FAILED - invoice payment has failed</li>
				<li>RESERVED - invoice amount is reserved</li>
			</ul>
			<b>Note!</b> If getPaymentStatus is not queried within 20 seconds after a successful payment, SEQR will assume that
			cash register is not notified of the successful payment and will reverse the transaction.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">ISSUED</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>receipt</td>
		<td>Receipt information. See <a href="#receipt-data">receipt description</a>.
		</td>
	</tr>
	</tbody>
</table>

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

## submitPaymentReceipt

#### submitPaymentReciept SOAP request fields

This method confirms that the payment has been acknowledged and adds a receipt from the point of sale as html. This receipt won't appear in the app automatically. 
Please contact us if you are interested in using a customized receipt in the app. 

<table>
	<tbody>
	<tr>
		<th colspan="2">submitPaymentReciept request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>.
		</td>
	</tr>
	<tr>
		<td>ersReference</td>
		<td>Reference of the payment for which the receipt is applicable.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">1397240460668</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>receiptDocument</td>
		<td>Receipt document, containing the full details of the receipt (mimeType, receiptData, receiptType - all mandatory). Preferably in ARTS Receipt XML/HTML format.
			<ul>
				<li>MimeType type: <span class="seqrhl">string</span></li>
				<li>ReceiptData type: <span class="seqrhl">base64Binary</span></li>
				<li>ReceiptType type: <span class="seqrhl">string</span></li>
				<li>Sample value: see request example below.</li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### submitPaymentReceipt SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">submitPaymentReciept response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of resultCode. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>ersReference</td>
		<td>Not used, will be null.
		</td>
	</tr>
	</tbody>
</table>

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

<table>
	<tbody>
	<tr>
		<th colspan="2">cancelInvoice request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>.
		</td>
	</tr>
	<tr>
		<td>invoiceReference</td>
		<td>Reference of the invoice to be canceled.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">1397240460668</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### cancelInvoice SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">cancelInvoice response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of resultCode. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>ersReference</td>
		<td>Not used, will be null.
		</td>
	</tr>
	</tbody>
</table>

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

<table>
	<tbody>
	<tr>
		<th colspan="2">commitReservation request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>.
		</td>
	</tr>
	<tr>
		<td>amount</td>
		<td>Commited amount and currency. Consists of currency (ISO standard currency signature) and value (in format #.##).
			<ul>
				<li>Value type: <span class="seqrhl">decimal</span></li>
				<li>Currency type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">N</span></li>
				<li>Sample below:
{% highlight python %}
<amount>
    <value>2.99</value>
    <currency>SEK</currency>
</amount>
{% endhighlight %}
          		</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>invoiceReference</td>
		<td>Reference of the invoice that refers to the commitment.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">1397240460668</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### commitReservation SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">commitReservation response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of resultCode. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### commitReservation SOAP request example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:commitReservation xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <context>
            <clientRequestTimeout>0</clientRequestTimeout>
            <initiatorPrincipalId>
               <id>87e791f9e24148a6892c52aa85bb0331</id>
               <type>TERMINALID</type>
            </initiatorPrincipalId>
            <password>1234</password>
         </context>
         <amount>
            <currency>SEK</currency>
            <value>5</value>
         </amount>
         <invoiceReference>123123</invoiceReference>
      </ns2:commitReservation>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

#### commitReservation SOAP response example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:commitReservationResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
         </return>
      </ns2:commitReservationResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

## refundPayment

#### refundPayment SOAP request fields

<table>
	<tbody>
	<tr>
		<th colspan="2">refundPayment request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>.
		</td>
	</tr>
	<tr>
		<td>ersReference</td>
		<td>Reference of the payment to be refunded.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">2015050100000000000000002</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>invoice</td>
		<td>Invoice data which contains the amount and other invoice information. See <a href="#invoice-data">invoice description</a>.</td>
	</tr>
	</tbody>
</table>

#### refundPayment SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">refundPayment response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of resultCode. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>ersReference</td>
		<td>Reference to the payment that is refunded.
		</td>
	</tr>
	</tbody>
</table>

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

## creditUser

### creditUser SOAP request field


|--- | --- | --- |
|  Parameter name | Required | Description |
|--- | --- | --- |
| userId | Y | 	Unique identifier of Glase user on partner's (iGaming) platform. That Id has no meaning in any other contexts.Alphanumeric string up to 36 digits   |
| description | N | optional string that will be visible on user's receipt. If not specified we will apply default one i.e "Credit from Merchant" / "Withdrawal from iGaming". It may be specific for given partner. Alphanumeric, dot and comma allowed - up to 160 characters. |
| currency | Y | currency of a credit. |
| clientContext | Y | the same context as used in all other calls - identifies calling principal [http://developer.seqr.com/merchant/reference/api.html#clientcontext-data](http://developer.seqr.com/merchant/reference/api.html#clientcontext-data) |
| amount | Y | credit amount |
|--- | --- | --- |

#### Notes:

#### 1.userId

You can find  it (value) in getPaymentStatusResponse for payment of specific user
{% highlight python %}
<customerTokens>
    <token>
        <description>I_GAMING_INTEGRATION</description>
        <id>I_GAMING_INTEGRATION</id>
        <status>0</status>
        <value>jfJhO6XipEktpy2BryxV010001152594ssss587</value>
    </token>
</customerTokens>
{% endhighlight %}
#### 2.Description

Not always merchant's have context of user's country / language. We have such information so we can provide default description which is displayed in our clients language.

#### 3. Currency

If currency will be different from currency of Glase user account we will make conversion.

### creditUser SOAP request example

{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ext="http://external.interfaces.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <ext:creditUser>
         <context>
            <channel>WS</channel>
            <clientRequestTimeout>0</clientRequestTimeout>
            <initiatorPrincipalId>
               <id>some_terminal_id</id>
               <type>TERMINALID</type>
            </initiatorPrincipalId>
            <password>terminal_password</password>
         </context>
         <creditUserRequest>
            <userId>some_glase_user_id</userId>
            <amount>
               <currency>EUR</currency>
               <value>100.00</value>
            </amount>
            <description>user credit</description>
            <correlationId>1234567890</correlationId>
         </creditUserRequest>
      </ext:creditUser>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}

### creditUser SOAP response  example

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:creditUserResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <ersReference>201708181204490000000001</ersReference>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <correlationId>1234567890</correlationId>
         </return>
      </ns2:creditUserResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}



## registerTerminal

#### registerTerminal SOAP request fields

<table>
	<tbody>
	<tr>
		<th colspan="2">registerTerminal request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>.
		</td>
	</tr>
	<tr>
		<td>externalTerminalId</td>
		<td>The identifier of the terminal in the client system.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">Store 111/Till 4</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>password</td>
		<td>Password of the registered terminal for future communications with the SEQR service.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">my_terminal_pass</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>name</td>
		<td>The name to appear on the buyer’s mobile device.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">My restaurant, cash register 2</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### registerTerminal SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">registerTerminal response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of resultCode. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>ersReference</td>
		<td>Not used, will be null.</td>
	</tr>
	<tr>
		<td>terminalId</td>
		<td>The newly generated unique identifier in SEQR system for this terminal. This identifier should be used in future communications of this terminal towards the SEQR service.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">87e791f9e24148a6892c52aa85bb0331</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

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

<table>
	<tbody>
	<tr>
		<th colspan="2">unregisterTerminal request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>. Contains terminalId of the terminal to deregister.
		</td>
	</tr>
	</tbody>
</table>

#### unregisterTerminal SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">unregisterTerminal response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of resultCode. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>ersReference</td>
		<td>Not used, will be null.</td>
	</tr>
	</tbody>
</table>

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

<table>
	<tbody>
	<tr>
		<th colspan="2">assignSeqrId request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>. The terminalId within is the terminal to which assign seqrId.
		</td>
	</tr>
	<tr>
		<td>seqrId</td>
		<td>An alphanumeric code to assign to a terminal (POS). It is used to generate a static QR code.
			<ul>
				<li>Type: <span class="seqrhl">alphanumeric</span></li>
				<li>Sample value: <span class="seqrhl">my_qr_code_string</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### assignSeqrId SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">assignSeqrId response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of resultCode. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>ersReference</td>
		<td>Not used, will be null.</td>
	</tr>
	</tbody>
</table>

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

## markTransactionPeriod

#### markTransactionPeriod request fields

<table>
	<tbody>
	<tr>
		<th colspan="2">markTransactionPeriod request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>.
		</td>
	</tr>
	<tr>
		<td>parameters</td>
		<td>An optional key-value parameter map that can be used in processing the request.
			<ul>
				<li>Sample value: see request per terminal reconciliation example.</li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### markTransactionPeriod response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">markTransactionPeriod response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of resultCode. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>transactionPeriodId</td>
		<td>The reference of this operation.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">2015100916014994401047376</span></li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

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
       <parameters>
        <parameter>
          <entry>
             <key>TERMINALID</key>
             <value>2469e0bf14214797880cafb0eda1b535</value>
          </entry>
        </parameter>
       <parameters>
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

<table>
	<tbody>
	<tr>
		<th colspan="2">executeReport request</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>context</td>
		<td>Request context information. See <a href="#clientcontext-data">context description</a>.
		</td>
	</tr>
	<tr>
		<td>reportId</td>
		<td>The identifier of the report that should be executed/produced.
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Required: <span class="seqrhl">Y</span></li>
				<li>Sample value: <span class="seqrhl">SOME_REPORT</span></li>
			</ul>
		</td>
	</tr>	
	<tr>
		<td>language</td>
		<td>The report language (null if the default language is to be used).
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>parameters</td>
		<td>An optional key-value parameter map that can be used in processing the request.
			<ul>
				<li>Sample value: see markTransactionPeriod request per terminal reconciliation example above.</li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

#### executeReport SOAP response fields

<table>
	<tbody>
	<tr>
		<th colspan="2">executeReport response</th>
	</tr>
   <col width="35%"/>
   <col width="65%"/>
	<tr>
		<th>Fields</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>resultCode</td>
		<td>Response result code.
			<ul>
				<li>Type: <span class="seqrhl">integer</span></li>
				<li>Max-length: <span class="seqrhl">2</span></li>
				<li>Sample value: <span class="seqrhl">0</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>resultDescription</td>
		<td>A textual description of resultCode. 
			<ul>
				<li>Type: <span class="seqrhl">string</span></li>
				<li>Sample value: <span class="seqrhl">SUCCESS</span></li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>report</td>
		<td>The executed/produced report, in binary and plain text form, if available. Consists of: content, contentString, mimeType, title. 
			<ul>
				<li>Content type: <span class="seqrhl">base64Binary</span></li>
				<li>ContentString type: <span class="seqrhl">string</span></li>
				<li>MimeType type: <span class="seqrhl">string</span></li>
				<li>Title type: <span class="seqrhl">string</span></li>
				<li>Sample: see response example below.</li>
			</ul>
		</td>
	</tr>
	</tbody>
</table>

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
| 29 | INVALID_INITIATOR_ PRINCIPAL_ID | Given id for TERMINALID in initiatorPrincipalId cannot be found | All requests |
| 37 | INITIATOR_PRINCIPAL_ NOT_FOUND | Given id or userId for RESELLERUSER in initiatorPrincipalId section not found in Glase | All requests |
| 49 | INVALID_INVOICE_ DATA | For example wrong currency | sendInvoice, updateInvoice |
| 50 | CANNOT_CANCEL_PAID_ INVOICE | Invoice with given reference number has already been paid | cancelInvoice |
| 51 | CANNOT_CANCEL_INVOICE_ IN_PROGRESS | | cancelInvoice |
| 53 | INVALID_SEQR_ID | Not alphanumeric string has been used or given glaseID has already been assigned to other terminal. Tip: use your own unique prefix for glaseID. Example mymerchantname31231231 | assignSeqrId |
| 54 | INVALID_INVOICE_ REFERENCE | Invoice with given reference number can't be found for given terminal id | getPaymentStatus |
| 64 | INVALID_NOTIFICATION_ URL | Not valid notificationUrl (e.g not starting with http://) | sendInvoice, updateInvoice, refundPayment |
| 90 | SYSTEM_ERROR | Unclassified errors | All requests |
| 91 | UNSUPPORTED_OPERATION | The method is not supported by the service | All requests |
| 94 | SERVICE_UNAVAILABLE | External backend system unavailable (e.g. Bank system) | All requests |
| 95 | INVOICE_ALREADY_CANCELED | Invoice with given reference number is already canceled through cancelInvoice call | cancelInvoice |
| 96 | INVOICE_STATE_NOT_RESERVED | The invoice state is not reserved for doing final or actual transaction | commitReservation |
| 97 | RESELLER_NOT_ALLOWED_ TO_DO_REFUND | Refund option is not allowed for that reseller | refundPayment |
| 98 | SUM_OF_REFUNDS_CAN_NOT_ BE_MORE_THAN_ORIGINAL_ TRANSACTION | Sum of the refunds is more than the original transaction | refundPayment |
| 99 | RECEIVER_ACCOUNT_DOES_ NOT_ALLOW_REFUNDS | External backend does not allow refund (e.g. receiver's banking system) | refundPayment |
