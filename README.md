# EveryAction


How long, roughly, did you spend working on this project?
    - About one hour

Give the steps needed to deploy and run your code, written so that someone else can follow and execute them.
    - Run pip3 install -r requirements.txt
    - Run python3 solution.py

What could you do to improve your code for this project if you had more time? 
    - I would include error handling for certain cases including empty results or error responses
    - I could add support for the $top parameter

Outline a testing plan for this report, imagining that you are handing it off to someone else to test. What did you do to test this as you developed it?
    - Test fetchemailBatch responses from failed/incorrect and correct credentials
    - Test printResults for handling non-empty and empty responses
    - Test getEmails for handling cases containing null and non-null 'nextPageLink' values
