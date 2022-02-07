import random
randNumber = random.randint(1, 6)
print(randNumber)

if(randNumber == 1):
    print("""

 *

""")
elif(randNumber == 2):
    print("""
*

  *
""")
elif(randNumber == 3):
    print("""
*
 *
  *
""")
elif(randNumber == 4):
    print("""
* *

* *
""")
elif(randNumber == 5):
    print("""
* *
 *
* *
""")
elif(randNumber == 6):
    print("""
* *
* *
* *
""")
