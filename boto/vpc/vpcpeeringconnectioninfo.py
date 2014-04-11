from boto.ec2.ec2object import TaggedEC2Object

class VPCPeeringConnectionInfo(TaggedEC2Object):

    def __init__(self, connection=None):
	super(VPCPeeringConnectionInfo, self).__init__(connection)
	self.APIVersion = '2014-02-01'
	self.vpcid = None
	self.ownerid = None
	self.cidrblock = None

    def __repr__(self):
	return 'VPCPeeringConnectionInfo:%s' % self.vpcid

    def startElement(self, name, attrs, connection):
	pass

    def endElement(self, name, value, connection):
	if name == 'ownerId':
		self.ownerid = value
	if name == 'vpcId':
		self.vpcid = value
	if name == 'cidrBlock':
		self.cidrblock = value
	else:
		setattr(self, name, value)


