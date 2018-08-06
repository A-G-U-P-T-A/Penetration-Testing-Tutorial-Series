#!/bin/bash
#declaring an array
pl=('python' 'perl' 'C' 'C++' 'JAVA' 'lua')
echo ${pl[1]} #accessing a particular element
echo ${pl[@]} #accessing the whole array
for i in "${pl[@]}"; #prints the elements using for each loops
do
	echo $i
done
pl=("${pl[@]}" "Assembly") #adding a new element
echo ${pl[@]}
nl=('Go' 'HTML' 'CSS')
pl=("${pl[@]}" "${nl[@]}")
echo ${pl[@]}
