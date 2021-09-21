# Project Name:
# ‘Ami Coding Pari Na’

#How to install in your machine
1. Frist of all download source code using git commend
2. Then install requirements.txt file using ”pip3 install requirements.txt”
3. Then run ”python3  manage.py makemigrations myapp”
4. Then run ”python3 manage.py migrate”
5. Finally run  ”python3 manage.py runserver”

# Project Description:
You have to develop a web application. Your project will contain 3 sections.

#Section 1: User Authentication/Registration Page
A user login and registration section. You can use whatever input fields you want (maintaining a standard)

#Section 2: Khoj the search Page
After login, users can access this page. 
 Khoj the search: In this segment(page), there will be two input fields
Input Values: User can input comma separated integers
Search Value: User can input only one integer 
Output: Will print True if the search value is in the input values. Otherwise print False



Now, before showing the output, you have to store the input values in the database in sorted order(descending) along with the logged in user id and the input timestamp. That means, when the user press the button “Khoj”, the Input values (9, 1, 5, 7, 10, 11, 0) will be stored in the database as follows : 11, 10, 9, 7, 5, 1, 0 

So the rough workflow for this section is as follows 

Take the “Input Values”
Take the “Search Value”
Sort the “Input values” in descending order.
Store the sorted “Input Values” in the database.
Check if the “Search Value” is in the “Input Values”
Print the output

Note: The above workflow might not be the optimal workflow. You can change your workflow as you need to make it more optimized.

#Section 3: API Endpoints
In this section, there will be only one API endpoints

Endpoint 1: Get All Input Values

Parameters: start_datetime, end_datetime, user_id

Returns: All the Input Values the user ever entered within start_datetime(inclusive) and end_datetime (inclusive). Check the following response format.

```bash
{
    “status”: “succes”,
    “user_id” : 1,
    “payload” : [
         {
              “timestamp” : ”2012-01-01 00:00:00”,
              “input_values” : “11, 10, 9, 7, 5, 1, 0”
          },
         {
                “timestamp” : ”2013-01-01 01:00:00”,
                 “input_values” : “13, 11, 10, 7, 5, 2, 1”
          
       ]
}

```



