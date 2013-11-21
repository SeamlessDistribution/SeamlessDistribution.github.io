---
layout: default
title: SEQR Reconciliation
description: SEQR Reconciliation
---

## Reconciliation

To check and confirm that cashregister/shop have the same number of transactions
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

The following are steps to perform reconciliation against SEQR from cashregisters

1. At the end of a working shift or shop hour, a cashier presses a button 'Close & Reconcile' on a cashregister.
The cashregisters application send markTransactionPeriod request to SEQR to mark end of transactions list
for this period. SEQR returns with a unique reference number, ersReference.
2. The cashregister application waits for a couple of seconds (around 3 seconds) in order to make sure that all
transactions are ready to process for reconciliation report.
3. The cashregister application calls executeReport using ersReference from step 1 to fetch reconciliation report
representing transaction summary since the previous reconciliation until the end of transaction list for this
period.
4. In case the reconciliation report is not ready , SEQR will return with result code 2
(REPORT_NOT_READY). The cashier should wait for couple seconds (around 3 seconds) more and repeat
step 3 again.

In executeReport, any of the following reports can be specified:


<table>
<tr><th>Report ID</th><th>Report Name</th><th>Description</th></tr>


<tr><td>STD_RECON_001</td>
    <td>Merchant Transactions</td>
    <td>Transaction summary for a shop representing number 
of transactions and summary amount done for the 
period 



<tr><td>STD_RECON_003</td>
    <td>Merchant Transactions Details</td><td>Transaction details for a shop
showing ersReference, cashier,
cash register and amount for the
period
</td></tr>

<tr><td>STD_RECON_006</td>
    <td>Terminal Transactions Summary</td><td>Contains the number 
of transactions and summary amount purchased/refunded for the 
period. </td></tr>
<tr><td>STD_RECON_007</td><td>Terminal Transactions Details</td>
    <td>Transaction details for a terminal showing reference 
id and amounts for each transaction in the period. 
</td></tr>



</table>

There are two ways of reconciliation against SEQR service:

* Per shop reconciliation: Only one master cashregister perform reconciliation process. The reconciliation
report will show transactions summary for every cashregisters in the shop.
* Per terminal reconciliation: Every cashregister in a shop perform reconciliation process. The reconciliation
report will show transactions summary only for the specific cashregister. In this case, terminalId
should be provided when calling markTransactionPeriod.

Please refer to the above table to check which reports can be used for per terminal
or per shop reconciliations.

