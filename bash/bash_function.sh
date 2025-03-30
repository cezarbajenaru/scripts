#!/bin/env bash
#Accepts a username as an argument.
#Checks if the username already exists on the system.
#If it does not exist, creates the user and sets a default password.
#Ensures the user belongs to a specified group (e.g., developers).
#Outputs a message confirming whether the user was created or already exists.
function my_first_function {
sudo groupadd -f devops
 if grep -q "^$1:" /etc/passwd
 then
  echo "Username $1 is already in the users list"
 else
  sudo useradd -m -G devops $1
  read -s -p "Enter Password for $1 :  " user_password
  echo "$1:$user_password" | sudo chpasswd
  echo "User $1 has been added to Group"
 fi
}

logging_function() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> /var/log/user_creation.log
}

my_first_function "$1"
#chmod u+x bash_function.sh
#./bash_function.sh raluca