from suds.client import Client
import logging
import random
import string

# only for debugging
#logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.DEBUG)

client = Client('https://extdev4.seqr.se/extclientproxy/service/v2?wsdl')
context = client.factory.create("ns0:clientContext")
context.clientRequestTimeout = 0
context.initiatorPrincipalId.type = 'RESELLERUSER'

# the following three parameters are provided by seamless for each shop
context.initiatorPrincipalId.id = 'public_test_shop'
context.initiatorPrincipalId.userId = '9900'
context.password = '1234'

def generatePassword(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(size))

password = generatePassword(15)

# register the terminal
response = client.service.registerTerminal(context, 'externalTerminalId', password, 'POS #2 in My Shop')
print "Terminal registered, terminal id: %s , terminal password: %s" % (response.terminalId, password)


