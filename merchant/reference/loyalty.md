---
layout: default
title: SEQR Merchant Loyalty
description: Reference
---


# Payment with loyalty program

The Cash Register Service allows SEQR users to add, connect and store loyalty program information in SEQR to be accessed anywhere at any time through the SEQR mobile wallet. 

SEQR informs the merchant that SEQR user has a loyalty (membership) program that is relevant for the merchant so it can be applied to the purchase. Normally, the merchant will only receive one loyalty program token for a specific payment.
When the merchant receives a token that is identified as a loyalty program token, it should apply the loyalty locally and then call updateInvoice to confirm to SEQR server of the updated amount and other information along with the token that was actually used.

## General loyalty scenario

1) Cash register sends a new bill (sendInvoice) to SEQR server. If SEQR user has swiped a loyalty card the customer token is added to the invoice as well.

2) SEQR user scans the QR code and SEQR app is being blocked until invoice is confirmed by cash register.

3) If user has loyalty card or card number was sent inside the invoice, SEQR server will send one card number in its response in this order:

* Card number from invoice (if present)

* Card number from SEQR database (if present)

 ________________________________________
  **Note!** SEQR app is only presenting loyalty cards. There is no communication between SEQR app and SEQR server being responsible for sending card number to cash register.

________________________________________



4) Cash register can update the invoice based on data received from SEQR server; that is, loyalty cards from SEQR database. Thus, cash register can also add loyalty card number (customer token) to invoice, if QR code was scanned meanwhile.

5) Cash register confirms optionally updated invoice which causes SEQR app being unblocked.

6) SEQR user confirms invoice by entering PIN.

7) After payment, if loyalty card has been sent from cash register, SEQR app asks user if SEQR should remember the card number (save new or update existing).Remembered card number is added to SEQR response in next payment process if shop is present in defined hierarchy for given loyalty card type.

## Sequence diagram

This sequence diagram illustrates a typical payment flow with loyalty card, where the cash register sends invoice, the user scans, confirms payment and then swipes the loyalty card (in this case, the card has not been used before):

#### This style?

<div class="diagram">

Cashregister->SEQR: sendInvoice
SEQR->Cashregister: invoice response
Note right of Cashregister: Cashregister loop
Cashregister->SEQR: getPaymentStatus
SEQR->Cashregister: ISSUED
Note right of Cashregister: User pays
Cashregister->SEQR: getPaymentStatus
SEQR->Cashregister: ISSUED
Note left of App: User scans QR code
App->SEQR: getInvoiceBrief
SEQR->App: response
Note left of App: User confirms\n with PIN
App->SEQR: payInvoice
SEQR->App: success
Note left of App: User swipes\n loyalty card
Note right of Cashregister: Cashregister loop
Cashregister->SEQR: updateInvoice (token=1)
SEQR->Cashregister: system error
Cashregister->SEQR: getPaymentStatus
SEQR->Cashregister: PAID
</div>

<script>
 $(".diagram").sequenceDiagram({theme: 'simple'});
</script>

#### Or this style??


<img src="/assets/images/loyalty.png" />


**Note:** The sequence can vary depending on how it is implemented by the card issuer or merchant. The sequence also varies depending on *when* the loyalty card is swiped during the payment process.

**Note:** Swiped loyalty cards always override loyalty account that already exists in SEQR.


## Graphical requirements

### Icon requirements

* Size: 110 x 110 px
* File format: png, jpg

Your **icon** is shown in multiple places in SEQR app:

* After payment if SEQR user swipes a loyalty card (app asks user to add the swiped loyalty card.)
* After payment if SEQR user swipes a new loyalty card (app asks user to replace the old loyalty with the new swiped loyalty card.)
* In the add loyalty list when user wants to add your loyalty (user can see all available loyalty accounts in a list and can read more about them by pressing the item.)
* In the account list when user has added your loyalty (when a loyalty account has been added, user can see the loyalty in their account list.)


### Logo requirements for "Add loyalty" page

* Size: fit your logo in 160 x 80 px
* File format: png, jpg
* Background: transparent

Your **logo** is shown in SEQR app:

* On the "add loyalty" page when user wants to add your loyalty (user can read about a loyalty by going to the add loyalty list. Here the user gets an explanation on how to add the loyalty account.)


### Logo requirements for "Information" page

* Size: fit your logo in 640 x 250 px
* File format: png, jpg
* Background: transparent

Your **logo** is shown in SEQR app:

* On the information page when user has added your loyalty (user can remove the loyalty account by going to the loyalty information page.)












