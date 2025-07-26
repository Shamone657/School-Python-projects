import math

while True:
 
 print("------------------------------------------------------------------------------------------------------------------------------------------------------") #seperator 

 formula = input("Select a formula: (1) v = u + at, (2) s = (u + v) / 2 t, (3) s = ut + 1/2at², (4) v² = u² + 2as \n") #formula selector

 formula = formula.lower()

 if formula in ["1" , "v" , "v=u+at" , "v=u"]: #formula v = u + at

  formula_1 = input("Select what letter you are looking for: initial velocity (u), acceleration (a), time (t), final velocity (v)")

  if formula_1 in ["v", "final velocity"]: #looking for final velocity (v)
   
   u = float(input("Enter initial velocity (u)"))

   a = float(input("Enter acceleration (a)"))

   t = float(input("Enter time (t)"))

   v = u + (a * t)

   print(v)

  elif formula_1 in ["u", "inital velocity"]: #looking for initial velocity (u) 
   
   v = float(input("Enter final velocity (v)"))

   a = float(input("Enter acceleration (a)"))

   t = float(input("Enter time (t)"))

   p = (a * t)  

   u = v - p

   print(u)

  elif formula_1 in ["a", "acceleration"]: #looking for acceleration (a) 
   
   v = float(input("Enter final velocity (v)"))

   t = float(input("Enter time (t)"))

   u = float(input("Enter initial velocity (u)"))

   if u < 0: 

    p = v + u 

    a = p / t

    print(a)

   else:

    p = v - u

    a = p / t

    print(a)

  elif formula_1 in ["t", "time"]: #looking for time (t) 
   
   v = float(input("Enter final velocity (v)"))

   a = float(input("Enter acceleration (a)"))

   u = float(input("Enter initial velocity (u)"))

   if u < 0:

    p = v + u 

    t = p / a

    print(t)

   else:

    p = v - u

    t = p / a

    print(t)

 elif formula in ["2" , "s" , "s=u+v" , "s=(u+v)/2t"]: #s = (u + v) / 2 t
   
  formula_2 = input("Select what letter you are looking for: initial velocity (u), distance (s), time (t), final velocity (v)")

  if formula_2 in ["s", "distance"]: #looking for distance (s)
   
   u = float(input("Enter initial velocity (u)"))

   v = float(input("Enter final velocity (v)"))

   t = float(input("Enter time (t)"))

   s = ((u + v) / 2) * t

   print(s)

  elif formula_2 in ["t", "time"]: #looking for time (t)
   
   u = float(input("Enter initial velocity (u)"))

   v = float(input("Enter final velocity (v)"))

   s = float(input("Enter distance (s)"))

   p = (u + v) / 2

   t = s / p

   print(t)

  elif formula_2 in ["u", "initial velocity"]: #looking for initial velocity (u)
   
   t = float(input("Enter time (t)"))

   v = float(input("Enter final velocity (v)"))

   s = float(input("Enter distance (s)"))


 
 elif formula in ["3" , "sut"  , "s=ut+1/2at**2" , "at**2"]: #formula s = ut + 1/2at**2

  formula_3 = input("Select what letter you are looking for: initial velocity (u), distance (s), time (t), acceleration (a)")

  if formula_3 in ["s", "distance"]:
 
   u = float(input("Enter initial velocity (u)"))

   a = float(input("Enter acceleration (a)"))

   t = float(input("Enter time (t)"))

   s = u * t + 0.5 * a * t ** 2

   print(s)

  elif formula_3 in ["u", "initial velocity"]:
 
   s = float(input("Enter distance (s)"))

   a = float(input("Enter acceleration (a)"))

   t = float(input("Enter time (t)"))

   p = 0.5 * a * t ** 2

   u = (s - p) / t

   print(u)

  elif formula_3 in ["a", "acceleration"]:
 
   s = float(input("Enter distance (s)"))

   u = float(input("Enter initial velocity (u)"))

   t = float(input("Enter time (t)"))

   p = u * t

   q = s - p

   z = t ** 2 * 0.5

   a = q / z

   print(a)

  elif formula_3 in ["t", "time"]:
 
   s = float(input("Enter distance (s)"))

   a = float(input("Enter acceleration (a)"))

   u = float(input("Enter initial velocity (u)"))



 elif formula in ["4" , "v**2" , "v**2=u**2+2as" , "v2"]: #formula v**2 = u**2 + 2as

  formula_4 = input("Select what letter you are looking for: initial velocity (u), distance (s), final velocity (v), acceleration (a)")

  if formula_4 in ["v", "final velocity"]:
 
   u = float(input("Enter initial velocity (u)"))

   a = float(input("Enter acceleration (a)"))

   s = float(input("Enter distance (s)"))

   v = u ** 2 + 2 * a * s 

   print(math.sqrt(v))

  elif formula_4 in ["u", "initial velocity"]:
 
   v = float(input("Enter final velocity (v)"))

   a = float(input("Enter acceleration (a)"))

   s = float(input("Enter distance (s)"))

   p = v ** 2 

   q = 2 * a * s

   u = p - q

   print(math.sqrt(u))

  elif formula_4 in ["a", "acceleration"]:
 
   v = float(input("Enter final velocity (v)"))

   u = float(input("Enter initial velocity (u)"))

   s = float(input("Enter distance (s)"))

   new_v = v ** 2

   new_u = u ** 2

   new_s = 2 * s

   q = new_v - new_u

   a = q / new_s

   print(math.sqrt(a))

  elif formula_4 in ["s", "distance"]:
 
   v = float(input("Enter final velocity (v)"))

   u = float(input("Enter initial velocity (u)"))

   a = float(input("Enter acceleration (a)"))

   new_v = v ** 2

   new_u = u ** 2

   new_a = 2 * a

   q = new_v - new_u

   s = q / new_a

   print(math.sqrt(s))

 else:
 
  print("Try again")
  
  continue


