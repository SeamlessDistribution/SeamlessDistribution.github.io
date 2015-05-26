---
layout: default
title: eProducts
description: eProducts, eVouchers
---

# eProducts introduction

Prepaid topup, e-products, electronic distribution of all kinds of services – Seamless offers possibilities to boost your revenues with low capital investment and no shelf space. We are present through subsidiaries and partners in many countries and we are expanding fast.

On this page you will find information how to set up integration of Seamless eProducts system with Point of Sales (POS) clients. POS refers to the merchant’s cash registers as well as terminals.


# Actors
The following terms are used for the different actors involved in the integration process:

* eProducts – the Seamless electronic products distribution system
* ERS server – Seamless backend/server performing the service and the API
* ERS Client Interface – Seamless API
* Client – the type of system integrating with eProducts, such as POS, cash register and terminal
* Merchant - the company selling vouchers (can be vendor and/or cashier)
* Reseller – the retailer, selling vouchers to subscribers/customers
* Subscriber/Customer - the consumer buying vouchers

# Overview of integration steps
To achieve a full integration between eProducts and POS client these steps must be covered:

1. Create SOAP reference
2. Add values to API functions
3. Configure POS for login
4. Test that integration works

# Create SOAP reference
Get started with the integration by creating SOAP reference. Use a SOAP library to create a SOAP reference in your code. eProducts API description and test endpoint URL can be found [here](/merchant/reference/eproductsapi.html).
Test creadentials can be found [here](/merchant/reference/signup.html).

# Function requests used for POS client integration

|--- | --- |
|  Mandatory Methods | Description |
|--- | --- |
| getProductList | Returns list of available products |
| reserveVoucher | Used for purchasing a voucher in a two-phase commit manner. ERS will only keep the reservation for a limited time (configurable on the ERS, typically a few minutes) after which a buyReservedVoucher might fail |
| buyReservedVoucher | The second step in the two-phase commit procedure for buying a voucher. Can only be called after getting a successful response from a reserveVoucher call |
| cancelVoucherReservation | Used to cancel a reservation of a voucher after a successful response from a reserveVoucher call and should be called if the purchase is to be aborted |
| cancelTransaction | Allows to cancel transaction that has been finished. Using ersReference from buyReservedVoucher response (not voucher) |
| --- | --- |

|--- | --- |
|  Optional Methods | Description |
|--- | --- |
| executeReport | Allows to generate reports |
| --- | --- |

Although other functions are avaliable on the WSDL on the testing environment, those should not be used for eProducts integration.

# Configure printer for receipts
The receipt file is part of the response code. Configure the printer to include the data as shown in the sample code below, which is valid for buyVoucherResponse with FormatId as “TEXT” (HTML and VML are also supported). The information shown on receipt is configured according to each telecom operator’s specification. There are special tags that should be replaced with supported characters on POS side.

|--- | --- |
|  Tag | Description |
|--- | --- |
| &lt;large&gt; | Set large text size |
| &lt;normal&gt; | Set normal text size |
| &lt;small&gt; | Set small text size |
| &lt;left&gt; | Left align text |
| &lt;center&gt; | Center align text |
| &lt;right&gt; | Right align text |
| &lt;br&gt; | Break line |
| &lt;vs&gt; | Add vertical space |
| &lt;hs&gt; | Add horizontal space |
| &lt;img src="logo.bmp"&gt; | Print image logo.bmp |
| &lt;barcode digits="$EAN_code$"&gt; | Print product barcode |
| --- | --- |

# Operator logos

Logos that should be printed on voucher depending on retuned img tag.
All logos can be downoaded from [HERE](/downloads/logos/Logos.zip).

|---|---|
| atribute | value |
|---|---|
| Max-width | 384px |
| Max-height | No larger then Max-width |
| Colour | Monochrome | 
|---|---|

# List of operator logos

|---|---|---|
| Operator | img tag | Country |
|---|---|---|
| Telia |&lt;img src="telia_se.bmp"&gt; | Sweden |
| Tele2 |&lt;img src="tele2_se.bmp"&gt; | Sweden
| Telenor |&lt;img src="telenor_se.bmp"&gt;| Sweden | 
| TRE |&lt;img src="3_se.bmp"&gt; |  Sweden |
| IDT |&lt;img src="idt_se.bmp"&gt;| Sweden |
| Lebara |&lt;img src="lebara_se.bmp"&gt;| Sweden |
| Mundio |&lt;img src="mundio_se.bmp"&gt;| Sweden |
| LycaMobile |&lt;img src="lyca_se.bmp"&gt;| Sweden |
| Lebara |&lt;img src="lebara_dk.bmp"&gt;| Denmark |
| TDC |&lt;img src="tdc_dk.bmp"&gt;| Denmark |
| Telia |&lt;img src="telia_dk.bmp"&gt;| Denmark |
| Oister |&lt;img src="oister_dk.bmp"&gt;| Denmark |
| Telenor |&lt;img src="telenor_dk.bmp"&gt;| Denmark |
| CBB |&lt;img src="cbb_dk.bmp"&gt;| Denmark |
| One Mobile |&lt;img src="one_dk.bmp"&gt;| Denmark |
| Colour Mobile |&lt;img src="colour_dk.bmp"&gt;| Denmark |
| LycaMobile |&lt;img src="lyca_dk.bmp"&gt;| Denmark |
| IDT |&lt;img src="idt_dk.bmp"&gt;| Denmark |
| Mundio |&lt;img src="mundio_dk.bmp"&gt;| Denmark |
| Telepost |&lt;img src="telepost_dk.bmp"&gt;| Denmark |
|---|---|---|

# Sample voucher

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<ns2:buyVoucherResponse xmlns:ns2="http://externalws.client.ers.seamless.com/">
<return>
<errorDescription>SUCCESS</errorDescription>
<ersReference>2013071914473764701002923</ersReference>
<resultCode>0</resultCode>
<productEAN>7330596001123</productEAN>
<productName><name of product> 100KR</productName>
<productSKU>10053</productSKU>
<receipt>
	<img src="telia_se.bmp">
	Värdebevis
<vs>
---------
2013/07/19 14:47:37
<vs>
<name of voucher> 100KR
<vs>
EAN:7330596001123
<vs>
Värdebevis: 100 SEK
<vs>
SÄKERHETSKOD <vs>
-------------------------<vs>
9140000014 <vs>
-------------------------<vs>
FÖR ATT TANKA PÅ DITT KORT SLÅ *110*SÄKERHETSKOD# OCH LUR
Giltigt fram till:2014/01/01
<vs>
Serienumber: 9140014
<vs>
VID PROBLEM MED
<vs>
LADDNING KONTAKTA 13
<vs>
<Operator> KUNDTJÄNST PÅ 
<barcode digits="7330596001123">
<phone number>
</receipt>
<voucher>
 <code>9140000014</code>
 <expiryDate>2014-01-01T00:00:00+01:00</expiryDate>
 <serial>9140014</serial>
</voucher>
</return>
</ns2:buyVoucherResponse>
</soap:Body>
</soap:Envelope>
{% endhighlight %}



# Two step voucher purchase
In a realistic scenario, the POS client wants to be very sure that the purchase goes through after it has received the payment/allocated the funds. This can be accomplished by using a two-phase commit procedure using reserveVoucher and buyReservedVoucher.
Note! Although this procedure minimizes the risk that the purchase fails this is no 100% guarantee. This means that the POS client must always have a procedure for handling a failed purchase, even if it is a manual procedure!

1. Reserve voucher, calling reserveVoucher. If this fails, return error message to customer.
2. Confirm the purchase with the customer, if cancelled the voucher reservation should be cancelled with cancelVoucherReservation.
3. Complete and verify the customer payment. How this is done is up to the client, but it will typically send a payment request to a payment system. If the payment fails, the voucher reservation should be cancelled with cancelVoucherReservation and the purchase be aborted.
4. Buy the reserved voucher using buyReservedVoucher.
5. Print/present the voucher returned by eProducts.

# Verification
When merchant has notified Seamless that all work is done, a certification test is performed by Seamless together with the merchant/vendor.
The certification flows are the following:

1. Getting product list using getProductList.
2. Reserving a voucher and buying it. Note that the system should allow buying more than one voucher in single transaction.
3. Reserving a voucher and canceling it. All vouchers should be cancelled if there is more than one for a single transaction.
4. Reserving and buying a voucher then refunding it using cancelTransaction (using ersReference from buyReservedVoucher response).
5. Getting reports using executeReport method (if implemented).
6. Error handling.
7. Printed voucher receipt verification. There should be a way to scan and send the printed receipt to Seamless during the certification.
