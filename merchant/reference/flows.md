---
layout: default
title: SEQR Merchant API flows
description: API reference
---

# General payment  

<div class="diagram">
Cashregister->SEQR: sendInvoice
App->Cashregister: Scan QR code
App->SEQR: getInvoiceBrief
SEQR-App: Invoice details
App->SEQR: payInvoice
SEQR-->Cashregister: (invoice reference)
Cashregister->SEQR: getPaymentStatus
SEQR-->Cashregister: ISSUED
SEQR->App: retry until SUCCESS
App->SEQR: Confirm payment
Cashregister->SEQR: getPaymentStatus
SEQR-->Cashregister: PAID
Note right of Cashregister: Payment cleared!
SEQR->App: Done (show receipt)
</div>





# Payment flows with loyalty program
Cash Register Service allows users to add, connect and store loyalty program information in SEQR to be accessed anywhere at any time through SEQR mobile wallet.
The following flows illustrate typical loyalty user flows. 
**Note:** Each flow can have some variation depending on how it is implemented by the card issuer or merchant.



## Payment with loyalty - card swiped after scanning, card not used before 

<div class="diagram">
Cashregister->SEQR: sendInvoice
App->Cashregister: Scan QR code
SEQR-->Cashregister: (invoice reference) 
Cashregister->SEQR: getPaymentStatus
SEQR-->Cashregister: ISSUED
App->Cashregister: Swipe loyalty card
Cashregister->SEQR: loyalty?
SEQR->App: inv. response+loyalty token
App->SEQR: Confirm payment
SEQR->App: SUCCESS+receipt+loyalty token
Cashregister->SEQR: updateInvoice
SEQR->Cashregister: result
Cashregister->SEQR: getPaymentStatus
SEQR-->Cashregister: PAID
SEQR->App: Add loyalty card?
App->SEQR: yes/no
SEQR->App: added/not added card
</div>




## Payment with loyalty - card swiped before scanning, card not used before 

<div class="diagram">
Cashregister->SEQR: sendInvoice
SEQR-->Cashregister: (invoice reference)
App->Cashregister: Swipe card
Cashregister->SEQR: loyalty?
Cashregister->SEQR: getPaymentStatus
SEQR-->Cashregister: ISSUED
SEQR->App: inv. response+loyalty token
App->SEQR: Confirm payment
SEQR->App: SUCCESS+receipt+loyalty token
Cashregister->SEQR: updateInvoice
SEQR->Cashregister: result
Cashregister->SEQR: getPaymentStatus
SEQR-->Cashregister: PAID
SEQR->App: Add loyalty card?
App->SEQR: yes/no
SEQR->App: added/not added card
</div>


## Payment with loyalty account in phone 

<div class="diagram">
Cashregister->SEQR: sendInvoice
SEQR-->Cashregister: (invoice reference)
Cashregister->SEQR: getPaymentStatus
SEQR-->Cashregister: ISSUED
App->SEQR: getInvoiceBrief (scan QR code)
SEQR-App: getInvoice before
Cashregister->SEQR: getPaymentStatus
SEQR-Cashregister: Token and inv.version = 1
Cashregister->SEQR: updateInvoice (version = 1)
SEQR->Cashregister: Status update ack
Cashregister->SEQR: getPaymentStatus
SEQR->Cashregister: Status update ack
Cashregister->SEQR: getPaymentStatus
SEQR->Cashregister: ISSUED
App->SEQR: getInvoiceBrief
SEQR->App: updated and issued invoice
App->SEQR: payInvoice
SEQR->App: SUCCESS
Cashregister->SEQR: getPaymentStatus
SEQR-->Cashregister: PAID
</div>


<script>
 $(".diagram").sequenceDiagram({theme: 'hand'});
</script>











