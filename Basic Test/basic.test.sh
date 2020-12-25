#!/bin/bash
check_result () {
  RESULT=$?
  MESSAGE=$1
  if [ $RESULT == 0 ]; then
    echo [SUCCESSFULLY] $MESSAGE
  else
    echo [FAILED] $MESSAGE
    exit 1
  fi
}

for sentiment in City Country Region ; do
  docker run iplocation -i 8.8.8.8 | grep $sentiment
  check_result $sentiment
done

exit 0