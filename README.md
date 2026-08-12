# Burp Cookie Switcher

A lightweight Burp Suite extension for quickly switching between **Admin and User cookies** while manually testing **Broken Access Control (BAC)**.

## Why I Created This

* Authorization-testing extensions can produce false positives.
* Some do not work properly with endpoints like **Edit** and **Delete**.
* Manually replacing authentication cookies repeatedly is slow and boring.
* This extension makes manual BAC testing faster and easier.

## How It Works

* Save your **Admin cookie**.
* Save your **User cookie**.
* Send a request to **Burp Repeater**.
* Right-click the request.
* Select **Extensions → Cookie Switcher**.
* Choose:

  * **Switch to Admin Cookie**
  * **Switch to User Cookie**

The extension replaces the authentication cookie automatically, letting you test the same request with different privilege levels without manually changing the cookie every time.

## Setup

* Open **Burp Suite → Extensions**.
* Add `cookie_switcher.py`.
* Open the **Cookie Switcher** tab.
* Add your Admin and User cookies.
* Start testing.
