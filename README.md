# Google_ChatGPT_Terminal_Search
PLease Read Comments and make sure you understand the code before utilizing.

Basic functions:
- Takes input from terminal or cmd and opens webpage based on input
- typing in "chat" will open up chat_gpt through bing.com
- use the website filter list to add websites to your web filter

example execution within VSC: 
python main.py chat (result will open bing.com chat bot)
python main.py how to reverse a linked list (results will open google search with filtered sites based off preference)
python main.py (will return error message since nothing was entered)

Finally!
To fully omptimize this project you will need to setup an alias with a .bat script that points to the file location using Doskey.
You can make a DOSKEY macro permanent by creating a macro definition file and adding it to the Autorun registry key for the Command Processor. 
Here’s how you can do it:
Create a macro definition file: Open a text editor and type your DOSKEY macros in the following format: macroname=command. For example, if you want to create a DOSKEY macro for the ipconfig command called ip, you would type doskey ip=ipconfig. Save this file with any name you like (e.g., macros.txt) in a location of your choice.

Add the macro definition file to the Autorun registry key: Open the Registry Editor by pressing the Windows key + R, typing regedit, and pressing Enter. Navigate to the following key: HKEY_CURRENT_USER\Software\Microsoft\Command Processor. Right-click on the right pane and select New > String Value. Name the new value Autorun. Double-click on the new value and set its data to doskey /macrofile="<path to your macro definition file>", replacing <path to your macro definition file> with the actual path to your macro definition file.

After completing these steps, your DOSKEY macros will be automatically loaded every time you open a new Command Prompt window1.
