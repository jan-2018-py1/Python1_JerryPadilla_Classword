Gets a bug when processing login info when session['email'], session['password'] 
don't have anything stored through "process_register". Meaning if you clear the 
session then try and login, it bugs out because recog session yet. If nothing is 
in session for the first login attempt then it bugs out on the 'email' validation 
because there is no session['email'] yet