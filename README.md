This party is NOT  over. Added captcha support (basically pulled changes from the main repo). Now you will hear a beep and then a captcha will popup like this:
Note: The captcha is a bit buggy and I had to make 5-6 tries before I was able to book.

![image](https://user-images.githubusercontent.com/83712877/117570457-cc82f300-b0e7-11eb-80a5-cd425afe4be9.png)


# Bombardier fully automated COVID-19 Vaccination Slot Booking Script
This is a fork over the neat https://github.com/pallupz/covid-vaccine-booking Thanks for creating a playground for me to build on.

What this repository does:
1. Automates OTP read from the SMS (Android only) after the token expires
2. Randomly chooses one of the available slots instea of waiting for input from the user
3. Reduces the polling wait to optimize on the polling frequency (hence the name bombardier)
![image](https://user-images.githubusercontent.com/83712877/117467267-290fd200-af71-11eb-8461-d6e253c183d7.png)


How it works:
1. https://ifttt.com/ is used to create a SMS trigger. The trigger happens when the OTP SMS is received
2. The trigger sends the text of the SMS to a REST service, I have used a free service which needs 0 setup for a shared storage


**Parallely**
1. The script runs continuously to poll (same logic as the original repository)
2. Whenever th OTP expires, an OTP is requested
3. When the OTP SMS is received on the Android, phone, the above logic triggers to store the OTP SMS in the shared storage
4. The script polls the shared storage to get the OTP
5. Once the OTP is received, the polling resumes
6. If a free slot is found, rather than waiting for an input, it randomly chooses a slot and attempts to book


**Steps to setup**
1. Create an account in ifttt.com (A premium paid account is recommended for a quicker response)
2.     Create a new applet
3.     If this..... click on Android SMS trigger
4.     Select "New SMS received matches search" and use CoWIN as the search key
5.     Then... Choose a service named Webhooks and then select make a web request
6.         Paste the url:  https://kvdb.io/AuNXJueossuYv4pTq1Fdtx/99XXXXXXXX replace 99XXXXXXXX with your phone number
7.         Method is PUT
8.         Content Type PlainText
9.        Body: Add ingredient and select Text
10. On your android phone, install ifttt app
11.     Login 
12.     Ensure that the battery saver mode, and all other optimizations are removed. The appshould always run (This is the key for quick response). 
	Tip: If your IFTTT is not triggered when your SMS is received: https://www.androidpolice.com/2020/05/30/how-to-prevent-apps-sleeping-in-the-background-on-android/
	Also a premium account is faster
13. Clone this repository
14. On mac I had to do the following too
15. 	brew install python-tk
16. 	brew install SoX
17. Run the script, use the steps given below to enter your preferences
18. Hopefully you get the slot
19. Stay healthy and stay safe!

Tips: I used this command to run the script as it was giving me Syntax error:_ python3 src/covid-vaccine-slot-booking.py_
Also I used this command to install the dependencies _python3 -m pip install -r requirements.txt_


**Same steps in screenshots:**
![image](https://user-images.githubusercontent.com/83712877/117159172-b0c4d780-addd-11eb-90f0-ab8438db4c8e.png)
![image](https://user-images.githubusercontent.com/83712877/117159291-c76b2e80-addd-11eb-991a-dc6de4bbb620.png)
![image](https://user-images.githubusercontent.com/83712877/117159444-e669c080-addd-11eb-9b4c-448335b1c781.png)
![image](https://user-images.githubusercontent.com/83712877/117159516-f8e3fa00-addd-11eb-832d-fcf92238f823.png)
![image](https://user-images.githubusercontent.com/83712877/117159663-17e28c00-adde-11eb-9a5f-4faf39430279.png)
![image](https://user-images.githubusercontent.com/83712877/117159753-2c268900-adde-11eb-9bb3-4bb54f951683.png)
![image](https://user-images.githubusercontent.com/83712877/117159818-38aae180-adde-11eb-96b5-0e779803b4b2.png)
![image](https://user-images.githubusercontent.com/83712877/117159863-4496a380-adde-11eb-8874-40cc6f851cf6.png)
![image](https://user-images.githubusercontent.com/83712877/117325821-b5a58c00-aeae-11eb-8156-2ea585a77834.png)



# COVID-19 Vaccination Slot Booking Script
## Update:
### **We are getting all kinds of attention now - which I do not want to handle. So there won't be any additional commits to this project. It has been put on indefinite hold.**



### Important: 
- This is a proof of concept project. I do NOT endorse or condone, in any shape or form, automating any monitoring/booking tasks. **Use at your own risk.**
- This CANNOT book slots automatically. It doesn't skip any of the steps that a normal user would have to take on the official portal. You will still have to enter the OTP and Captcha.
- Do NOT use unless all the beneficiaries selected are supposed to get the same vaccine and dose. 
- There is no option to register new mobile or add beneficiaries. This can be used only after beneficiary has been added through the official app/site.
- API Details (read the first paragraph at least): https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2
- BMC Link: https://www.buymeacoffee.com/pallupz
- And finally, I know code quality isn't great. Suggestions are welcome.

### Noteworthy Forks
- https://github.com/bombardier-gif/covid-vaccine-booking : I haven't tried this personally but, it looks like a promising, completely automated solution that would require a bit more setting up.

### Usage:

For the anyone not familiar with Python and using Windows, using the ```covid-vaccine-slot-booking.exe``` executable file (EDIT: EXE is not working at the moment due to unresolved errors) would be the easiest way. It might trigger an anti-virus alert. That's because I used ```pyinstaller``` to package the python code and it needs a bit more effort to avoid such alerts.

OR

Use **Python 3.7** and install all the dependencies with:
```
pip install -r requirements.txt
```
Then, run the script file as show below:
```
python src\covid-vaccine-slot-booking.py
```
If you're on Linux, install the beep package before running the Python script. To install beep, run:
```
sudo apt-get install beep
```
If you already have a bearer token, you can also use:
```
python src\covid-vaccine-slot-booking.py --token=YOUR-TOKEN-HERE
```

### Third-Party Package Dependency:
- ```tabulate``` : For displaying data in tabular format.
- ```requests``` : For making GET and POST requests to the API.
- ```inputimeout``` : For creating an input with timeout.
