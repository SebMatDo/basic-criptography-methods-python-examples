#!/usr/bin/env python3
# THIS EEA RETURNS GDC(A,B)
import math

def EEA(a,b):
	if b == 0:
		return (a,1,0)

	q = math.floor(a/b)
	derivadaD,derivadaX,derivadaY = EEA(b,a % b)
	d,x,y = (derivadaD, derivadaY, derivadaX - q * derivadaY)
	print("d: ",d , "x: ",x ,"y: ",y)
	return (d,x,y)

def main():
  a = int(input("Put a value: "))
  b = int(input("put b value: "))
  d,x,y = EEA(a,b)
  print("FINAL", "d: ",d , "x: ",x ,"y: ",y)


if __name__ == "__main__":
    main()