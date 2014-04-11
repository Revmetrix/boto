# Copyright (c) 2009-2010 Mitch Garnaat http://garnaat.org/
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""
Represents a VPC Peering Connection 
"""

from boto.ec2.ec2object import TaggedEC2Object
from boto.resultset import ResultSet
from boto.vpc.vpcpeeringconnectioninfo import VPCPeeringConnectionInfo
from boto.handler import XmlHandler
import xml.sax

class Status(TaggedEC2Object):
    def __init__(self, connection=None):
        super(Status, self).__init__(connection)
	self.code = None
	self.message = None

    def startElement(self, name, attrs, connection):
        result = super(Status, self).startElement(name, attrs, connection)

    def endElement(self, name, value, connection):
        setattr(self, name, value)


class VPCPeeringConnection(TaggedEC2Object):

    def __init__(self, connection=None):
        super(VPCPeeringConnection, self).__init__(connection)
	self.APIVersion = '2014-02-01'
        self.id = None
	self.requesterVpc = None
	self.accepterVpc = None
	self.status = None
	self.expirationTime = None

    def __repr__(self):
        return 'VPCPeeringConnection:%s' % self.id
    """
	<requesterVpcInfo>
            <ownerId>777788889999</ownerId>
            <vpcId>vpc-vpc-1a2b3c4d</vpcId>
            <cidrBlock>10.0.0.0/28</cidrBlock>
        </requesterVpcInfo>
        <accepterVpcInfo>
            <ownerId>123456789012</ownerId>
            <vpcId>vpc-a1b2c3d4</vpcId>
        </accepterVpcInfo>
        <status>
            <code>initiating-request</code>
            <message>Initiating Request to 123456789012</message>
        </status>
        <expirationTime>2014-02-18T14:37:25.000Z</expirationTime>
     """

    def startElement(self, name, attrs, connection):
        result = super(VPCPeeringConnection, self).startElement(name, attrs, connection)

        if result is not None:
            # Parent found an interested element, just return it
            return result

        if name == 'requesterVpcInfo':
	    self.requesterVpc = VPCPeeringConnectionInfo()
            return self.requesterVpc
        elif name == 'accepterVpcInfo':
	    self.accepterVpc = VPCPeeringConnectionInfo()
            return self.accepterVpc
	elif name == 'status':
	    self.status = Status()
            return self.status
        else:
            return None

    def endElement(self, name, value, connection):
        if name == 'vpcPeeringConnectionId':
            self.id = value
        else:
            setattr(self, name, value)
