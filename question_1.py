# (1)# Write a program that can return highest common factor of two numbers.
def h_fac(x, y):
   fac_x=[]
   fac_y=[]
   hfac=[]
   for fac in range(1, x+1):
      if x % fac == 0:
         fac_x.append(fac)
   for fac_1 in range(1, y+1):
      if y % fac_1 == 0:
         fac_y.append(fac_1)
   for num in fac_x:
      if num in fac_y:
         hfac.append(num)
   print(hfac)
   print(hfac[-1])

h_fac(24, 48)