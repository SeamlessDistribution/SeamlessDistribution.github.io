---
layout: default
title: SEQR Webshop Payments
description: SEQR Merchant, webshop, POS integration
---


## SEQR in a WebShop

### Introduction

SEQR must be implemented as a new payment method in the “Check out” process where the 
customer selects between different methods of payment. This is an example of a 
checkout that supports SEQR:

<img src="/assets/images/seqr_webshop.png" />

The flow for a webshop SEQR payment is very similar to the [basic SEQR
payment](/merchant/payment).
The difference is in details of how the SEQR QR code is presented to the SEQR
user. To integrate SEQR, follow these steps:
1. Integrate the payment view 
2. Present the QR code 
3. Present receipt

### Integrate the Payment View
There are two payment views that you can choose from:

* Standard Payment View
* Slim Payment View

Each module contains three different sizes to be used depending on type (size) of device 
that is used for payment (smartphone, tablet, etc.) Two of the sizes contain a QR code to 
scan, whilst the third contains a link that forwards the payer to SEQR app. The latter is
used in case of browsing the webshop using a smartphone.
The difference between the modules is that one contains an introduction film about 
SEQR. Both modules contain download links to SEQR.

### Present the QR Code



### Present Receipt
