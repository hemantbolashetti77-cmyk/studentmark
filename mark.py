import sys
if len(sys.argv) !=6:
      print("Usage: python mark.py <sub1> <sub2>")
      sys.exit(1)

script_name = sys.argv[0]
sub1 = sys.argv[1]
sub2= sys.argv[2]
sub3 = sys.argv[3]
sub4 = sys.argv[4]
sub5 = sys.argv[5]
avg=(sub1+sub2+sub3+sub4+sub5)/5
print("Average marks",avg)
print("Grade")
if avg>=90 :
  print("A")
else avg>=80 :
 print("B")
else avg>=70 :
 print("C")
else avg>=60 :
 print("D")
else avg<60 :
 print("Fail")
