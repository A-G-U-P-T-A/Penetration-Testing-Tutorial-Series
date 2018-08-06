#!/bin/bash
#simple function
func1(){
	echo "Function 1 called"
}
#passing parameters to a function
func2(){
	echo "$1 $2 $3"
}
#function returns value
func3(){
	echo "Function 3 called"
}
#calling the different functions
func1
func2 "Function" "2" "called"
func3_return=$(func3)
echo $func3_return
