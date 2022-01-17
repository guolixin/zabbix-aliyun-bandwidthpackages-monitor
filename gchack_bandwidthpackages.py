#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Author: guo8
# Date:2022/01/15
# Last modified:
# zabbix键值设置
# gchack_bandwidthpackages[ak_id ak_Secret instanceId net_rx.rate]
#
# vim zabbix_agentd.conf
# UnsafeUserParameters=1
# UserParameter=gchack_bandwidthpackages[*],/usr/bin/python3 /etc/zabbix/script/gchack_bandwidthpackages.py $1 $2 $3 $4
#
# https://next.api.aliyun.com/api/Cms/2019-01-01/DescribeMetricLast?lang=PYTHON&params={%22Namespace%22:%22acs_bandwidth_package%22,%22MetricName%22:%22net_rx.rate%22}&tab=DEMO
# https://help.aliyun.com/document_detail/51939.html
# https://help.aliyun.com/document_detail/165008.htm?spm=a2c4g.11186623.0.0.d5191c27qu4Pj7#concept-2495480
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkcms.request.v20190101.DescribeMetricLastRequest import DescribeMetricLastRequest
import sys,json

def chack_instanceId(info,in_instanceId):
    if "instanceId" in info['Datapoints']:
        for i in eval(info['Datapoints']):
            temp_date1 =dict(i)
            if in_instanceId in temp_date1['instanceId']:
                #返回Mbps
                return float(temp_date1['Value'])/1024/1024
    else:
        return float(0)


def gchack_bandwidthpackages(in_access_key_id,in_access_key_secret,in_instanceId,in_MetricName):
    credentials = AccessKeyCredential(in_access_key_id, in_access_key_secret)
    # use STS Token
    # credentials = StsTokenCredential('<your-access-key-id>', '<your-access-key-secret>', '<your-sts-token>')
    client = AcsClient(region_id='cn-beijing', credential=credentials)

    request = DescribeMetricLastRequest()
    request.set_accept_format('json')

    request.set_Namespace("acs_bandwidth_package")
    request.set_MetricName(in_MetricName)

    return chack_instanceId(json.loads(client.do_action_with_exception(request)),in_instanceId)

if __name__ == '__main__':
    # test:
    # python3.exe .\gchack_bandwidthpackages.py ak_id ak_Secret instanceId net_rx.rate
    chack_bandwidth = gchack_bandwidthpackages(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    print(chack_bandwidth)
