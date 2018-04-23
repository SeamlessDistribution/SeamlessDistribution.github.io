---
layout: default
title: Link your app to Glase payment
description: Glase Merchant, link your app to SEQR payment
---


# Support your customers - Link your app to SEQR payment

A mobile integration with Glase would contain the following items:

* A page with brief information about Glase (optional)
* A button to pay with Glase
* When button is pressed, Glase app should be launched if customer already installed it, otherwise customer should be redirected to download page


## URLs and labels to use

Link to Glase app:

|--- |  --- | --- |
|  OS | Link to Glase app | Button label |
|--- | --- |
| iOS | seqr:// | Betala med Glase/Pay with Glase |
| Android | open:com.seamless.seqr | Betala med Glase/Pay with Glase |
| --- | --- | --- |


Link to download store:

|--- |  --- | --- |
|  OS | Link to download store | Button label |
|--- | --- |
| iOS | https://itunes.apple.com/se/app/seqr/id494224742 | Skaffa SEQR-appen/Get SEQR app|
| Android | market://details?id=com.seamless.seqr | Skaffa SEQR-appen/Get SEQR app |
| --- | --- | --- |



## Customer stories

### Customer with Glase app installed already

This scenario illustrates payment when the customer already has Glase app installed:

1.	Customer opens your app.
2.	Customer gets information that Glase can be used to pay at your checkouts.
3.	Customer presses the **Betala med Glase/Pay with Glase** link in your app.
4.	Glase app is launched and customer pays with Glase.
5.	Customer gets the receipt in the mobile device and a standard receipt.



### Customer does not have Glase app installed yet

This scenario illustrates payment when the customer does not have Glase app installed yet:

1.	Customer opens your app.
2.	Customer gets information that Glase can be used to pay at your checkouts.
3.	Customer presses the **Skaffa Glase-appen/Get Glase app** link in your app.
4.	Customer is sent to the download store.
5.	Customer downloads and launches Glase app. 
6.	Customer connects a payment account and pays with Glase.
7.	Customer gets the receipt in the mobile device and a standard receipt.

