from suds.client import Client
import logging
import time, sys
import qrcode
import tempfile

# only for debugging
#logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.DEBUG)

client = Client('https://extdev4.seqr.se/soap/merchant/cashregister-2?wsdl')
context = client.factory.create("ns0:clientContext")
context.clientRequestTimeout = 0

# see the terminal registration example to know where this value came from
context.initiatorPrincipalId.type = 'TERMINALID'
context.initiatorPrincipalId.id = '8609bf533abf4a20816e8bfe76639521'
context.password = 'N2YFUhKaB1ZSuVF'


print "Creating the invoice..."

invoice = client.factory.create("ns0:invoice")
invoice.paymentMode = "IMMEDIATE_DEBIT"
invoice.acknowledgmentMode = "NO_ACKNOWLEDGMENT"
invoice.title="Grand Cinema"
invoice.invoiceRows = client.factory.create('ns0:invoiceRows')
row1 = invoice.invoiceRows.invoiceRow = client.factory.create('ns0:invoiceRow')
row1.itemDescription = "Movie Tickets"
row1.itemTotalAmount = client.factory.create('ns0:itemTotalAmount')
row1.itemTotalAmount.value, row1.itemTotalAmount.currency = "500", "SEK"

invoice.totalAmount = client.factory.create('ns0:totalAmount')
invoice.totalAmount.value, invoice.totalAmount.currency = "500", "SEK"

print "Sending the invoice to SEQR..."

invoiceResponse = client.service.sendInvoice(context, invoice)
if invoiceResponse.resultCode != 0:
    print ("Oops... sendInvoice failed! error: %s(%d)"%
	(invoiceResponse.resultDescription, invoiceResponse.resultCode))
    exit(1)

qr = qrcode.QRCode()
qr.add_data(invoiceResponse.invoiceQRCode)
print ("Invoice created with id %s, scan this QR code to pay the invoice:"%
    invoiceResponse.invoiceReference)
qr.print_tty()

# wait for payment
response = client.service.getPaymentStatus(context,
	    invoiceResponse.invoiceReference)
while response.resultCode == 0 and response.status == "ISSUED":
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(1)
    response = client.service.getPaymentStatus(context,
		invoiceResponse.invoiceReference)

print
if response.resultCode != 0:
    print ("Oops... getPaymentStatus failed! error: %s(%d)"%
	(invoiceResponse.resultDescription, invoiceResponse.resultCode))
    exit(1)

if response.status == "PAID":
    print "Payment successfull!"
else:
    print "Payment unsuccessful, invoice status is " + response.status
