
while 1:
  low = float(input("low:"))
  high = float(input("high:"))
  direct = int(input("up or down:(1 or 2) "))
  diff = high-low
  if direct==1:
    sl = low
    tp = high+diff
  else:
    pDiff = float(input("point diff="))
    sl = high+2*pDiff
    tp = low-diff+2*pDiff
  print("Stop Loss = %f, Take Profit = %f"%(sl, tp))
  again = int(input("Again?(1:yes, other: no) "))
  if again != 1:
    break

