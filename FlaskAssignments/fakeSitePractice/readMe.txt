Fake registering and login site because I was bored at work. Figured I would just
add it here because it's practice. Using session as a fake "database".

Gets a bug when processing login info when session['email'], session['password'] 
don't have anything stored through "process_register". Meaning if you clear the 
session then try and login, it bugs out because recog session yet. If nothing is 
in session for the first login attempt then it bugs out on the 'email' validation 
because there is no session['email'] yet.

Lastly, there is no email verification with the Regex because I didn't get around 
to adding that. lol.
