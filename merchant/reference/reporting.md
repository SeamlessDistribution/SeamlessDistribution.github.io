---
layout: default
title: SEQR Reporting and Reconciliation
description: SEQR Reporting Reconciliation
---

## Reporting and reconciliation

To check and confirm that cash register/shop has the same number of transactions
as SEQR service, merchants can integrate towards the reconciliation feature of
SEQR service.

Reconciliation is provided with the following calls:

* markTransactionPeriod - Marks the end of one and the beginning of a new 
transaction period; used in reporting. 
* executeReport - Generates a report for the transaction period. 


<div class="diagram">
Cashregister->SEQR: markTransactionPeriod
SEQR-->Cashregister: ersReference
Cashregister->SEQR: executeReport (ersReference)
SEQR-->Cashregister: REPORT_NOT_READY
Cashregister->SEQR: executeReport (ersReference)
SEQR-->Cashregister: XML report contents
</div>

<script>
 $(".diagram").sequenceDiagram({theme: 'hand'});
</script>

### Procedure to reconcile transactions and create report

The following are steps to perform reconciliation against SEQR from cash registers

1. At the end of a working shift or shop hour, a cashier presses a button 'Close & Reconcile' on a cash register.
The cash register sends **markTransactionPeriod** request to SEQR to mark end of transactions list
for this period. SEQR returns with a unique reference number, ersReference.
2. The cash register waits for a couple of seconds (around 3 seconds) in order to make sure that all
transactions are ready to process for reconciliation report.
3. The cash register calls **executeReport** using ersReference from step 1 to fetch reconciliation report
representing transaction summary since the previous reconciliation until the end of transaction list for this
period. The report to be specified, using executeReport, depends on whether it is per shop or per terminal reconciliation, see below.
4. In case the reconciliation report is not ready, SEQR will return with result code 2
(REPORT_NOT_READY). The cashier should wait for couple seconds (around 3 seconds) more and repeat
step 3 again.



### Reports per shop reconciliation


Only one master cash register perform reconciliation process. The reconciliation
report will show transactions summary for every cash register in the shop.


<table>
<tr><th>Report ID</th><th>Report Name</th><th>Description</th></tr>


<tr><td>STD_RECON_001</td>
    <td>Merchant Transactions</td>
    <td>Transaction summary for a shop representing number 
of transactions and summary amount done for the 
period. 
</td></tr>


<tr><td>STD_RECON_003</td>
    <td>Merchant Transactions Details</td><td>Transaction details for a shop
showing ersReference, cashier,
cash register and amount for the
period.
</td></tr>
</table>



### Reports per terminal reconciliation


Every cash register in a shop perform reconciliation process. The reconciliation
report will show transactions summary only for the specific cash register. In this case, terminalId
should be provided when calling markTransactionPeriod.


<table>
<tr><th>Report ID</th><th>Report Name</th><th>Description</th></tr>

<tr><td>STD_RECON_006</td>
    <td>Terminal Transactions Summary</td><td>Contains the number 
of transactions and summary amount purchased/refunded for the 
period. </td></tr>

<tr><td>STD_RECON_007</td><td>Terminal Transactions Details</td>
    <td>Transaction details for a terminal showing reference 
id and amounts for each transaction in the period. 
</td></tr>
</table>


### executeReport SOAP request example, report STD_RECON_001 (shop)


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
            <id>hml</id>
            <type>RESELLERUSER</type>
            <userId>9900</userId>
          </initiatorPrincipalId>
          <password>2009</password>
       </context>
       <reportId>Reconciliation/Shop.xml</reportId>
       <language>en</language>
       <parameters>
          <parameter>
             <entry>
                <key>transactionPeriodId</key>
                <value>2012071711291546101000028</value>
             </entry>
          </parameter>
       </parameters>
     </ext:executeReport>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


### executeReport SOAP response example, report STD_RECON_001 (shop)

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:executeReportResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <report>
               <title/>
               <mimeType>text/html</mimeType>
               <content>Cjw/...=</content>
               <contentString><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<ResellerTransactionSummary>
<Meta>
<ResellerId>hm1</ResellerId>
<TransactionPeriodId>2012071711291546101000028</TransactionPeriodId>
<GeneratedAt>2012-07-18 15:19</GeneratedAt>
</Meta>
<Row>
<SalesCount>202</SalesCount>
<SalesTotal>5476.52000</SalesTotal>
</Row>
<ResellerTransactionSummary>]]></contentString>
            </report> 
         </return>
      </ns2:executeReportResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


### executeReport SOAP request example, report STD_RECON_003 (shop)


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
            <id>hml</id>
            <type>RESELLERUSER</type>
            <userId>9900</userId>
          </initiatorPrincipalId>
          <password>2009</password>
       </context>
       <reportId>Reconciliation/STD_RECON_003.xml</reportId>
       <language>en</language>
       <parameters>
          <parameter>
             <entry>
                <key>transactionPeriodId</key>
                <value>2012071711291546101000028</value>
             </entry>
          </parameter>
       </parameters>
     </ext:executeReport>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


### executeReport SOAP response example, report STD_RECON_003 (shop)

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:executeReportResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <report>
               <title>STD_RECON_003_2012071711291546101000028.xml</title>
               <mimeType>text/html</mimeType>
               <content>PD94bWwgdmVyc2...=</content>
              <contentString><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<TransactionDetails>
<Meta>
<ResellerId>hm1</ResellerId>
<TransactionPeriodId>2012071711291546101000028</TransactionPeriodId>
<GeneratedAt>2012-07-18 15:21</GeneratedAt>
</Meta>

<Row>
<TerminalId>d8e0ff10ea214e5282899aa9697117c1</TerminalId>
<CashierId>bob</CashierId>
<SalesAmount>93.31000</SalesAmount>
<ErsReference>2012060410485453001000101</ErsReference>
</Row>

<Row>
<TerminalId>d8e0ff10ea214e5282899aa9697117c1</TerminalId>
<CashierId>bob</CashierId>
<SalesAmount>30.00000</SalesAmount>
<ErsReference>2012060410502892201000104</ErsReference>
</Row>

<Row>
<TerminalId>d8e0ff10ea214e5282899aa9697117c1</TerminalId>
<CashierId>bob</CashierId>
<SalesAmount>340.00000</SalesAmount>
<ErsReference>2012060411033709001000145</ErsReference>
</Row>

</TransactionDetails>]]></contentString>
            </report> 
         </return>
      </ns2:executeReportResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



### executeReport SOAP request example, report STD_RECON_006 (terminal)


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
            <id>hml</id>
            <type>RESELLERUSER</type>
            <userId>9900</userId>
          </initiatorPrincipalId>
          <password>2009</password>
       </context>
       <reportId>Reconciliation/STD_RECON_006.xml</reportId>
       <language>en</language>
       <parameters>
          <parameter>
             <entry>
                <key>transactionPeriodId</key>
                <value>2012102916093771801000146</value>
             </entry>
             <entry>
                <key>TERMINALID</key>
                <value>2469e0bf14214797880cafb0eda1b535</value>
             </entry>
          </parameter>
       </parameters>
     </ext:executeReport>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



### executeReport SOAP response example, report STD_RECON_006 (terminal)

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:executeReportResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <report>
               <title>STD_RECON_006_2012102916093771801000146.xml</title>
               <mimeType>text/html</mimeType>
               <content>PD94...==</content>
               <contentString><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<CashierTransactionSummary>
<Meta>
<ResellerId>hm1</ResellerId>
<TerminalId>2469e0bf14214797880cafb0eda1b535</TerminalId>
<TransactionPeriodId>2012102916093771801000146</TransactionPeriodId>
<GeneratedAt>2012-10-30 12:18</GeneratedAt>
</Meta>

<Row>
<SalesCount>1</SalesCount>
<SalesTotal>10.00000</SalesTotal>
</Row>

</TerminalTransactionSummary>]]></contentString>
            </report> 
         </return>
      </ns2:executeReportResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



### executeReport SOAP request example, report STD_RECON_007 (terminal)


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
            <id>hml</id>
            <type>RESELLERUSER</type>
            <userId>9900</userId>
          </initiatorPrincipalId>
          <password>2009</password>
       </context>
       <reportId>Reconciliation/STD_RECON_007.xml</reportId>
       <language>en</language>
       <parameters>
          <parameter>
             <entry>
                <key>transactionPeriodId</key>
                <value>2012102916093771801000146</value>
             </entry>
             <entry>
                <key>TERMINALID</key>
                <value>2469e0bf14214797880cafb0eda1b535</value>
             </entry>
          </parameter>
       </parameters>
     </ext:executeReport>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}


### executeReport SOAP response example, report STD_RECON_007 (terminal)

{% highlight python %}
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:executeReportResponse xmlns:ns2="http://external.interfaces.ers.seamless.com/">
         <return>
            <resultCode>0</resultCode>
            <resultDescription>SUCCESS</resultDescription>
            <report>
               <title>STD_RECON_007_2012102916091394901000143.xml</title>
               <mimeType>text/html</mimeType>
               <content>PD94...==</content>
               <contentString><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<CashierTransactionSummary>
<Meta>
<ResellerId>hm1</ResellerId>
<TerminalId>2469e0bf14214797880cafb0eda1b535</TerminalId>
<TransactionPeriodId>2012102916093771801000146</TransactionPeriodId>
<GeneratedAt>2012-10-30 12:20</GeneratedAt>
</Meta>

<Row>
<SalesCount>1</SalesCount>
<SalesTotal>10.00000</SalesTotal>
</Row>

</TerminalTransactionSummary>]]></contentString>
            </report> 
         </return>
      </ns2:executeReportResponse>
   </soapenv:Body>
</soapenv:Envelope>

{% endhighlight %}



