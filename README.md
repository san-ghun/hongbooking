# Automatically booking evaluation slots program

At 42, students are required to schedule evaluation slots for their projects. 
Occasionally, due to high demand, available slots may become scarce, 
prompting students to patiently await their availability 
or continuously refresh the page.

I have developed an automated code solution 
to streamline the process by reserving evaluation slots 
as soon as they become accessible.

download selenium if do not have type in your terminal

pip install selenium

# 1. Go to your evaluation page where you can book evaluation slots 
copy URL of last team_id which is xxxxxxx as below

example 
https://projects.intra.42.fr/projects/cpp-module-09/slots?team_id=1234567

and replace team_id number in my code
let me know there is better ID

#everyone has different team_id

team_id = "xxxxxxx"  # Replace with the actual team ID


# 2. Comment out "nextok.click()"
if you believe me try it. 

I have not tried yet.

#nextok.click()


# 3. Run the program in terminal type below 
Use last version example now it is eval_booker11.py

python3 eval_booker*.py



I wanted to make auto macro to book evaluation slots.

because I do not want to spend time to click F5 several times.


