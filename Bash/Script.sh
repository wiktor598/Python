#!/bin/bash
set -x
read -p "File Path (Pulling from) " file_path 
read -p "Username (Pulling from Uname) " user_name
read -p "Servername (Pulling from IP) " Server_name 
read -p "Destination Path (pulling too) " Path

scp ${file_path} ${user_name}@$Server_name:${Path}



# test

sdcc