#!/bin/bash

SERVER=127.0.0.1
PORT=12321

INFO=`w -hs |awk '{print $3}'`
if [ $# == 1 ]
then
  INFO=$1
fi
if [ ! -n "$INFO" ]
then
  echo "is Null"
  exit -1
fi
echo " "$INFO > /tmp/dog

nc $SERVER $PORT -u -q 1 < /tmp/dog
