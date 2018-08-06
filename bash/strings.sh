#!/bin/bash
#initialize a string
a="Hello"
echo "The string is $a"
#stubstitution operation on string
echo "$a{a/ll/LL}"
#slicing a string
echo "${a:1:3}"
echo "${a::4}"
echo "${a::-1}"
