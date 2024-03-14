nric = input('Enter an NRIC number: ')
# Type your code below
dweight,sttable,fgtable,prod  = "2765432","JZIHGFEDCBA0","XWUTRQPNMLK0",-1
if len(nric) == 9 and nric[1:8].isdigit():
  prod = sum([int(nric[i])*int(dweight[i-1]) for i in   range(1,8)],int(nric[0] in "TG")*4)%11
print("NRIC is " + int(not(((nric[0] in "ST")*(sttable[prod]) + (nric[0] in "FG")*(fgtable[prod])) == nric[-1]))*"in" + "valid.")
  