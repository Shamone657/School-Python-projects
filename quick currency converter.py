import math

while true:
   
   currency_1 = input("Enter the currency you want to convert (usd) (euro) (zlo)")
   
   currency_1 = currency_1.lower()
   
   currnecy_2 = currency_2.lower()
   
   if currency_1 in ["E", "Euro", "1"]:
       
       currency_2 = input("Enter the second currency you want to convert")
       
       if currency_2 in ["Z", "Zloty"]:
           
           euro = float(input("Enter how much Euro do you want to convert"))
           
           result = euro * 4.2
           
           print(result)
           
      elif currency_2 in ["D", "USD", "dollar", "2"]:
          
          euro = float(input("Enter how much Euro do you want to convert"))
          
          result = euro * 1.11
          
          print(result)
          
   elif currency_1 in ["Z", "Zloty"]:
       
       currency_2 = input("Enter the second currency you want to convert")
       
       if currency_2 in ["E", "Euro"]:
           
           zloty = float(input("Enter how much Zloty do you want to convert"))
           
           result = zloty * 0.23
           
           print(result)
           
      elif currency_2 in ["D", "USD", "dollar"]:
          
          zloty = float(input("Enter how much zloty do you want to convert"))
          
          result = zloty * 0.26
          
          print(result)
          
   elif currency_1 in ["usd", "dollar", "3"]:
       
       currency_2 = input("Enter the second currency you want to convert")
       
       if currency_2 in ["E", "Euro"]:
           
           zloty = float(input("Enter how much euro do you want to convert"))
           
           result = zloty * 0.9
           
           print(result)
           
      elif currency_2 in ["z", "zloty", "zlo"]:
          
          zloty = float(input("Enter how much zloty do you want to convert"))
          
          result = zloty * 3.88
          
          print(result)
                     
                     