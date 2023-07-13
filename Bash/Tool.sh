#!/bin/bash


PS3='Please enter your choice: '
options=("Option 1" "Option 2" "Option 3" "Quit")

select option in "${options[@]}"

do
    case $opt in
        "Option 1")
            echo "you chose choice 1"
            ;;
        "Option 2")
            echo "you chose choice 2"
            ;;
        "Option 3")ss
            echo "you chose choice 3"
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

