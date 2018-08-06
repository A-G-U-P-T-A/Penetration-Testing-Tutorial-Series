#!/bin/bash
cat file | while read line; do
	echo $line
done
