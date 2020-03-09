#!/usr/bin/env bash
# thrift --gen py -out ../ message.thrift

# !! windows version!!
thrift  --gen java -out X:\GitHub\MicroserviceDemo\message-thrift-service-api/src/main/java  X:\GitHub\MicroserviceDemo\message-thrift-python-service\thriftPkg\message1.thrift