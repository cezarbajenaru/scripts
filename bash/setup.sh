#!/usr/bin/env bash
echo "Setup and configure server"

file_name=config.yaml

config_dir=$1

if [ -d "$config_dir" ]
then
	echo "reading config directory contents"
	config_files=$(ls "$config_dir")
else
	echo "Config dir not found. Creating one"
	mkdir "$config_dir"
	touch "$config_dir/config.sh"
fi

user_group=$2

if [ "$user_group" == "cezar" ]
then
	echo "configure the server"
elif [ "$user_group" == "admin" ]
then
	echo " administer the server"
else
	echo "no permission to configure server. wrong user group"
fi

echo "Using file $file_name to configure something"
echo "Here are all iconfiguration files: $config_files"
