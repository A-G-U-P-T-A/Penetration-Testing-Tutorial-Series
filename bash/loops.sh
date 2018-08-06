#!/bin/bash
echo "for loop"
for i in {5..25..5}; do
	echo "The value is $i"
done
echo "while loop"
i=5
while [ $i -le 25 ]; do
	echo "The value is $i"
	let i=i+5
done
i=5
echo "until loop"
until [ $i -gt 25 ]; do
	echo "The value is $i"
	let i=i+5
done
