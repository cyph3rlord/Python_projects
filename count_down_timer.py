import time

my_time = int(input("Enter the time in seconds: "))

paused = False

while my_time > 0:
    if not paused:
        seconds = my_time % 60
        minutes = int(my_time / 60) % 60
        hours = int(my_time / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        
        time.sleep(1)
        my_time -= 1
print('TIME\'S UP')  
        
 # user_input = input("Enter 'p' to pause and 'r' to resume Enter to continue").lower()
#    if user_input == 'p':
       
     #  paused = True
  #     print('Timer paused')
 #   else:
#       paused = False
       #print('Timer resumed')
             
        