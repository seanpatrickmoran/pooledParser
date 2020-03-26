#!/bin/bash


A=$(wc -l < $1)
B=$(($A/1000))
for i in $(seq 1 $B); do
	VAR=$(expr $i - 1)
	echo "head -n ${i}000 $1|tail -n 1000 >JQ_${VAR}Kto${i}K.txt"
	head -n ${i}000 $1|tail -n 1000 > JQ_${VAR}Kto${i}K.txt
done
C=$(($B*1000))
D=$(($A-$C))
echo "tail -n ${D} > JQ_${B}KtoENDK.txt"
tail -n ${D} JQ_DB_NAMES.txt > JQ_${B}KtoENDK.txt
