hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")
h = float(hrs)
r = float(rate)
def computepay(h,r):
    ot= h - 40
    pay = (40 * r) + (ot * (r * 1.5))
    return pay   

if h > 40:
    pay = computepay(h,r)
    
else: 
    pay = h * r

print pay
 
    
 
