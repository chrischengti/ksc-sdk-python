#!/usr/bin/python
# -*- encoding:utf-8 -*-

#使用方法
'''
examples
'''

from kscore.session import get_session
import sys,pprint
import time
from kscore.exceptions import ClientError

ks_access_key_id =''
ks_secret_access_key = ''
region = 'cn-shanghai-2'


def getLines():
    try:
        res = eipClient.get_lines()
	print res
        return res['LineSet']
    except ClientError, e:
        print 'error '+str(e)
def describeAddresses(AllocationIdN=None,ProjectIdN=None,MaxResults=None,NextToken=None):
    param = {}
    if AllocationIdN:
        param.update(dict(("AllocationId.{}".format(index), item) for index, item in enumerate(AllocationIdN, 1)))
    if ProjectIdN:
        param.update(dict(("ProjectId.{}".format(index), item) for index, item in enumerate(ProjectIdN, 1)))        
    try:
        print param
        res = eipClient.describe_addresses(**param)
        for eip in res['AddressesSet']:
	    print eip
    except ClientError, e:
        print 'error '+str(e)
def allocateAddress(LineId,BandWidth,ChargeType,PurchaseTime=0,ProjectId=0):
    res = None
    param = {
            "LineId": LineId,
            "BandWidth": BandWidth,
            "ChargeType" : ChargeType,
            "PurchaseTime": PurchaseTime,
        }    
    try:
        if ChargeType == 'Daily':
            res = eipClient.allocate_address(**param)
	    print res
    except ClientError, e:
        print 'error '+str(e)
def associateAddress(AllocationId,InstanceType,InstanceId,NetworkInterfaceId):
    res = None
    param = {
            "AllocationId": AllocationId,
            "InstanceType": InstanceType,
            "InstanceId" : InstanceId,
            "NetworkInterfaceId": NetworkInterfaceId,
        } 
    try:
        res = eipClient.associate_address(**param)
	print res
    except ClientError, e:
        print 'error '+str(e)
def disassociateAddress(AllocationId):
    try:
        res = eipClient.disassociate_address(AllocationId=AllocationId)
	print res
    except ClientError, e:
        print 'error '+str(e)
def releaseAddress(AllocationId):
    try:
        res = eipClient.release_address(AllocationId=AllocationId)
	print res
    except ClientError, e:
        print 'error '+str(e)
def getAccountAllProjectList():
    try:
        res = iamClient.get_account_all_project_list()
        return res['ListProjectResult']['ProjectList']
    except ClientError, e:
        print 'error '+str(e)
if __name__ == "__main__":
    s = get_session()
    #s.set_credentials(ks_access_key_id, ks_secret_access_key)
    vifClient = s.create_client("vpc", region, use_ssl=True)
    kecClient = s.create_client("kec", region, use_ssl=True)
    eipClient = s.create_client("eip", region, use_ssl=True)
    slbClient = s.create_client("slb", region, use_ssl=True)
    iamClient = s.create_client("iam", region, use_ssl=True)
    lineId = None
    for line in getLines():
        if line['LineName'] == 'BGP':
            lineId = line['LineId']
    #allocateAddress(lineId,1,'Daily')
    #eips=['d2a6c424-8d32-424f-84d5-f41aef59fd11','ecfae0a6-8d8c-49c9-aa04-20bc2492fc3a']
    projects=[100012,100013]
    #describeAddresses(ProjectIdN=projects)
    describeAddresses(AllocationIdN=[],ProjectIdN=projects)
    #pprint.pprint(getAccountAllProjectList())
    #associateAddress('2835602d-d12d-4799-bfb0-0331ef1e4edc','Ipfwd','8749bb48-0c63-444a-80ce-0bd9d0d91f34','8fced74a-e232-4916-8023-1febd55fb1a2')
    #disassociateAddress('2835602d-d12d-4799-bfb0-0331ef1e4edc')
    #releaseAddress('2835602d-d12d-4799-bfb0-0331ef1e4edc')
