from json import dumps
from datetime import datetime
from re import S
from httplib2 import Http

#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
#if (current_time == "16:03"):

person = input("Who would you like to message? ")

if person == "damian":
    url = "https://chat.googleapis.com/v1/spaces/x2Zg44AAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=z8_1vfBjQFkP4cEior9htb4LRBS7-_Y_mxE1AuLOZmY%3D"
if person == "daves":
    url =  "https://chat.googleapis.com/v1/spaces/iHk224AAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=ja1YeyOeK2PKXYiKgeJcnlzDJ1B7AhbHTr9gsw2EsfU%3D"
if person == "neilh":
    url = "https://chat.googleapis.com/v1/spaces/s144cEAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=9ejU9kXXzMoOh5jH9U8wal_HrwMYwANPA8CHfD2uOHA%3D"
if person == "jeff":
    url = "https://chat.googleapis.com/v1/spaces/6Y7w44AAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=k3ogAaivRFQ1i91P66IEQBWXusoR0SoMW81Lb3oOvTc%3D"
if person == "neils":
    url = "https://chat.googleapis.com/v1/spaces/wpLbk4AAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=ggAEj3opUk-mjQFyVtB_z8zqGlKiSe1QOhnSmf9EXpU%3D"
if person == "scott":
    url = "https://chat.googleapis.com/v1/spaces/_tQvaEAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=lRm2j8AXFxGHEM-aSSnNArWc2sw9uF0totwj9CrGUQQ%3D"
str = input("What should I send? ") # takes input to send


def main():     #connect & send message
    
    bot_message = {'text': str}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)

if __name__ == '__main__': #if true run main() ^^^
    main()
 
