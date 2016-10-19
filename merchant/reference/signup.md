---
layout: default
title: SEQR Integration Sign up
description: SEQR Integration Sign up
---

# Get login credentials

You need to [contact](/contact) SEQR to get reseller ID and password. With these you call the registerTerminal API request to receive a terminal ID. Then the terminal ID and password can be used to make payment requests.

Notice: on production environment SEQR Customer Service provides with credentials. For POS a merchant is provided with resellerId for each one shop.  

# SEQR test credentials

Example terminal context, that can be used before contacting us:
{% highlight python %}
context.initiatorPrincipalId.type = 'TERMINALID'
context.initiatorPrincipalId.id = 'public_test_shop_terminal'
context.password = '12345678'
{% endhighlight %}

Example shop/reseller context, that can be used before contacting us:
{% highlight python %}
context.initiatorPrincipalId.type = 'RESELLERUSER'
context.initiatorPrincipalId.id = 'public_test_shop'
context.initiatorPrincipalId.userId = '9900'
context.password = '1234'
{% endhighlight %}

# eProducts test credentials

{% highlight python %}
context.clientId = 'samplereseller'
context.clientUserId = '9900'
context.password = '12345678'
{% endhighlight %}