#!/bin/bash
set -x
read -p "File Path " file_path
read -p "Username " user_name
read -p "Servername " Server_name 
read -p "Destination Path " Path

scp ${file_path} ${user_name}@$Server_name:${Path}



# test

