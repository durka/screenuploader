screenuploader
==============

This is a dead-simple screenshot uploader for Mac OS X.
It depends on [terminal-notifier](https://github.com/alloy/terminal-notifier) for notifications.

Overview
========
Screenuploader works with the [regular keyboard shortcuts](http://fortysevenmedia.com/blog/archives/quick_screenshot_key_commands_in_mac_os_x/) for taking screenshots. Whenever a file appears on the desktop, the screenuploader script is run (via a LaunchAgent) and it looks for a screenshot image created within the last minute. A notification is displayed, and if you click the notification, the image is removed from the desktop and uploaded to your server (see below). Another notification is displayed when the upload completes, and the direct URL to the image is copied to the clipboard.

Setup
=====
0. Install dependencies:
    brew install terminal-notifier
   (You can install it some other way, but it has to be at `/usr/local/bin/terminal-notifier`.
1. Copy `config.py.example` to `config.py` and read the comments therein to set up your configuration.
2. Run `install.py`. If it completes successfully it will say "Finished!" at the end.
3. Take a screenshot and make sure everything works.

