# (2)# -Write a program that takes a number and determine whether it is a tens, hundred, thousand or million.
#  Use arithmetic operation to determine this
# for number 2, when you divide by either of the tens, hundred, thousand and million- it must give a whole number


def calb(num):
   x= num // 10
   y=num // 100
   z=num // 1000
   a=num // 1000000
   if 1 <= x  and x < 10:
      return "tens"
   if 1 <= y and y < 10:
      return "hundreds"
   if 1 <= z and z < 1000:
      return "thousands"
   if 1 <= a and z < 1000:
      return "millions"
   else:
      return "number is greater than million"

print(calb(300100))



