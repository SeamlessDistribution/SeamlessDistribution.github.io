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
   HTTP://SEQR.SE/000/invoice?j=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImlzcyI6ImV4YW1wbGUifQ.eyJhIjoiMjkuOTkiLCJjIjoiU0VLIiwiZCI6IlRlc3QgaW52b2ljZSIsInIiOiJSODIwOTE5IiwibyI6ImZhbHNlIn0.PwBs2SXHLMC3sofiSWayX180XM7i3wANOdZTjmXHmLg
{% endhighlight %}

QRCode contains URL containing single query parameter labaled as "j".

The rules governing the creation of a QR code are summarized in a table below.

<table>
   <tbody>
   <col width="35%"/>
   <col width="10%"/>
   <col width="55%"/>
      <tr>
         <th>QR code element</th>
         <th>Mandatory</th>
         <th>Description</th>
      </tr>
      <tr>
         <td>
            HTTP://SEQR.SE/000/invoice?
         </td>
         <td>
				Y
         </td>
         <td>
				This part is compulsory and a QR code must start with it.
         </td>
      </tr>
      <tr>
         <td>
            j={JWT}
         </td>
         <td>
				Y
         </td>
         <td>
				JSON Web Token data.
         </td>
      </tr>
   </tbody>
</table>

This parameter is so called JSON Web Token (JWT). More on that standard can be obtained from website: <a href="http://jwt.io/">http://jwt.io/</a>. Value of this parameter must conform to JWT standard. Usage of one of many implementations proposed on <a href="http://jwt.io/">jwt.io</a> website is suggested.

JWT contains 2 parts that must be taken care of: header and payload. Both should be prepared as JSON data with following fields.

#### JWT Header

<table>
   <tbody>
   <col width="35%"/>
   <col width="10%"/>
   <col width="55%"/>
      <tr>
         <th>JSON field</th>
         <th>Mandatory</th>
         <th>Description</th>
      </tr>
      <tr>
         <td>
            alg: "HS256"
         </td>
         <td>
				Y
         </td>
         <td>
				Algorithm used for JWT signature. It should always stay HS256. This value is filled automatically by most JWT implementation libraries.
         </td>
      </tr>
      <tr>
         <td>
            typ: "JWT"
         </td>
         <td>
				Y
         </td>
         <td>
				Type of an object. In our case it's always JWT. This value is filled automatically by most JWT implementation libraries.
         </td>
      </tr>
      <tr>
         <td>
            iss: &lt;issuer_id&gt;
         </td>
         <td>
				Y
         </td>
         <td>
				Issuer name provided by SEQR.
         </td>
      </tr>
   </tbody>
</table>

#### JWT Payload

<table>
   <tbody>
   <col width="35%"/>
   <col width="10%"/>
   <col width="55%"/>
      <tr>
         <th>JSON field</th>
         <th>Mandatory</th>
         <th>Description</th>
      </tr>
      <tr>
         <td>
            d: &lt;description&gt;
         </td>
         <td>
				Y
         </td>
         <td>
				Max 50-characters long description of the invoice. Allowed characters: alphanumeric, white spaces, braces, dash, slash, comma, dot, single and double quotes.
				<br>
				<span class="seqrhl">([A-Za-z\w.,\(\)-\\\\/\"\'])+</span>.
         </td>
      </tr>
      <tr>
         <td>
            a: &lt;amount&gt;
         </td>
         <td>
				Y
         </td>
         <td>
				Amount to be paid, numerical value with a precision up to 2 decimal points, eg. 100.00 (with a dot '.' being the decimal seperator).
         </td>
      </tr>
      <tr>
         <td>
            c: &lt;currency&gt;
         </td>
         <td>
				Y
         </td>
         <td>
				3-characters long currency.
         </td>
      </tr>
      <tr>
         <td>
            r: &lt;issuers_reference&gt;
         </td>
         <td>
				Y
         </td>
         <td>
				Max 30-characters long unique reference of the invoice. It is set up by an issuer. Allowed characters: alphanumeric, white spaces, braces, dash, slash, comma, dot, single and double quotes.
				<br>
				<span class="seqrhl">([A-Za-z\w.,\(\)-\\\\/\"\'])+</span>.
         </td>
      </tr>
      <tr>
         <td>
            o: &lt;true|false&gt;
         </td>
         <td>
				Y
         </td>
         <td>
				If set to true the invoice can be paid only once; default value: false - it means that invoice identified by the same reference can be paid several times.
         </td>
      </tr>
   </tbody>
</table>

### Example

Let's assume our issuer name and secret are:

|---|---|---|
| Param name | Param value |
|---|---|---|
| Issuer Name | example |
| Secret | 5ecr3t |
|---|---|---|

We want to issue invoice with following data:

|---|---|---|
| Param name | Param value |
|---|---|---|
| amount | 29.99 |
| currency | SEK |
| description | Test invoice |
| reference | R820919 |
| once | false |
|---|---|---|

Our payload should be represented by JSON like:

{% highlight python %}
{
    "a": "29.99",
    "c": "SEK",
    "d": "Test invoice",
    "r": "R820919",
    "o": "false"
}
{% endhighlight %}

Secret code must be encoded using SHA-256 before use. In our example it's value for '5ecr3t' should be:

|---|---|---|
| Encoding type | Encoded value |
|---|---|---|
| base64 hash | v7omClW4RuJEC8SUBCaL6E5q7R5wFPbHC7uN/J56U48= |
| hex hash | bfba260a55b846e2440bc49404268be84e6aed1e7014f6c70bbb8dfc9e7a538f |
|---|---|---|

We present both representations, raw value encoded by base64 and hexadecimal value. On <a href="http://jwt.io/">jwt.io</a> website you can verify your JWT using first option (base64 hash) after checking "secret base64 encoded".

For testing purposes one can use on-line SHA-256 calculator available at: <a href="http://approsto.com/sha-generator/">http://approsto.com/sha-generator</a>.

Generated JWT should be:

{% highlight python %}
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImlzcyI6ImV4YW1wbGUifQ.eyJhIjoiMjkuOTkiLCJjIjoiU0VLIiwiZCI6IlRlc3QgaW52b2ljZSIsInIiOiJSODIwOTE5IiwibyI6ImZhbHNlIn0.PwBs2SXHLMC3sofiSWayX180XM7i3wANOdZTjmXHmLg
{% endhighlight %}

And finally URL in QRCode:

{% highlight python %}
HTTP://SEQR.SE/000/invoice?j=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImlzcyI6ImV4YW1wbGUifQ.eyJhIjoiMjkuOTkiLCJjIjoiU0VLIiwiZCI6IlRlc3QgaW52b2ljZSIsInIiOiJSODIwOTE5IiwibyI6ImZhbHNlIn0.PwBs2SXHLMC3sofiSWayX180XM7i3wANOdZTjmXHmLg
{% endhighlight %}

Use this QR code generator to verify your implementation:
<br><a href="http://cdn.seqr.com/seqr-services-dev/invite-service-qr-generator/single_qr.html">http://cdn.seqr.com/seqr-services-dev/invite-service-qr-generator/single_qr.html</a>.

Below we present implementations in some popular programming languages using one of libraries suggested on <a href="http://jwt.io/">jwt.io</a> website.

#### JavaScript with jsrsasign

{% highlight python %}
/***
 * Requires jsrassign
 * Required js files:
 *   - js/jsrsasign-5.0.2-all-min.js
 *   - js/ext/json-sans-eval-min.js
 *   - js/jws-3.3.js
 */
KJUR.jws.JWS.sign(
  null,
  {"alg":"HS256","typ":"JWT","iss":"example"},
  {"a":"29.99","c":"SEK","d":"Test invoice","r":"R820919","o":"false"},
  CryptoJS.SHA256('5ecr3t').toString()
);
{% endhighlight %}

#### PHP using Firebase

{% highlight python %}
/***
 * Requires php-jwt
 * Composer installation: composer require firebase/php-jwt
 */
require __DIR__ . '/vendor/autoload.php';
use \Firebase\JWT\JWT;
 
$key = hash('sha256', "5ecr3t", true);
$head = array(
    "alg" => "HS256",
    "typ" => "JWT",
    "iss" => "example"
);
$token = array(
    "a" => "29.99",
    "c" => "SEK",
    "d" => "Test invoice",
    "r" => "R820919",
    "o" => "false"
);
 
$jwt = JWT::encode($token, $key, 'HS256', null, $head);
print_r($jwt . PHP_EOL);
{% endhighlight %}

#### Python using jwcrypto

{% highlight python %}
"""
Requires jwcrypto
PIP installation: pip install jwcrypto cryptography
"""
 
from jwcrypto import jwt, jwk
from jwcrypto.common import base64url_encode
import hashlib
 
Token = jwt.JWT(
    header='{"alg":"HS256","typ":"JWT","iss":"example"}',
    claims='{"a":"29.99","c":"SEK","d":"Test invoice","r":"R820919","o":"false"}'
)
 
key = jwk.JWK(
    kty='oct',
    k=base64url_encode(hashlib.sha256("5ecr3t").digest())
)
Token.make_signed_token(key)
print Token.serialize()
{% endhighlight %}

#### Ruby using jwt

{% highlight python %}
##
# Requires jwt
# Gem installation: gem install jwt
 
require 'jwt'
require 'digest'
 
# This prevents jwt from changing headers
JWT.instance_eval do
  def encoded_header(algorithm = 'HS256', header_fields = {})
    base64url_encode(encode_json(header_fields))
  end
end
 
header = {:alg => 'HS256', :typ => 'JWT', :iss => 'example'}
payload = {:a => '29.99', :c => 'SEK', :d => 'Test invoice', :r => 'R820919', :o => "false"}
 
secret = Digest::SHA256.digest '5ecr3t'
token = JWT.encode payload, secret, 'HS256', header
puts token
{% endhighlight %}

# Invoice reports

To fetch a report one needs to call a RESTful API using HTTP GET method. 

For integration/testing purpose please use below service URL:

	https://invoice-int.seqr.com/api/report/

The parameters of a call are as follows:

|---|---|---|
| Param name | Param type | Description |
|---|---|---|
| startDate | QUERY | give me reports newer than startDate (inclusive), format: ddMMyyyy |
| endDate | QUERY | give me reports older than endDate (inclusive), format: ddMMyyyy |
| issuer | QUERY | issuer name; the same value that is used in generated QR codes |
| X-Auth-Token | HTTP HEADER | SHA-256 hash constructed out of the following string: &lt;issuer name&gt; + &lt;secret string for issuer used for invoice QR code generation&gt;. |
|---|---|---|

All these parameters are mandatory.

### Example

Let us assume that issuer name is <span class="seqrhl">abc</span> and secret string is <span class="seqrhl">SECRET_STRING_FOR_ISSUER</span>.
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
'https://invoice-int.seqr.com/api/report?startDate=01062015&endDate=30062015&issuer=abc'
{% endhighlight %}

### Report content

Report consists of the following fields in the specified order: 

<ul>
	<li>ID - unique identifier of an invoice in SEQR</li>
	<li>DESCRIPTION - description of an invoice provided by an issuer.
		Double quotes and new lines are escaped.</li>
	<li>AMOUNT - amount paid, format 123.45 ('.' as a decimal
		separator)</li>
	<li>CURRENCY - 3-characters logs currency of an amount, eg. EUR</li>
	<li>STATUS - status of invoice; at the moment only PAID invoices
		are returned</li>
	<li>REFERENCE - identifier of an invoice provided by an issuer</li>
	<li>ERS_REFERENCE - identifier of a transaction in SEQR which paid
		the invoice</li>
	<li>PURCHASE_TIME - datetime when invoice was paid, format:&nbsp;<span
		style="line-height: 1.4285715;">YYYY-MM-DDThh:mm:ssTZD</span>,
		eg.&nbsp;<span style="line-height: 1.4285715;">1997-07-16T19:20:30+01:00</span>&nbsp;(described
		in <a rel="nofollow" class="external-link"
		href="http://www.w3.org/TR/NOTE-datetime">WC3 Date and Time
			Formats</a>)
	</li>
	<li>PAYER_MSISDN - MSISDN of payer if issuer requested it</li>
	<li>PAYER_FIRST_NAME - first name of payer if issuer requested
		delivery address of payer</li>
	<li>PAYER_LAST_NAME - last name of payer if issuer requested
		delivery address of payer</li>
	<li>PAYER_STREET - street of payer if issuer requested delivery
		address of payer</li>
	<li>PAYER_CITY - city of payer if issuer requested delivery
		address of payer</li>
	<li>PAYER_ZIP - ZIP code fo payer if issuer requested delivery
		address of payer</li>
	<li>PAYER_COUNTRY - country code of payer if issuer requested
		delivery address of payer</li>
</ul>

# Notifications

After successfull payment SEQR Invoice Service will call RESTful API exposed by issuer.
Please check <a href="/merchant/reference/invoiceserviceapi.html">SEQR Invoice Service API</a> for more details.

# Verification

The easiest way to verify your QRCodes is downloading and setting SEQR app up.
Please follow instructions from [SEQR test app](/app) then just scan your QRCode to find out whether it is valid or not.

# Certification

For certification purpose we will send you couple sets of parametrs. You should generate SEQR Invoice Service QR codes based on these parameters and send generated QR codes back to us for validation. 
After validation we will try to use them for payment and will check if your notification service exposed to SEQR Invoice Service returns HTTP 200.
We will also ask you to get few reports using our API.


