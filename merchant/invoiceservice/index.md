---
layout: default
title: SEQR Invoice Service
description: SEQR Invoice Service
---

# SEQR Invoice Service introduction

This page describes how QR codes for SEQR Invoice Service should be constructed by issuers. Issuer is a company who wishes to distribute QR codes in an invoice among their consumers scanning of which starts the payment process of an invoice associated with the QR code.

Please become familiar with guidelines for printing SEQR QR codes attached to [this document](/downloads/seqr-qrcode-print-guidelines.pdf).

<b>Before integrating with SEQR Invoice service contact Seamless to obtain:</b>

* Issuer name
* Secret key for the issuer


# SEQR Invoice Service QR code

An example QR code for Invoice Service looks as follows:

{% highlight python %}
   HTTP://SEQR.SE/000/invoice?i=abc&d=Phone%20invoice%2005.2015
   &a=100&c=SEK&r=73782174&o=true
   &h=99fd26ca2e1e28324e45465c0f9949c474d2544e0ccb8474d12930c72235fddb
{% endhighlight %}

(all in one line)

The rules governing the creation of a QR code are summarized in a table below.

|---| --- | --- |
| QR code element | Mandatory | Description |
|---| --- | --- |
| HTTP://SEQR.SE/000/invoice? | Y | this part is compulsory and a QR code must start with it |
| i=&lt;issuer_name&gt; | Y | &lt;issuer_name&gt; should be replaced with a name provided by SEQR for an issuer during the onboarding procedure |
| d=&lt;description&gt; | Y | Max 50-characters long description of the invoice. Allowed characters: alphanumeric, white spaces, braces, dash, slash, comma, dot, single and double quotes. ([A-Zaz\w.,\(\)-\\\\/\"\'])+ |
| a=&lt;amount&gt; | Y | Amount to be paid, numerical value with a precision up to 2 decimal points, eg. 100.00 (with a dot '.' being the decimal seperator). |
| c=&lt;currency&gt; | Y | 3-characters long currency |
| r=&lt;issuers_reference&gt; | Y | Max 30-characters long unique reference of the invoice. It is set up by an issuer. Allowed characters: alphanumeric, white spaces, braces, dash, slash, comma, dot, single and double quotes. ([A-Zaz\w.,\(\)-\\\\/\"\'])+ |
| o=&lt;true or false&gt; | N | if set to true the invoice can be paid only once; default value: false - it means that invoice identified by the same reference can be paid several times. |
| h=&lt;hash_of_invoice&gt; | Y | SHA-256 hash which is a derivative of the URL. It protects against any changes introduced to the QR code by a non-issuer. The algorithm for computing the checksum is explained in the dedicated chapter below. |
|--- | --- | --- |

Parameters: issuer, description, amount, currency, reference and h can be placed in the QR code after '?' character in any order.


# Hash computation

Let us assume that there is the following QR code representing the invoice to be paid.

{% highlight python %}
   HTTP://SEQR.SE/000/invoice?i=abc&d=Phone%20invoice%2005.2015
   &a=100.00&c=SEK&r=73782174
   &h=22ef08bdc0fe9693ca4a65e3bfec3d927108fc47be9889b1001fd6f613f6e3b3
{% endhighlight %}

(all in one line)

The following QR code consists of the parameters:

|---|---|---|
| Param name | Param value |
|---|---|---|
| a | 100.00 |
| c | SEK |
| d | Phone invoice 05.2015 |
| h | 22ef08bdc0fe9693ca4a65e3bfec3d927108fc47be9889b1001fd6f613f6e3b3 |
| i | abc |
| r | 73782174 |
|---|---|---|

To compute the hash (the value of 'h' paramater) one should do the following:

1. Take value of 'issuer' parameter
2. Append to it value of 'description' parameter
3. Append to it value of 'amount' parameter
4. Append to it value of 'currency' parameter
5. Append to it value of 'reference' parameter
6. If 'once' is present, append to it value of 'once' parameter
7. Append to it a secret string for issuer. Secret string will be provided to an issuer during the onboarding process. 
   In this instruction, let us asume that the secret string is: SECRET_STRING_FOR_ISSUER.
8. Transform any upper-case letters in the string into lower-case letters.
9. Compute SHA-256 out of the final string. The resulting hash is a value of 'h' parameter.

Hash is computed for strings in utf-8 format. This should be supported by default by any major development platform.

# Hash computing examples

<b>Example #1</b>

QR code (urlencoded)

{% highlight python %}
   HTTP://SEQR.SE/000/invoice?i=abc&d=Phone%20invoice%2005.2015
   &a=100.00&c=SEK&r=73782174
   &h=22ef08bdc0fe9693ca4a65e3bfec3d927108fc47be9889b1001fd6f613f6e3b3
{% endhighlight %}

(all in one line)

The input string for computing the hash (after point 8 in the instruction above) is:

{% highlight python %}
   abcphone invoice 05.2015100.00sek73782174secret_string_for_issuer
{% endhighlight %}

The corresponding SHA-256 hash is:

{% highlight python %}
   22ef08bdc0fe9693ca4a65e3bfec3d927108fc47be9889b1001fd6f613f6e3b3
{% endhighlight %}


<b>Example #2</b>

QR code (urlencoded)

{% highlight python %}
   HTTP://SEQR.SE/000/invoice?i=abc&d=Phone%20invoice%2005.2015
   &a=100.00&c=SEK&r=73782174&o=true
   &h=99fd26ca2e1e28324e45465c0f9949c474d2544e0ccb8474d12930c72235fddb
{% endhighlight %}

(all in one line)

The input string for computing the hash (after point 8 in the instruction above) is:

{% highlight python %}
   abcphone invoice 05.2015100.00sek73782174truesecret_string_for_issuer
{% endhighlight %}

The corresponding SHA-256 hash is:

{% highlight python %}
   99fd26ca2e1e28324e45465c0f9949c474d2544e0ccb8474d12930c72235fddb
{% endhighlight %}


For testing purposes one can use on-line SHA-256 calculator available at: <a href="http://www.xorbin.com/tools/sha256-hash-calculator">http://www.xorbin.com/tools/sha256-hash-calculator</a> .

# Invoice reports

To fetch a report one needs to call a RESTful API using HTTP GET method. 

For integration/testing purpose please use below service URL:

	https://invoice-int.seqr.com/api/report/

The parameters of a call are as follows:

|---|---|---|
| Param name | Param type | Description |
|---|---|---|
| startDate | QUERY | give me reports newer than startDate (inclusive),
format: dd.MM.yyyy |
| endDate | QUERY | give me reports older than endDate (inclusive),
format: dd.MM.yyyy |
| issuer | QUERY | issuer name; the same value that is used in generated QR codes |
| X-Auth-Token | HTTP HEADER | SHA-256 hash constructed out of the following string: &lt;issuer name&gt; + &lt;secret string for issuer used for invoice QR code generation&gt;. |
|---|---|---|

All these parameters are mandatory.

<b>Example</b>

Let us assume that issuer name is 'abc' and secret string is SECRET_STRING_FOR_ISSUER.
Hence, the input string for hash calculation is

{% highlight python %}
   abcSECRET_STRING_FOR_ISSUER
{% endhighlight %}

which results in the following SHA-256 hash

{% highlight python %}
   1be46a9bb3efac8e7b691c06cb6d7bea43c5522a64a1cbfd5f511e67de6440c0
{% endhighlight %}


Hence, the call to fetch a report from 1st June to 30th June 2015 is 

{% highlight python %}
curl
-X GET
-H 'X-Auth-Token: 1be46a9bb3efac8e7b691c06cb6d7bea43c5522a64a1cbfd5f511e67de6440c0'
'https://invoice-int.seqr.com/api/report?startDate=01.06.2015
&endDate=30.06.2015&issuer=abc'
{% endhighlight %}

# Notifications

After successfull payment SEQR Invoice Service will call RESTful API exposed by issuer.
Please check <a href="/merchant/reference/invoiceserviceapi.html">SEQR Invoice Service API</a> for more details.

# Certification

For certification purpose we will send you couple sets of parametrs. You should generate SEQR Invoice Service QR codes based on these parameters and send generated QR codes back to us for validation. 
After validation we will try to use them for payment and will check if your notification service exposed to SEQR Invoice Service returns HTTP 200.
We will also ask you to get few reports using our API.


