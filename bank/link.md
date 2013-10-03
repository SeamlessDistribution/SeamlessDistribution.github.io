---
layout: default
title: Bank Link API
description: SEQR Bank or credit payment and information API 
---

Just four methods to enable payments
====================================

Our standard back end link allows you deliver payments and transfeers.
The four methods we need from you are:

    authorize(ersRefernce,fromAccount,toAccount,fromMessage,toMessage,currency,amountm,batch)
    capture(reference,ersReference,batch)
    cancel(reference,ersReference,batch)
    getAccountInformation(account)

The methods are called from our SEQR-backend and we also have an example with source ready for download. 

Download the bank-link-simulator and modify it to your banking or credit system.

- [runnable+code](/download/ers-standard-bank-link-sample.tgz)

- [bank-link-API](/download/ers-standard-bank-link.pdf)


Start the sample server like: 

     mvn exec:java -Dexec.mainClass="com.seamless.ers.common.banklink.sample.Main"
