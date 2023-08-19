def add_time(start, duration):
    global period
    hour=int(start.split(":")[0])
    minutes=int(start.split(":")[1].split()[0])
    d_hour=int(duration.split(":")[0])
    d_minutes=int(duration.split(":")[1])
    period=start.split(":")[1].split()[1]
    t_hour=hour+d_hour
    t_minutes=minutes+d_minutes
  
    def period_toggle(Count=0):
      global period
      if period == "PM" and Count==0:
           period="AM (next day)"
      elif period =="AM" or period=="AM (next day)" and Count==0:
           period="PM"
      elif period =="AM" or period=="AM (next day)" and Count!=0:
           period="PM, ("+str(round(Count/2))+" days later)"
      else:
           period="AM ("+str(Count)+" days later)"
     
        
    if t_hour<=12 and t_minutes<60:
       new_hour=t_hour
       new_minutes=t_minutes
       if t_hour==12:
          period_toggle()
         
    elif t_hour>12 and t_minutes>=60:
       new_hour=t_hour+1
       new_minutes=t_minutes -60
       count=0
       while(new_hour>12):
         new_hour= new_hour-12
         count=count+1
         period_toggle()
       if count>=2:
         period_toggle(count)
    
      
    elif t_hour>12 and t_minutes<60:
       new_hour=t_hour
       new_minutes=t_minutes
       count=0
       while(new_hour>12):
         new_hour= new_hour-12 
         count=count+1
         period_toggle()
       if count>2:
         period_toggle(count)
    
    elif t_hour<12 and t_minutes>=60:
       new_hour= t_hour+1
       new_minutes=t_minutes-60
       if new_hour==12:
          period_toggle()  
         
    new_time= str(new_hour)+":"+str(new_minutes).rjust(2, '0')+" "+period
    return new_time

print(add_time("11:06 PM", "2:02"))
