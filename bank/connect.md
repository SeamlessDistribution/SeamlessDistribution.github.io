---
layout: default
title: Bank Registration API
description: SEQR Bank/Credit connect API 
---

Register customers for SEQR accounts
====================================

Our authservice WS makes it easily to register users, seqr online, via atm or mobile

Authservice provides these methods:

    createAuthorization(context,type,purpose,mimetype,message)
    queryAuthorization(context,reference)
    cancelAuthorization(context,reference)
    submitAccountRegistration(context,reference,accounttype,accountid,parameters)
    confirm_identity(context,authreference, ...)

Download [example code here](/download/seqr-provisioner-sample.tgz).
