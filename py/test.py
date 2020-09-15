# coding:utf-8
import sys

shard_count = int(sys.argv[1])  # 分片的个数

r = sys.argv[2]
T = sys.argv[3]
rate = sys.argv[5]  # rate
shard="0"
if shard_count == 1: # 单分片的情况下
    cmd = "cd dist;./tm-bench -rate " + rate + " -r " + r + " -T " + T +" -as 0 0S1.test:26657"
    print(cmd)
else:
    Send_shard = ""  # 要发往哪些分片
    shard_node = ""
    for i in range(0, shard_count ):
        a = str(i)
        if i == (shard_count-1):
            Send_shard = Send_shard + a
            shard_node = shard_node + a+"S1.test:26657"
        else:
            Send_shard = Send_shard + a + ","
            shard_node = shard_node + a+"S1.test:26657,"
    if shard_count == 0:
        Send_shard = Send_shard + ",1"
    cmd = "cd dist;./tm-bench -rate " + rate + " -r " + r + " -T " + T +" -as " + Send_shard + " -datafile token_transfers.csv " + shard_node

    print(cmd)
