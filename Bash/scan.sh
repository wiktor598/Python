#!/bin/bash



echo "Enter the starting IP address: "
read addr

nmap -sT $addr

