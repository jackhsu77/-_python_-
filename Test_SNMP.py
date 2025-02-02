from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.hlapi.asyncio import *

from pysnmp.hlapi import *

import asyncio

async def run(snmpEngine, transportDispatcher):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, transportDispatcher.runDispatcher)

snmpEngine = SnmpEngine()

# 配置SNMPv3用户
config.addV3User(
    snmpEngine, 
    userName='yourUser', 
    authProtocol=usmHMACSHAAuthProtocol, authKey='yourAuthKey',
    privProtocol=usmAesCfb128Protocol, privKey='yourPrivKey'
)

# 开始监听端口162
transportDispatcher = SnmpDispatcher(snmpEngine)
transportDispatcher.registerTransport(
    udp.UdpTransport().openServerMode(('localhost', 162))
)

# 处理接收到的Trap
def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    print('Received new Trap message')
    for name, val in varBinds:
        print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))

# 注册Trap接收器
snmpEngine.transportDispatcher.jobStarted(1)
snmpEngine.msgAndPduDsp.registerContextEngineId(
    snmpEngine.snmpEngineID, snmpEngine.contextEngineId, cbFun)

# 运行监听
loop = asyncio.get_event_loop()
loop.run_until_complete(run(snmpEngine, transportDispatcher))
