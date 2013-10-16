---
layout: default
title: Merchant API
description: SEQR Merchant, webshop, POS integration
---

<img src="/assets/images/cash_register_bw.png" align="right" width="200px"/>

## Get SEQR payments

1. Point your smart phone to developer.seqr.com/app and install the developer app.
2. Install the demo-shop-example: 
        [demo-shop.zip](/download/demo-shop.zip), [wsdl](http://extdev4.seqr.se:8913/extclientproxy/service?wsdl)
3. Get a merchant id and password via
        [integrations@seamless.se](mailto:integrations@seamless.se) 
4. Go on a shopping spree and change the looks and products.

Feel hungry for real payments now?

More examples: 

* Magento (php) [code & plugin example](/download/magento/seqr_magento_module.zip)


## Code snippets

Create a a bill and publish it to the app (java): 
 
    Invoice invoice = new Invoice();
    invoice.setClientInvoiceId("20140102-002131");
    invoice.setTotalAmount(new Amount(2.00f,"USD"));
    invoice.setTitle("Ice cream shop");
    invoice.setFooter("Have a nice day");
    invoice.setBackURL("http://myicecreamshop.com/delivery");
    ret = merchantws.sendInvoice(getContext(),invoice); 
 
Querying for payment status (java-pseudo-code): 

    ret = merchantws.queryInvoice(invoiceReference);
    if ("PAYMENT_COMPLETE".equals(ret.getResponseCode())) {
        merchantws.sendReceipt("text/html",receipt);
        activity("payment-done-screen");
    } else if ("PAYMENT_CANCELLED") {
        // ...  
    } else if ("PAYMENT_PENDING") {
        activity("payment-pending-screen");
    } else ...

Creating a point of sale access-context (java):

    private ClientContext getContext()
    {
        ClientContext context = new ClientContext();
        PrincipalId principalId = new PrincipalId();
        principalId.setType("TERMINALID");
        principalId.setId(myTerminalId);
        context.setInitiatorPrincipalId(principalId);
        context.setPassword(myPassword);
        return context;
    }

Creating a new terminal-id using your reseller-id (python):  

    from suds.client import Client
    client = Client('http://extdev4.seqr.se:8913/extclientproxy/service?wsdl')
    context = client.factory.create("ns0:clientContext")
    context.channel="ws"
    context.clientId="client"
    context.clientRequestTimeout=0
    context.initiatorPrincipalId.id='myUserId'
    context.initiatorPrincipalId.type='RESELLERUSER
    context.initiatorPrincipalId.userId='9900'
    context.password='myPassword'
    response = client.service.registerTerminal(context, 'externalTerminalId', 'password-1234', 'my cashregsiter')
    print response # contains terminalId 

And assign the terminal-id to a QR-sticker (python continued): 

    ...
    context.initiatorPrincipalId.id=response.terminalId
    context.initiatorPrincipalId.type='TERMINALID'
    context.initiatorPrincipalId.userId=None
    client.assignSeqrId(context, "0046700000101")

 
### Try more functions
Please contact us to get APIs and examples for: 

- Kiosk, web purchase trough the app. (TV commercials, Ads, Parking)

- Signing up new SEQR users and getting a kick-back. 

- Loyalty/Membership managment