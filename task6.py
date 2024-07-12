def divion(x,y):
 try:
  return x/y
 except ZeroDivisionError:
  print("div tow number result = Zero")
try:
 (divion(5,0))
except Exception as e:
 print(e)

 #  def divion(x,y):
#   return x/y
# #  except ZeroDivisionError:
# #   print("div tow number result = Zero")
# try:
#  (divion(5,0))
# except Exception as e:
#  print(e)

