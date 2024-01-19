# 0. Run booking evaluation slots program  

python3 eval_booker**.py  

# Automatically booking evaluation slots  

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
(error002) fixed: installing selenium if there is no "selenium" library  

@mschaub - inception  
working  
(error003) when you force to close chrome page, error occurs.  
(error003) not fixed : not critical error. let's see.  

@dwilke - minishell  
not working  
(error004) Some project's name has + "42cursus-"  
(error004) fixed : fixed project_name_mapping  


<19/Jan>  
(error005) - random host number was 65536  
(error005) fixed ? : host number is going to be 65536 to 65999  

@
(error001 - 2nd) I should check if evaluation slot is booked

