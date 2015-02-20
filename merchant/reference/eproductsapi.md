---
layout: default
title: eProducts API
description: eProducts API reference
---

# Table of content

1. [eProducts API](#eproducts-api)
2. [Function requests used for POS client integration](#function-requests-used-for-pos-client-integration)
3. [Mandatory Methods](#mandatory-methods)
	* [getProductsList](#getproductslist)
	* [reserveVoucher](#reservevoucher)
	* [buyReservedVoucher](#buyreservedvoucher)
	* [cancelVoucherReservation](#cancelvoucherreservation)
	* [cancelTransaction](#canceltransaction)
4. [Optional Methods](#optional-methods)
	* [executeReport](#executereport)
5. [Response Codes](#response-codes)

# 1. eProducts API

This is a description of our SOAP-WS-API for merchants, our test WSDL is available at: 
http://extdev.kontantkort.nu/extclientproxy/client?wsdl

[Up](#table-of-content)

# 2. Function requests used for POS client integration 
Below you will find methods used in POS and eProducts integration.
This is part of eProducts API. Methods not listed belowe shall not be implemented.

[Up](#table-of-content)

# 3. Mandatory Methods
These methods have to be implemented in order to pass our certification get production access.

[Up](#table-of-content)

### getProductsList
Returns list of available product.

[Up](#table-of-content)

#### getProductList request

|--- | --- | --- | --- | --- | 
|  Field | Required | Type | Sample Value | Description |
|--- | --- | --- | --- | --- | 
| channel | yes | String | WS | Needs to be set to WS|
| clientId | yes | String | reseller123 | clientId provided by Seamless or from [here](/merchant/reference/signup.html) |
|clientRequestTimeout | yes | decimal | 0 | Timeout requested from the client´s side. We highly recommend to leave it to zero for an immediate response. Use different than 0 only if it´s a special situation. |
| clientUserId | yes | decimal | 9900 | Use 9900 unless provided with different clientUserId |
| password | yes | String | p@55w0Rd | password provided by Seamless or from [here](/merchant/reference/signup.html) |
|--- | --- | --- | --- | --- | 

{% highlight python %}
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ext="http://externalws.client.ers.seamless.com/">
    <soapenv:Header />
    <soapenv:Body>
        <ext:getProductList>
            <context>
                <channel>web</channel>
                <clientId>test_id</clientId>
                <password>abc123</password>
                <clientRequestTimeout>0</clientRequestTimeout>
                <clientUserId>9900</clientUserId>
            </context>
        </ext:getProductList>
    </soapenv:Body>
</soapenv:Envelope>
{% endhighlight %}

[Up](#table-of-content)

#### getProductList response

|--- | --- | --- | --- |
| Field | Type | Sample value | Description |
|--- | --- | --- | --- |
| errorDescription | String | SUCCESS | Description of the status of the response |
| ersReference | String | 2014071814275177901000128 | Trackable number of the voucher in ERS system of the request. To be used with buyReservedVoucher and cancelVoucherReservation requests |
| resultCode | decimal | 0 | Response result code. See posible result codes at the bottom of this page |
| name | String | GT Mobile | Name of a supplier |
| currency | String | SEK | Currency code |
| value | decimal | 70 | Product price |
| ean | String | 7330596005932 | Product ean |
| sku | String | 3453433 | Product sku |
| name | String | Some name | Product name |
|--- | --- | --- | --- |

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:getProductListResponse xmlns:ns2="http://externalws.client.ers.seamless.com/">
         <return>
            <errorDescription>Success</errorDescription>
            <ersReference>2014111710075839201000024</ersReference>
            <resultCode>0</resultCode>
            <suppliers>
               <name>Test Supplier</name>
               <products>
                  <customerPrice>
                     <currency>SEK</currency>
                     <value>70</value>
                  </customerPrice>
                  <ean>7330596005932</ean>
                  <name>Test Product Name</name>
                  <sku>10181</sku>
               </products>
            </suppliers>
         </return>
      </ns2:getProductListResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

[Up](#table-of-content)

### reserveVoucher
Used for purchasing a voucher in a two-phase commit manner. ERS will only keep the reservation for a limited time (configurable on the ERS, typically a few minutes) after which a buyReservedVoucher might fail.

[Up](#table-of-content)

#### reserveVoucher request ####

|--- | --- | --- | --- | --- | 
|  Field | Required | Type | Sample Value | Description |
|--- | --- | --- | --- | --- | 
| channel | yes | String | WS | Needs to be set to WS|
| clientId | yes | String | reseller123 | clientId provided by Seamless or from [here](/merchant/reference/signup.html) |
|clientRequestTimeout | yes | decimal | 0 | Timeout requested from the client´s side.
We highly recommend to leave it to zero for an immediate response. Use different than 0 only if it´s a special situation. |
| clientUserId | yes | decimal | 9900 | Use 9900 unless provided with different clientUserId |
| password | yes | String | p@55w0Rd | password provided by Seamless or from [here](/merchant/reference/signup.html) |
| clientComment | no | String | Some comment | Can be used to add additional information from the client system |
| clientReference | no | String | 823429834723948 | Reference of the transaction in clients system |
| clientTag | no | String | POS007 | Tracking tag from the clients system (i.e: cash register ID) |
| productId | yes | String | ean:7332023036197 | The ean or sku number of the voucher that is being reserved. Needs to be prefixed by "sku:" or "ean:". List of available skus and eans can be obtained by getProductList call |
|--- | --- | --- | --- | --- | 

{% highlight python %}
<soapenv:Envelope 
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
Xmlns:ext="http://externalws.client.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <ext:reserveVoucher>
         <context>
            <channel>WS</channel>
            <clientId>Test</clientId>
            <clientRequestTimeout>0</clientRequestTimeout>
            <clientUserId>9900</clientUserId>
            <password>123456678123</password>
         </context>
         <transactionData>
            <clientComment>?</clientComment>
            <clientReference>?</clientReference>
            <clientTag>?</clientTag>
         </transactionData>
         <productId>ean:7332023036197</productId>
      </ext:reserveVoucher>
   </soapenv:Body>
</soapenv:Envelope>
{% endhighlight %}

[Up](#table-of-content)

#### reserveVoucher response

|--- | --- | --- | --- |
| Field | Type | Sample value | Description |
|--- | --- | --- | --- |
| errorDescription | String | SUCCESS | Description of the status of the response |
| ersReference | String | 2014071814275177901000128 | Trackable number of the voucher in ERS system of the request. To be used with buyReservedVoucher and cancelVoucherReservation requests |
| resultCode | decimal | 0 | Response result code. See posible result codes at the bottom of this page |
|--- | --- | --- | --- |

{% highlight python %}
<soap:Envelope 
Xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:reserveVoucherResponse 
Xmlns:ns2="http://externalws.client.ers.seamless.com/">
         <return>
            <errorDescription>SUCCESS</errorDescription>
            <ersReference>2014071814275177901000128</ersReference>
            <resultCode>0</resultCode>
         </return>
      </ns2:reserveVoucherResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

[Up](#table-of-content)

### buyReservedVoucher 
The second step in the two-phase commit procedure for buying a voucher. Can only be called after getting a successful response from a reserveVoucher call.

[Up](#table-of-content)

#### buyReservedVoucher request

|--- | --- | --- | --- | --- | 
|  Field | Required | Type | Sample Value | Description |
|--- | --- | --- | --- | --- | 
| channel | yes | String | WS | Needs to be set to WS|
| clientId | yes | String | reseller123 | clientId provided by Seamless or from [here](/merchant/reference/signup.html) |
|clientRequestTimeout | yes | decimal | 0 | Timeout requested from the client´s side. We highly recommend to leave it to zero for an immediate response. Use different than 0 only if it´s a special situation. |
| clientUserId | yes | decimal | 9900 | Use 9900 unless provided with different clientUserId |
| password | yes | String | p@55w0Rd | password provided by Seamless or from [here](/merchant/reference/signup.html) |
| ersReference | yes | String | 2014071716555003001000100 | ersReference of the reserved voucher returned by reserveVoucher response |
| receiptFormatId | yes | String | TEXT | Needs to be set to one of the following: VML, TEXT, HTML |
|--- | --- | --- | --- | --- | 

{% highlight python %}
<soapenv:Envelope 
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
Xmlns:ext="http://externalws.client.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <ext:buyReservedVoucher>
         <context>
            <channel>WS</channel>
            <clientId>Test</clientId>
            <clientRequestTimeout>0</clientRequestTimeout>
            <clientUserId>9900</clientUserId>
            <password>123456678123</password>
         </context>
         <ersReference>2014071716555003001000100</ersReference>
         <receiptFormatId>VML</receiptFormatId>
      </ext:buyReservedVoucher>
   </soapenv:Body>
</soapenv:Envelope>
{% endhighlight %}

[Up](#table-of-content)

#### buyReserverdVoucher response

|--- | --- | --- | --- |
| Field | Type | Sample value | Description |
|--- | --- | --- | --- |
| errorDescription | String | SUCCESS | Description of the status of the response |
| ersReference | String | 2014071814275177901000128 | Trackable number of the voucher in ERS system of the request. To be used with buyReservedVoucher and cancelVoucherReservation requests |
| resultCode | decimal | 0 | Response result code. See posible result codes at the bottom of this page |
| productEAN | String | 7332023036197 | EAN number of the product (voucher) that was bought |
| productName | String | Årskort 999KR | Name of the product |
| productSKU | String | 19016 | SKU number of the product |
| receipt | String | Sample receipt can be found [here](/merchant/eproducts) | Content to be parsed on POS side, printed and provided to the customer|
| code | String | 380000080 | Code of the generated voucher |
| expiryDate | date | 2014-01-01T00:00:00+01:00 | Voucher's date of expiration |
| serial | String | 380080 | Serial number of the voucher |
|--- | --- | --- | --- |

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:buyReservedVoucherResponse xmlns:ns2="http://externalws.client.ers.seamless.com/">
         <return>
            <errorDescription>SUCCESS</errorDescription>
            <ersReference>2014071814355935801000131</ersReference>
            <resultCode>0</resultCode>
            <productEAN>7332023036197</productEAN>
            <productName>Årskort 999KR</productName>
            <productSKU>19016</productSKU>
            <receipt> …........ </receipt>
            <voucher>
               <code>380000080</code>
               <expiryDate>2014-01-01T00:00:00+01:00</expiryDate>
               <serial>380080</serial>
            </voucher>
         </return>
      </ns2:buyReservedVoucherResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

[Up](#table-of-content)

### cancelVoucherReservation
Used to cancel a reservation of a voucher after a successful response from a reserveVoucher call and should be called if the purchase is to be aborted.

[Up](#table-of-content)

#### cancelVoucherReservation request

|--- | --- | --- | --- | --- | 
|  Field | Required | Type | Sample Value | Description |
|--- | --- | --- | --- | --- | 
| channel | yes | String | WS | Needs to be set to WS|
| clientId | yes | String | reseller123 | clientId provided by Seamless or from [here](/merchant/reference/signup.html) |
|clientRequestTimeout | yes | decimal | 0 | Timeout requested from the client´s side. We highly recommend to leave it to zero for an immediate response. Use different than 0 only if it´s a special situation. |
| clientUserId | yes | decimal | 9900 | Use 9900 unless provided with different clientUserId |
| password | yes | String | p@55w0Rd | password provided by Seamless or from [here](/merchant/reference/signup.html) |
| ersReference | yes | String | 2014071716555003001000100 | ersReference of the reserved voucher returned by reserveVoucher response |
| receiptFormatId | yes | String | TEXT | Needs to be set to one of the following: VML, TEXT, HTML |
|--- | --- | --- | --- | --- | 

{% highlight python %}
<soapenv:Envelope 
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
Xmlns:ext="http://externalws.client.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <ext:cancelVoucherReservation>
         <context>
            <channel>WS</channel>
            <clientId>Test</clientId>
            <clientRequestTimeout>0</clientRequestTimeout>
            <clientUserId>9900</clientUserId>
            <password>123456678123</password>
         </context>
         <ersReference>2014071716555003001000100</ersReference>
      </ext:cancelVoucherReservation>
   </soapenv:Body>
</soapenv:Envelope>
{% endhighlight %}

[Up](#table-of-content)

#### cancelVoucherReservation response

|--- | --- | --- | --- |
| Field | Type | Sample value | Description |
|--- | --- | --- | --- |
| errorDescription | String | SUCCESS | Description of the status of the response |
| ersReference | String | 2014071814275177901000128 | Trackable number of cancelation in the ERS system |
| resultCode | decimal | 0 | Response result code. See posible result codes at the bottom of this page |
|--- | --- | --- | --- | 	

{% highlight python %}
<soap:Envelope 
Xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:reserveVoucherResponse 
Xmlns:ns2="http://externalws.client.ers.seamless.com/">
         <return>
            <errorDescription>SUCCESS</errorDescription>
            <ersReference>2014071814275177901000128</ersReference>
            <resultCode>0</resultCode>
         </return>
      </ns2:reserveVoucherResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

[Up](#table-of-content)

### cancelTransaction
Allows to cancel transaction that has been finished. Using ersReference from buyReservedVoucher response (not voucher).

[Up](#table-of-content)

#### cancelTransaction request

|--- | --- | --- | --- | --- | 
|  Field | Required | Type | Sample Value | Description |
|--- | --- | --- | --- | --- | 
| channel | yes | String | WS | Needs to be set to WS|
| clientId | yes | String | reseller123 | clientId provided by Seamless or from [here](/merchant/reference/signup.html) |
|clientRequestTimeout | yes | decimal | 0 | Timeout requested from the client´s side. We highly recommend to leave it to zero for an immediate response. Use different than 0 only if it´s a special situation.|
| clientUserId | yes | decimal | 9900 | Use 9900 unless provided with different clientUserId |
| password | yes | String | p@55w0Rd | password provided by Seamless or from [here](/merchant/reference/signup.html) |
| clientComment | no | String | Some comment | Can be used to add additional information from the client system |
| clientReference | no | String | 823429834723948 | Reference of the transaction in clients system |
| clientTag | no | String | POS007 | Tracking tag from the clients system (i.e: cash register ID) |
| ersReference | yes | String | 2014110515155960201000883 | ersReference from buyReservedVoucher response of voucher to be refunded |
| verificationCode | no | String | 803987373939 | The verification code for the cancellation, if required |
| reasonCode | no | decimal | 03 | The code categorizing the reason for the cancellation. 01 - Cashier mistake, 02 - Technical error, 03 - Customer mistake, 11 - Code unusable |
|--- | --- | --- | --- | --- | 

{% highlight python %}
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ext="http://externalws.client.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <ext:cancelTransaction>
         <context>
            <channel>?</channel>
            <clientId>?</clientId>
            <clientRequestTimeout>?</clientRequestTimeout>
            <clientUserId>?</clientUserId>
            <password>?</password>
         </context>
         <transactionData>
            <clientComment>?</clientComment>
            <clientReference>?</clientReference>
            <clientTag>?</clientTag>
         </transactionData>
         <ersReference>?</ersReference>
         <verificationCode>?</verificationCode>
         <reasonCode>?</reasonCode>
         <reason>?</reason>
      </ext:cancelTransaction>
   </soapenv:Body>
</soapenv:Envelope>
{% endhighlight %}

[Up](#table-of-content)

#### cancelTransaction response

|--- | --- | --- | --- |
| Field | Type | Sample value | Description |
|--- | --- | --- | --- |
| errorDescription | String | SUCCESS | Description of the status of the response |
| ersReference | String | 2014071814275177901000128 | Trackable number of cancelation in the ERS system |
| resultCode | decimal | 0 | Response result code. See posible result codes at the bottom of this page |
|--- | --- | --- | --- | 	

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:cancelTransactionResponse xmlns:ns2="http://externalws.client.ers.seamless.com/">
         <return>
            <errorDescription>SUCCESS</errorDescription>
            <resultCode>0</resultCode>
            <ersReference>2014111312525268801000008</ersReference>
         </return>
      </ns2:cancelTransactionResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

[Up](#table-of-content)

# 4. Optional Methods
These methods have to be implemented in order to pass our certification get production access.

[Up](#table-of-content)

### executeReport 
Allows to generate reports.

#### executeReport request

|--- | --- | --- | --- | --- | 
|  Field | Required | Type | Sample Value | Description |
|--- | --- | --- | --- | --- | 
| channel | yes | String | WS | Needs to be set to WS|
| clientId | yes | String | reseller123 | clientId provided by Seamless or from [here](/merchant/reference/signup.html) |
|clientRequestTimeout | yes | decimal | 0 | Timeout requested from the client´s side. We highly recommend to leave it to zero for an immediate response. Use different than 0 only if it´s a special situation. |
| clientUserId | yes | decimal | 9900 | Use 9900 unless provided with different clientUserId |
| password | yes | String | p@55w0Rd | password provided by Seamless or from [here](/merchant/reference/signup.html) |
| clientComment | no | String | Some comment | Can be used to add additional information from the client system |
| clientReference | no | String | 823429834723948 | Reference of the transaction in clients system |
| reportId | yes | String | repo:///terminal/ REP_TERM_CASHIER_SALES_PERIOD.xml | Type of report that you'd like to get |
| language | yes | String | en | Language of report. Currently available are "en" for English and "sv" for Swedish|
| key | yes | Sring | resellerId | Name of the parameter. Different types of reports require diffrent parametrs. Check below example request to see differences |
| value | yes | String | someresellerid | Value of the parameter |
|--- | --- | --- | --- | --- | 

#### executeReport response

|--- | --- | --- | --- |
| Field | Type | Sample value | Description |
|--- | --- | --- | --- |
| errorDescription | String | SUCCESS | Description of the status of the response |
| resultCode | decimal | 0 | Response result code. See posible result codes at the bottom of this page |
| content | String | Cgo8YnI+Cjxp... | Contains report in base64 form |
| contentString | String | See examples below | content of the report |
|--- | --- | --- | --- | 

[Up](#table-of-content)

#### executeReport CASHIER_SALES_PERIOD example

{% highlight python %}
<!--REQUEST-->

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ext="http://externalws.client.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <ext:executeReport>
         <context>
            <channel>TERMINAL</channel>
            <clientId>test</clientId>
            <clientRequestTimeout>0</clientRequestTimeout>
            <clientUserId>9900</clientUserId>
            <password>123456</password>
         </context>
         <transactionData>
            <clientComment>TEST</clientComment>
            <clientReference>001001</clientReference>
         </transactionData>
         <reportId>repo:///terminal/REP_TERM_CASHIER_SALES_PERIOD.xml</reportId>
         <language>en</language>
         <parameters>
            <parameter>
               <entry>
                  <key>resellerId</key>
                  <value>test</value>
               </entry>
               <entry>
                  <key>user</key>
                  <value>9900</value>
               </entry>
               <entry>
                  <key>startTime</key>
                  <value>2014-01-01 00:00:00</value>
               </entry>
               <entry>
                  <key>endTime</key>
                  <value>2014-12-01 00:00:00</value>
               </entry>
            </parameter>
         </parameters>
      </ext:executeReport>
   </soapenv:Body>
</soapenv:Envelope>
{% endhighlight %}


{% highlight python %}
<!--RESPOSNE-->

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:executeReportResponse xmlns:ns2="http://externalws.client.ers.seamless.com/">
         <return>
            <errorDescription>SUCCESS</errorDescription>
            <resultCode>0</resultCode>
            <reportData>
               <content>Cgo8YnI+Cjxp...</content>
               <contentString><![CDATA[<br>
                  <img=seamless.bmp><br><br>
                  <center><large>Cashier Sales Summary over period
                  <line><normal>
                  <br>
                  <br>
                  <br><align=2><left>Reseller ID<right>DIST1
                  <br><align=2><left>Cashier<right>webuser
                  <br><align=2><left>Start<right>2014-01-01 00:00:00
                  <br><align=2><left>End<right>2014-12-01 00:00:00
                  <br>
                  <br>
                  <align=3><left>Product<center>Count<right>Amount
                  <line>
                  <br>
                  
                  <line>
                  <align=3><left>Total<center>0<right>0,00 SEK
                  <line>
                  <br>]]>
               </contentString>
               <mimeType>text/html</mimeType>
               <title/>
            </reportData>
         </return>
      </ns2:executeReportResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

[Up](#table-of-content)

#### executeReport CASHIER_WORKSHIFT example

{% highlight python %}
<!--REQUEST -->

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ext="http://externalws.client.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <ext:executeReport>
         <context>
            <channel>TERMINAL</channel>
            <clientId>test</clientId>
            <clientRequestTimeout>0</clientRequestTimeout>
            <clientUserId>9900</clientUserId>
            <password>123456</password>
         </context>
         <transactionData>
            <clientComment>TEST</clientComment>
            <clientReference>001001</clientReference>
         </transactionData>
         <reportId>repo:///terminal/REP_TERM_TARGET_WORKSHIFT.xml</reportId>
         <language>en</language>
         <parameters>
            <parameter>
               <entry>
                  <key>resellerId</key>
                  <value>test</value>
               </entry>
               <entry>
                  <key>targetUser</key>
                  <value>9900</value>
               </entry>
               <entry>
                  <key>terminalId</key>
                  <value>001</value>
               </entry>
            </parameter>
         </parameters>
      </ext:executeReport>
   </soapenv:Body>
</soapenv:Envelope>
{% endhighlight %}

{% highlight python %}
<!--RESPONSE-->

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:executeReportResponse xmlns:ns2="http://externalws.client.ers.seamless.com/">
         <return>
            <errorDescription>SUCCESS</errorDescription>
            <resultCode>0</resultCode>
            <reportData>
               <content>CgoKCjxicj4...</content>
               <contentString><![CDATA[<br>
                  <img=seamless.bmp><br><br>                  
                  <center><large>Cashier Workshift
                  <line><normal>
                  <br>
                  <br>
                  <br><align=2><left>Terminal ID<right>001
                  <br><align=2><left>Cashier<right>webuser
                  <br><align=2><left>Start<right>2014-11-24 00:00:00
                  <br><align=2><left>End<right>2014-11-24 13:55:23
                  <br>
                  <br>
                  <align=3><left>Product<center>Count<right>Amount
                  <line>
                  <br>
                  
                  <line>
                  <align=3><left>Total<center>0<right>0,00 SEK
                  <line>
                  <br>]]>
               </contentString>
               <mimeType>text/html</mimeType>
               <title/>
            </reportData>
         </return>
      </ns2:executeReportResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

[Up](#table-of-content)

#### executeReport RESELLER_INFO example

{% highlight python %}
<!--REQUEST-->

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ext="http://externalws.client.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <ext:executeReport>
         <context>
            <channel>TERMINAL</channel>
            <clientId>test</clientId>
            <clientRequestTimeout>0</clientRequestTimeout>
            <clientUserId>9900</clientUserId>
            <password>123456</password>
         </context>
         <transactionData>
            <clientComment>TEST</clientComment>
            <clientReference>001001</clientReference>
         </transactionData>
         <reportId>repo:///terminal/REP_TERM_RESELLER_INFO.xml</reportId>
         <language>en</language>
         <parameters>
            <parameter>
               <entry>
                  <key>resellerId</key>
                  <value>test</value>
               </entry>
            </parameter>
         </parameters>
      </ext:executeReport>
   </soapenv:Body>
</soapenv:Envelope>
{% endhighlight %}

{% highlight python %}
<!--RESPONSE-->

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:executeReportResponse xmlns:ns2="http://externalws.client.ers.seamless.com/">
         <return>
            <errorDescription>SUCCESS</errorDescription>
            <resultCode>0</resultCode>
            <reportData>
               <content>Cgo8YnI+Cj...</content>
               <contentString><![CDATA[<br>
                  <img=seamless.bmp><br><br>
                  
                  <center><large>Reseller Information
                  <line><normal>
                  
                  <br><align=2><left>Reseller ID<right>DIST1
                  <br><align=2><left>Terminal ID<right>?terminalId(terminalId)?
                  <br><align=2><left>A/C status<right>Active
                  <br>
                  
                  <line>
                  <br><align=2><left>Balance<right>0,00 SEK
                  <br>
                  <line>
                  <line>]]>
               </contentString>
               <mimeType>text/html</mimeType>
               <title/>
            </reportData>
         </return>
      </ns2:executeReportResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

[Up](#table-of-content)

#### executeReport RESELLER_SALES_PERIOD example

{% highlight python %}
<!--REQUEST-->

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ext="http://externalws.client.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <ext:executeReport>
         <context>
            <channel>TERMINAL</channel>
            <clientId>test</clientId>
            <clientRequestTimeout>0</clientRequestTimeout>
            <clientUserId>9900</clientUserId>
            <password>123456</password>
         </context>
         <transactionData>
            <clientComment>TEST</clientComment>
            <clientReference>001001</clientReference>
         </transactionData>
         <reportId>repo:///terminal/REP_TERM_RESELLER_SALES_PERIOD.xml</reportId>
         <language>en</language>
         <parameters>
            <parameter>
               <entry>
                  <key>resellerId</key>
                  <value>test</value>
               </entry>
               <entry>
                  <key>startTime</key>
                  <value>2014-01-01 00:00:00</value>
               </entry>
               <entry>
                  <key>endTime</key>
                  <value>2014-12-01 00:00:00</value>
               </entry>
            </parameter>
         </parameters>
      </ext:executeReport>
   </soapenv:Body>
</soapenv:Envelope>
{% endhighlight %}


{% highlight python %}
<!--RESPONSE-->

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:executeReportResponse xmlns:ns2="http://externalws.client.ers.seamless.com/">
         <return>
            <errorDescription>SUCCESS</errorDescription>
            <resultCode>0</resultCode>
            <reportData>
               <content>Cgo8YnI+...</content>
               <contentString><![CDATA[<br>
                  <img=seamless.bmp><br><br>
                  
                  <center><large>Sales Summary over period
                  <line><normal>
                  <br>
                  <br>
                  <br><align=2><left>Reseller ID<right>DIST1
                  <br><align=2><left>Start<right>2014-01-01 00:00:00
                  <br><align=2><left>End<right>2014-12-01 00:00:00
                  <br>
                  <br>
                  <align=3><left>Product<center>Count<right>Amount
                  <line>
                  <br>
                  
                  <line>
                  <align=3><left>Total<center>0<right>0,00 SEK
                  <line>
                  <br>]]>
               </contentString>
               <mimeType>text/html</mimeType>
               <title/>
            </reportData>
         </return>
      </ns2:executeReportResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

[Up](#table-of-content)

#### executeReport WORKSHIFT example

{% highlight python %}
<!--REQUEST-->

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ext="http://externalws.client.ers.seamless.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <ext:executeReport>
         <context>
            <channel>TERMINAL</channel>
            <clientId>test</clientId>
            <clientRequestTimeout>0</clientRequestTimeout>
            <clientUserId>9900</clientUserId>
            <password>123456</password>
         </context>
         <transactionData>
            <clientComment>TEST</clientComment>
            <clientReference>001001</clientReference>
         </transactionData>
         <reportId>repo:///terminal/REP_TERM_WORKSHIFT.xml</reportId>
         <language>en</language>
         <parameters>
            <parameter>
               <entry>
                  <key>user</key>
                  <value>9900</value>
               </entry>
               <entry>
                  <key>terminalId</key>
                  <value>001</value>
               </entry>
            </parameter>
         </parameters>
      </ext:executeReport>
   </soapenv:Body>
</soapenv:Envelope>
{% endhighlight %}

{% highlight python %}
<!--REPOSNE-->

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:executeReportResponse xmlns:ns2="http://externalws.client.ers.seamless.com/">
         <return>
            <errorDescription>SUCCESS</errorDescription>
            <resultCode>0</resultCode>
            <reportData>
               <content>CgoKCjxicj4KPGlt...</content>
               <contentString>
                  <![CDATA[<br>
                  <img=seamless.bmp><br><br>
                  
                  <center><large>Workshift Report
                  <line><normal>
                  <br>
                  <br>
                  <br><align=2><left>Terminal ID<right>001
                  <br><align=2><left>Cashier<right>webuser
                  <br><align=2><left>Start<right>2014-11-24 00:00:00
                  <br><align=2><left>End<right>2014-11-24 14:29:16
                  <br>
                  <br>
                  <align=3><left>Product<center>Count<right>Amount
                  <line>
                  <br>
                  
                  <line>
                  <align=3><left>Total<center>0<right>0,00 SEK
                  <line>
                  <br>]]>
               </contentString>
               <mimeType>text/html</mimeType>
               <title/>
            </reportData>
         </return>
      </ns2:executeReportResponse>
   </soap:Body>
</soap:Envelope>
{% endhighlight %}

[Up](#table-of-content)

# 5. Response Codes

|--- | --- | --- | --- |
| Code | Description | Detailed description | Can occur |
|--- | --- | --- | --- |
| 78 | The transaction has already been reversed. Transaction ID: 2015012716100420301000413 | Voucher has been bought and refunded | buyReservedVoucher |
| 78 | The specified transaction is in illegal state for this operation. | Voucher already bought | buyReservedVoucher, cancelVoucherReservation |
| 79 | You are not found in the system. | Provided incorrect credentials (clientId or clientUserId) | Any method |
| 79 | The given password is not correct | Provided password is incorrect | Any method |
| 90 | You provided an unknown product SKU/EAN. Please try again with an existing product SKU/EAN. | | reserveVoucher |
| 90 | SYSTEM_ERROR: Missing parameter resellerId ! | reportId key/value is missing in executeReport request where it is required| executeReport |
| 90 | SYSTEM_ERROR: Report not found! | wrong reportId | executeReport |
| 90 | SYSTEM_ERROR: Unable to find layout for language: | wrong language value | executeReport |
| 91 | The specified transaction could not be found. | Wrong ersReference | buyReservedVoucher, cancelVoucherReservation, cancelTransaction |
|--- | --- | --- | --- |

[Up](#table-of-content)