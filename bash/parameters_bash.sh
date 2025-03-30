#!/usr/bin/env bash
# 
#echo "all params $*"
#echo "number of params : $#"

for param in $*
 do
  if [ -d "$param" ]
  then
    echo " executing in the config folder"
    ls -l "$param"
  fi
  echo $param
 done

 function score_sum {
 sum=0
  while true
  do
   read -p "enter the score:" score
   if [ $score == "q" ]
   then
   break
  fi
  sum=$(($sum+$score))  # this transorms from string to integer
   echo "total score is : $sum"
done
 }

function create_file() { #never use more than 5 paramters
 file_name=$1
 is_shell_script=$2
 touch $file_name
 echo "file with $file_name created"

 if [ "$is_shell_script" == true ]
 then
  chmod u+x $file_name
  echo "added execute permission"
  fi
}
create_file test.txt  #this is the argument passed though the function. just like in python 
create_file config.yaml 
create_file myscript.sh

function sum() {
  total=$(($1+$2))
  return $total
}
sum 2 190 #assign parameters to function 
result=$? #access result of the previous command execution and stores it. In this case is $total
echo "sum of first arg and second arg is $result"


