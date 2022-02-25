#!/bin/bash

#  ls /Users/51pwn/MyWork/ip2domain/data/country|xargs -I %|sed 's/\.txt//g'|xargs -I % mkdir -p xmldata/%

cd xmldata
ls|xargs -I W bash -c 'cat ../data/country/W.txt|xargs -I % echo "doMasscan %" > W/run1.sh'
