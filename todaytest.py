# using part of the lsat exercise 
jhr = input("Enter Hours:")
jr = input("Enter Rate:")
try:  
    fh = float (jhr)
    fr = float (jr) 
except:
    print ("Error, please enter numeric input")
    quit ()

   #print (fh,fr)

if fh > 40 :
    regpay = fh * fr
    otpay  = (fh - 40.0) * (0.5 * fr)
    totalpay = regpay + otpay
else :

    totalpay = fh * fr 


print("Pay:", totalpay)


