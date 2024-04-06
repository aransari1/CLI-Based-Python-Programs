Minutes_List = []
Seconds_List = []

#Function for Spliting the Time in Minutes and Seconds for better calculation
def Time_Sorter(Input_Time):
    minutes, seconds = map(int, Input_Time.split('.'))
    if float(seconds) <= 6.0:
        Minutes = (minutes)
        Seconds = (int(seconds))
    else: print ("Please Enter Seconds <= 60: ")
    
    return Minutes,Seconds
        
        
          
def Time_Calculate(Minutes_List,Seconds_List):
    
    Total_Minutes, Total_Seconds = 0,0
    for Time in Seconds_List:
        print(Time)
        Total_Seconds = (Total_Seconds + Time)
        
    for Time in Minutes_List:
        Total_Minutes = (Total_Minutes + Time)
        
    Seconds_to_Minute_Conversion(Total_Minutes,Total_Seconds)
    return print(f"Total Time is {Total_Minutes}:{Total_Seconds}")


def Seconds_to_Minute_Conversion(Total_Minutes,Total_Seconds):
    Total_Minutes = Total_Minutes + (Total_Seconds//60)
    Total_Seconds = Total_Seconds-((Total_Seconds//60)*60)
    return Total_Minutes, Total_Seconds

while True:
     Input_Time = input("Enter the Time:    ")
     Minutes, Seconds = Time_Sorter(Input_Time)
     Minutes_List.append (Minutes)
     Seconds_List.append (Seconds)
     Choice = input("To Quit enter: 'Q' : ")
     if Choice == ("q" or "Q"):
         Time_Calculate(Minutes_List,Seconds_List)
         break
     else:
        continue