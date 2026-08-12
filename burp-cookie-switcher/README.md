# Burp Cookie Switcher

A lightweight Burp Suite extension for quickly switching between different authentication cookies while manually testing Broken Access Control (BAC).

## Why I Created This

Authorization-testing extensions can produce a lot of false positives and may not work properly with endpoints such as **edit** and **delete** requests.

Manually testing BAC can also become boring and time-consuming when you have to repeatedly replace authentication tokens or cookies.

So I created this extension to make manual BAC testing faster and easier.

## How It Works

The extension lets you save two authentication cookies:

- **Admin cookie**
- **User cookie**

You can then quickly switch between them directly from Burp Repeater.

Instead of manually replacing the cookie every time, you can simply switch the authentication context with a right-click.

## Setup

1. Open **Burp Suite**.
2. Go to **Extensions**.
3. Add the Python extension `cookie_switcher.py`.
4. Open the **Cookie Switcher** tab.
5. Add your **Admin cookie**.
6. Add your **User cookie**.
7. Send a request to **Repeater**.

## Usage

In Burp Repeater:

1. Right-click the request.
2. Select **Extensions → Cookie Switcher**.
3. Choose:
   - **Switch to User Cookie**
   - **Switch to Admin Cookie**

The extension replaces the authentication cookie so you can test the same request with different privilege levels without manually changing the cookie each time.