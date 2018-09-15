def printText(x):
    print(x)
    return
def prob1(u,v):
    A=abs(u-v)
    B=(abs(u-v))/(abs(u))
    # print(B)
    return B




def demo_routine(num):
 print('I am a demo function')
 if num % 2 == 0:
  return(True)
 else:
  return(False)

num = int(input('Enter a number:'))
if demo_routine(num) is True:
 print(num, 'is an even number')
else:
 print(num, 'is an odd number')
