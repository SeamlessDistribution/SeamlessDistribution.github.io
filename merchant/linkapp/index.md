---
layout: default
title: Link app to SEQR
description: SEQR Merchant, link your app to SEQR payment
---


# Link your app to SEQR payment  

The purpose of in-app linking to SEQR is for your customer to be able to pay with SEQR from your app. The link should be used to increase usage of your app and thereby increase consumer loyalty to your brand.


## Information about SEQR in your app

A sample integration with SEQR would contain the following items:

* A page with brief information about SEQR (optional)
* A button to pay with SEQR
* When button is pressed, SEQR app should be launched if customer already installed it, otherwise customer should be redirected to download page


## URLs and labels to use

Link to SEQR app:

|--- |  --- | --- |
|  OS | Link to SEQR app | Button label |
|--- | --- |
| iOS | seqr:// | Betala med SEQR/Pay with SEQR |
| Android | open:com.seamless.seqr | Betala med SEQR/Pay with SEQR |
| --- | --- | --- |


Link to download store:

|--- |  --- | --- |
|  OS | Link to download store | Button label |
|--- | --- |
| iOS | https://itunes.apple.com/se/app/seqr/id494224742 | Skaffa SEQR-appen/Get SEQR app|
| Android | market://details?id=com.seamless.seqr | Skaffa SEQR-appen/Get SEQR app |
| --- | --- | --- |



## Customer stories

### Customer with SEQR app installed already

This scenario illustrates payment when the customer already has SEQR app installed:

1.	Customer opens your app.
2.	Customer gets information that SEQR can be used to pay at your checkouts.
3.	Customer presses the **Betala med SEQR** link in your app.
4.	SEQR app is launched and customer pays with SEQR.
5.	Customer gets the receipt in the mobile device and a standard receipt.



### Customer does not have SEQR app installed yet

This scenario illustrates payment when the customer does not have SEQR app installed yet:

1.	Customer opens your app.
2.	Customer gets information that SEQR can be used to pay at your checkouts.
3.	Customer presses the Betala med SEQR link in your app.
4.	Customer is sent to the download store.
5.	Customer downloads and launches SEQR app. 
6.	Customer connects a payment account and pays with SEQR.
7.	Customer gets the receipt in the mobile device and a standard receipt.

