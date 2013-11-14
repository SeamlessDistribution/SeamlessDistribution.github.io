---
layout: default
title: POS Payments
description: SEQR Merchant, webshop, POS integration
---

<img src="/assets/images/cash_register_bw.png" align="right" width="200px"/>

## Get Paid at Physical POS

When getting a payment through physical POS, we cannot show the payment QR code
which is generated for the invoice to the end customer. To overcome that problem,
we assign a fixed QR code to each POS. A POS SEQR sticker looks like this:

<img src="/assets/images/seqr-qrcodes.png" width="200px"/>

To register a SEQR sticker, please take a look at the following sample:

{% highlight python %}
{% include registerTerminal.py %}
{% endhighlight %}
