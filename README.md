# 0. Run booking evaluation slots program

python3 eval_booker**.py

You can also do coding or web surf while the program is running

# Automatically booking evaluation slots program

At 42, students are required to schedule evaluation slots for their projects. 
Occasionally, due to high demand, available slots may become scarce, 
prompting students to patiently await their availability 
or continuously refresh the page.

I have developed an automated code solution 
to streamline the process by reserving evaluation slots 
as soon as they become accessible.




# Test result

<17/Jan>
@rtimsina - cpp  
not working  
(error001) time delay between click button is shown and actually click button  
(error001) fixed: change time delay 5 sec to 1 sec to click icon  

<18/Jan>
@ttaneski - cpp
working
(error002) I want to do everything with my code even installing "selenium" library
(error002) fixed: selenium if there is no "selenium" library

@mschaub - inception
working
(error003) when you close chrome page, below error is shown. 
(error003) not fixed : not critical error so let'see.

An unexpected error occurred: Message: no such window: target window already closed
from unknown error: web view not found
  (Session info: chrome=120.0.6099.109)
Stacktrace:
#0 0x55800fdd2f83 <unknown>
#1 0x55800fa8bcf7 <unknown>
#2 0x55800fa5f728 <unknown>
#3 0x55800fb0c69f <unknown>
#4 0x55800fb23719 <unknown>
#5 0x55800fb04e53 <unknown>
#6 0x55800faccdd4 <unknown>
#7 0x55800face1de <unknown>
#8 0x55800fd97531 <unknown>
#9 0x55800fd9b455 <unknown>
#10 0x55800fd83f55 <unknown>
#11 0x55800fd9c0ef <unknown>
#12 0x55800fd6799f <unknown>
#13 0x55800fdc0008 <unknown>
#14 0x55800fdc01d7 <unknown>
#15 0x55800fdd2124 <unknown>
#16 0x7f5adf8edac3 <unknown>

@dwilke - minishell
not working
(error004) Some project's name has + "42cursus-"
(error004) fixed : fixed project_name_mapping


<19/Jan>
(error005) - random host number was 65536
(error005) fixed ? : host number is going to be 65536 to 65999

