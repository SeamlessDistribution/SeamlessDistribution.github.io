---
layout: default
title: Glase Merchant API flows
description: API reference
---

# General payment

### Example 1: Cashregister sends invoice and user scans QR code and confirms payment   


<img src="/assets/images/normal_payment_flow_140108.png" />





# Payment flows with loyalty program

Cash Register Service allows users to add, connect and store loyalty program information in SEQR to be accessed anywhere at any time through SEQR mobile wallet.
The following sequence diagrams illustrate typical loyalty flows. 

**Note:** Each flow may have some variation depending on how it is implemented by the card issuer or merchant.

**Note:** Swiped loyalty cards always override loyalty account already existing in SEQR.



### Example 2: Cashregister sends invoice, user scans, confirms payment and then swipes loyalty card (card not used before)

<img src="/assets/images/loyalty_send_scan_pay_swipe_140108.png" />



### Example 3: Cashregister sends invoice, user scans, swipes loyalty card (card not used before) and then confirms payment 

<img src="/assets/images/loyalty_send_scan_swipe_pay_140108.png" />


### Example 4: Cashregister sends invoice, user swipes card (card not used before), scans and then confirms payment   

<img src="/assets/images/loyalty_send_swipe_scan_140109.png" />




### Example 5: Loyalty account exists in SEQR already: Cashregister sends invoice, user scans and confirms payment

<img src="/assets/images/loyalty_acc_inSEQR_140108.png" />



### Example 6: Replace loyalty card: Cashregister sends invoice, loyalty account exists in SEQR but another card is swiped, user scans and confirms payment

<img src="/assets/images/replace_loyalty_inSEQR_140109.png" />


### Example 7: Same loyalty card swiped: Cashregister sends invoice, loyalty account exists in SEQR but same card is swiped, user scans and confirms payment

<img src="/assets/images/same_loyalty_inSEQR_140109.png" />













