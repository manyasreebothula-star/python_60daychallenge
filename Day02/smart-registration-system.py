studentID=input("enter your id: ")
email=input("enter your email: ")
password=input("enter your password: ")
referral=input("enter your referral: ")

valid = True

#studentID validation:-
if len(studentID) != 7:
    valid = False
elif studentID[0] != "C" and studentID[1] != "S" and studentID[2] != "E":
    valid = False
elif studentID[3] != "-" :
    valid = False
elif not(studentID[4].isdigit() and studentID[5].isdigit() and studentID[6].isdigit()):
    valid = False

#email validation:-
elif "@" not in email or "." not in email:
    valid = False
elif email[0] == "@" or email[-1] == "@":
    valid = False
elif email[-4:] != ".edu":
    valid = False

#password validation:-
elif len(password) < 8:
    valid = False
elif  not password[0].isupper():
    valid = False
elif not(password[0].isdigit() or password[1].isdigit() or password[2].isdigit()
    or password[3].isdigit() or password[4].isdigit() or password[5].isdigit
         or password[6].isdigit() or password[7].isdigit()):
    valid = False

#referral validation:-
elif len(referral) != 6:
    valid = False
elif not(referral[0] == "R" or referral[1] == "E" or referral[2] == "F"):
    valid = False
elif not(referral[3].isdigit() and referral[4].isdigit()):
    valid = False
elif referral[5] != "@":
    valid = False

#output:-
if valid:
    print("APPROVED")
else:
    print("REJECTED")
