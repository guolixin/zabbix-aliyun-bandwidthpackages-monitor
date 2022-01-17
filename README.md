# zabbix-aliyun-bandwidthpackages-monitor
zabbix抓取阿里云流量包信息
使用方法：
1、编辑zabbix配置
# vim zabbix_agentd.conf
# UnsafeUserParameters=1
# UserParameter=gchack_bandwidthpackages[*],/usr/bin/python3 /etc/zabbix/script/gchack_bandwidthpackages.py $1 $2 $3 $4
#
2、在zabbix中导入模板
3、添加主机，Macro中填写参数阿里云参数
    1){$GAK_ID} 阿里云akid至
    2){$GAK_SECRET} 阿里云akid对应密钥
    3){$GINSTANCEID} 流量包实例ID cbwp-****
    4){$GBANDWIDTH} 预设带宽上限
