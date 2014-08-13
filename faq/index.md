---
layout: default
title: Frequently Asked Questions
description: Frequently Asked Questions
---

Frequently Asked Questions
=============

Below you can find answers to the most common questions that may occur during the integration process.
 
<script>
 $(document).ready(function() {
 
    $('.faq_question').click(function() {
 
        if ($(this).parent().is('.open')){
            $(this).closest('.faq').find('.faq_answer_container').animate({'height':'0'},500);
            $(this).closest('.faq').removeClass('open');
 
            }else{
                var newHeight =$(this).closest('.faq').find('.faq_answer').height() +'px';
                $(this).closest('.faq').find('.faq_answer_container').animate({'height':newHeight},500);
                $(this).closest('.faq').addClass('open');
            }
 
    });
 
});
</script>
<style>
/*FAQS*/
.faq_question {
    margin: 0px;
    padding: 0px 0px 5px 0px;
    display: inline-block;
    cursor: pointer;
    font-weight: bold;
    color: #2EAE9B;
}
 
.faq_answer_container {
    height: 0px;
    overflow: hidden;
    padding: 0px;
}

.faq_container {
	margin-bottom: 5px;
}
 
</style>
 
<div class="faq_container">
   <div class="faq">
      <div class="faq_question">I've been using /extclientproxy/service?wsdl and now I'm trying to use /extclientproxy/service/v2?wsdl but after scanning QR code in SEQR app there is still “waiting for amount...” info even after calling sendInvoice by my point of sale. Why?</div>
           <div class="faq_answer_container">
              <div class="faq_answer">Probably the reason is missing
<pre><code class="python"><span class="n">&lt;</span>acknowledgmentMode<span>&gt;</span>NO_ACKNOWLEDGMENT<span>&lt;</span><span>/</span>acknowledgmentMode<span>&gt;</span></code></pre>
			in your sendInvoice request. See <a href="/merchant/reference/api.html">API</a> for details.</div>
           </div>        
    </div>
 </div>
<div class="faq_container">
   <div class="faq">
      <div class="faq_question">I've called markTransactionPeriod and used transactionPeriodId in executeReport for STD_RECON_006 or STD_RECON_007 reports but report is still not ready. Why?</div>
           <div class="faq_answer_container">
              <div class="faq_answer">In order to use terminal related reports you have to specify that terminal in markTransactionPeriod call by adding:
<pre><code class="python"><span class="p">&lt;</span><span class="n">parameters</span><span class="o">&gt;</span>
	<span class="o">&lt;</span><span class="n">entry</span><span class="o">&gt;</span>
		<span class="o">&lt;</span>key<span class="o">&gt;</span><span class="n">TERMINALID</span><span class="o">&gt;</span><span class="n"></span><span class="o">&lt;/</span><span class="n">key</span><span class="o">&gt;</span>
		<span class="o">&lt;</span>value<span class="o">&gt;</span><span class="n"><span class="o">&lt;</span>YOUR_TERMINAL_ID_HERE</span><span class="o">&gt;</span><span class="o">&lt;/</span><span class="n">value</span><span class="o">&gt;</span>
	<span class="o">&lt;/</span><span class="n">entry</span><span class="o">&gt;</span>
<span class="o">&lt;/</span><span class="n">parameters</span><span class="o">&gt;</span></code></pre>
			in your sendInvoice request. See <a href="/merchant/reference/api.html">API</a> for details.</div>
           </div>        
    </div>
 </div>
<div class="faq_container">
   <div class="faq">
      <div class="faq_question">I have a webshop. Can I use registerTerminal and register my own terminal that way?</div>
           <div class="faq_answer_container">
              <div class="faq_answer">No, you can't. Terminal registered by registerTerminal call will be of type “cash register”, so there will always be only one transaction on it. Every new sendInvoice call will cancel previous invoice. You have to use terminalID/password provided by Seamless.</div>
           </div>        
    </div>
 </div>
 <div class="faq_container">
   <div class="faq">
      <div class="faq_question">Can I use credentials from <a href="developer.seqr.com">developer.seqr.com</a> for integration purpose?</div>
           <div class="faq_answer_container">
              <div class="faq_answer">No, you can't. You should use credentials provided by Integrations team in startup kit as these credentials are unique and will be used during certification.</div>
           </div>        
    </div>
 </div>
  <div class="faq_container">
   <div class="faq">
      <div class="faq_question">Where can I find credentials to use for integration purpose?</div>
           <div class="faq_answer_container">
              <div class="faq_answer">Please check the document which name starts with “Account_information”</div>
           </div>        
    </div>
 </div>
 <div class="faq_container">
   <div class="faq">
      <div class="faq_question">I've downloaded SEQR Android application, and registered but I can't pay in my store. Why?</div>
           <div class="faq_answer_container">
              <div class="faq_answer">Make sure you have chosen <b>Extdev</b> server from the list during registration.</div>
           </div>        
    </div>
 </div>
 <div class="faq_container">
   <div class="faq">
      <div class="faq_question">I want to integrate my webshop with SEQR - do I have to implement all methods on my own?</div>
           <div class="faq_answer_container">
              <div class="faq_answer">You can implement all methods on your own the way you like. You can also use our <a href="https://github.com/SeamlessDistribution/seqr-webshop-plugin">plugin</a> which will simplify generating QR code and calling getPaymentStatus.</div>
           </div>        
    </div>
 </div>
 <div class="faq_container">
   <div class="faq">
      <div class="faq_question">I have certified webshop/POS system but want to implement method that wasn't implemented before. Should my webshop/POS system be recertified?</div>
           <div class="faq_answer_container">
              <div class="faq_answer">Yes. Every change made in SEQR API implementation should be recertified in order to avoid regression errors.</div>
           </div>        
    </div>
 </div>
 <div class="faq_container">
   <div class="faq">
      <div class="faq_question">I have used "notificationUrl" in sendInvoice request but it is called only when invoice status is changed to "PAID". Why? </div>
           <div class="faq_answer_container">
              <div class="faq_answer">Unfortunately the URL defined in "notificationUrl" will currently be called only once invoice is PAID. So if you're not using our <a href="https://github.com/SeamlessDistribution/seqr-webshop-plugin">plugin</a> then you have to implement getPaymentStatus and check status of invoice on your own.</div>
           </div>        
    </div>
 </div>













