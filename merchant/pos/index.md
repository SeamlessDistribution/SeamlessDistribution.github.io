---
layout: default
title: POS Payments
description: SEQR Merchant, webshop, POS integration
---

<img src="/assets/images/cash_register_bw.png" align="right" width="200px"/>

## Configure POS/Cash register for SEQR

Follow these steps to configure your POS for integration with SEQR:

1. Register POS (terminal) with SEQR 
2. Assign SEQR id
3. Add SEQR as payment in your POS
6. Go live!

### 1. Register POS with SEQR


Features of registerTerminal function:


* Each POS/cash register in the checkout line is called a "terminal" in SEQR.
* Register and unregister POS against SEQR are separate functions in POS. 
* SEQR payments do not work in POS without a proper registration.
* Reseller user id and password stored in back office are used when a new SEQR terminal is registered.


________________________________________
**Note!** Each terminal is added only once. For example, if the checkout line contains five cash registers you also need five terminals registered in SEQR. Any new or reinstalled POS must be registered against SEQR.

________________________________________




**_POS menu_**

The SEQR terminal menu in the POS can be accessed with administrative rights. The menu on the POS may look like this:

Picture?
 
Both parameters terminalId and password are stored in the local database after successful registration. 

**How to add a terminal**

Preferably done in the back office.

1.	Create a context for administrative tasks using RESELLERUSER as the principal type. You have received your account information in a separate document from Seamless. 

2.	Call registerTerminal to add new terminals into the SEQR system. Save the password you generated together with the terminal id received from SEQR system for further usage.


________________________________________
**Note!** The terminal id that is received as response, must hereafter be used in every method that is called, for the particular terminal/POS.

________________________________________

Example of registerTerminal:

{% highlight python %}
{% include registerterminal.py %}
{% endhighlight %}





### 2. Assign SEQR id
(Method: **assignSeqrId**)

When getting a payment through the cash register, we cannot show the payment QR code
which is generated for the invoice to the SEQR user. To overcome that problem,
we assign a fixed QR code to each cash register. A POS SEQR sticker looks like this:

<img src="/assets/images/seqr-qrcodes.png" width="200px"/>

Each QR code sticker has a unique number assigned known as SEQR ID. The cash register/POS needs this number to establish a link with the QR code.


The cashier starts the sequence to assign the SEQR ID from the Configuration menu in POS and SEQR ID registration submenu. It is possible to enter the number manually or by scanning the QR code with a scanner. The scanner must be configured to accept Code 128 in order to read the barcode on the QR sticker.

Picture?

The parameter seqrId is stored in the local database after a successful assignment.

1.	Create a context for terminal usage by setting the principal type to TERMINALID. Supply the context with password and the terminal id as you saved for further usage when the terminal was created.

2.	Call assignSeqrId to assign the SEQR ID currently in use by the cash register.

### 3. Add SEQR as payment in your POS
This section describes how to set up the POS for SEQR payment from a cashier's perspective. Refer also to First SEQR payment, which shows how to implement the code with sample flow.

SEQR must be added as a new payment method. SEQR payment is enabled when an active receipt has started and the amount to pay is greater than zero. 

##### 1.	Start the payment by pressing the SEQR payment button in POS 

The following dialog is displayed to the cashier:
 
Picture?

The amount to pay is pre-entered in the dialog. The cashier can choose to increase or decrease the pre-entered amount.
If amount to pay is less than the receipt total, the following will occur after a completed payment:
* The receipt cannot be parked
* The receipt cannot be canceled
* The payment cannot be corrected
* Another payment must be used to complete the receipt

If amount to pay is higher than the receipt total, the following occurs after a completed payment:
* The difference between paid amount and the receipt total is returned to the customer.

##### 2.	Press the Pay button

It is possible to cancel an ongoing SEQR payment by pressing the Cancel button (method used: cancelInvoice). This option is only available before the payment is committed on the SEQR server. The dialog below is displayed to the cashier until the paying customer has completed the payment on the phone:

Picture?

POS calls the SEQR server each second while waiting for the payment to complete (see Get payment status below). The status code returned is “please wait more”, “payment completed” “canceled” or “an error occurred”.
When the SEQR payment is complete a transaction post is written to the receipt file. 
The transaction post contains the following data:

* Amount
* Reference number (ersReference)
* Description “SEQR payment”
* Timestamp

##### 3.	Configure the printer to include the following data as a confirmation of the purchase:


* Amount
* Reference number (ersReference)
* Description “SEQR payment”

________________________________________
**Note!**
* It is not possible to perform a SEQR payment against SEQR server when POS is offline. 
* All payments made by SEQR must be recorded, preferably in a separate account in the back office. A report can be generated, preferably in the back office – for more information, refer to Reporting.

________________________________________





##### 4. Send invoice to SEQR

(Method: **sendInvoice**)
The cashier starts a new payment sequence:
1.	Create a context for terminal usage by setting the principal type to TERMINALID. Supply the context with password and the terminal id as you saved for further usage when the terminal was created.

2.	Create a new  invoice, including:
* Cashier id/name
* Total amount for the entire invoice
* Issue date, when the invoice was created
* Invoice title
* ClientInvoiceId (a link between SEQR and your own system)
* Invoice rows (articles, discounts, other payments) 


________________________________________
**Note!** The sum of all invoice rows must be equal to the total amount of the invoice. You are allowed to create negative rows just to balance the invoice.

________________________________________


##### 5. Get payment status 

(Method: **getPaymentStatus**)

This function obtains status of a previously submitted invoice.
Do the following:

1.	Create a context for terminal usage by setting the principal type to TERMINALID. Supply the context with password and the terminal id as you saved for further usage when the terminal was created.

2.	Once each second; call getPaymentStatus for 30 seconds until the method returns that payment has completed. If getPaymentStatus is not queried, payment done by SEQR user will be refunded. 

3.	Add questions for the cashier to select either “try again” or “cancel the payment” if the payment has still not gone through after 30 seconds of polling. When selecting “try again” a new poll of 30 seconds is started, with the same reference number. **Note!** The POS must check the status each second, to verify that payment is completed. Otherwise the SEQR server does not receive any notification that transaction is finalized and the purchase will then be reversed!

4.	Once the payment is complete a reference number (ersReference) is obtained from SEQR. Save the reference number for follow-ups and print the number on end user receipts.


##### Optional - How to remove a terminal

1.	Create a context for terminal usage by setting the principal type to TERMINALID. Supply the context with password and the terminal id as you saved for further usage when the terminal was created.

2.	Call unregisterTerminal and the terminal is deleted from the SEQR system.

### 4. Go live!

To go live with your integration, [contact](/contact) Seamless to get [certified](/merchant/reference/certification.html) and receive the credentials to your POS/cash register.
