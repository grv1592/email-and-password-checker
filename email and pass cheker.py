import re

pattern1 = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

while True:
    email = input("please enter emial id :")
    if pattern1.search(email):
        print('thank you!')
        break
    else:
        print('please try again')

pattern2 = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$")

while True:
    password = input("enter the password: ")
    if pattern2.search(password):
        print('thank you!')
        break
    else:
        print('enter again')

