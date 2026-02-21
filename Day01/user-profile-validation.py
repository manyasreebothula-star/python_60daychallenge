name=input("Please enter your full name: ")
email=input("Please enter your email: ")
mobile=input("Please enter your mobile number: ")
age=int(input("Please enter your age: "))

valid=True

        #full name validation
if name[0]==" " or name[len(name)-1]==" ":
    valid=False
elif name.count(" ")<1:
    valid=False

         #email ID validation
if email.count("@") < 1 or email.count(".") < 1:
      valid=False
elif email[0] == "@" :
      valid=False

         #mobile number validation
if len(mobile) != 10:
      valid=False
elif mobile.isdigit()==False:
      valid=False
elif mobile[0]=="0":
      valid=False

         #age validation
if age < 18 or age >60 :
  valid=False

if valid:
    print("User profile VALID")
else:
    print("User profile INVALID")
