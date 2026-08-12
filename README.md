~ Burp Cookie Switcher:
A lightweight Burp Suite extension for quickly switching between different authentication cookies while manually testing Broken Access Control (BAC).

~ Why I Created This:
Authorization-testing extensions can produce a lot of false positives and may not work properly with endpoints such as edit and delete requests.

Manually testing BAC can also become boring and time-consuming when you have to repeatedly replace authentication tokens or cookies, So I created this extension to make manual BAC testing faster and easier.

~ How It Works:
The extension lets you save two authentication cookies:

Admin cookie
User cookie

You can then quickly switch between them directly from Burp Repeater.

Instead of manually replacing the cookie every time, you can simply switch the authentication context with a right-click.

~ Setup:
Open Burp Suite.
Go to Extensions.
Add the Python extension cookie_switcher.py.
Open the Cookie Switcher tab.
Add your Admin cookie.
Add your User cookie.
Send a request to Repeater.
Usage

In Burp Repeater:

Right-click the request.
Select Extensions → Cookie Switcher.
Choose:
Switch to User Cookie
Switch to Admin Cookie

The extension replaces the authentication cookie so you can test the same request with different privilege levels without manually changing the cookie each time.
