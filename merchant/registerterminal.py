#!/usr/bin/python

import suds
from suds.client import Client
import logging

# only for debugging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

client = Client('http://extdev2.seqr.se:8913/extclientproxy/service?wsdl')
context = client.factory.create("ns0:clientContext")
context.channel="ws"
context.clientId="client"
context.clientRequestTimeout=0
context.initiatorPrincipalId.id='pcms'
context.initiatorPrincipalId.type='RESELLERUSER'
context.initiatorPrincipalId.userId='9900'
context.password='1817846'
r1 = client.service.registerTerminal(context, 'externalTerminalId', '123', 'my cashregsiter')
print r1.terminalId


context.initiatorPrincipalId.id=r1.terminalId
context.initiatorPrincipalId.type='TERMINALID'
context.initiatorPrincipalId.userId=None
client.assignSeqrId(ns0:clientContext context, "0046700000101")


