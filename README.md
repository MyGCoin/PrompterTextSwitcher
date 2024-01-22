# PrompterTextSwitcher
Switching Elgato Prompter Text for Camera Hub

This Python code was created to give you an idea how you could code your own Switcher
for the Elgato Prompter. I created this for my own usage, so use and modify this at
your own risk and don't forget to change the path to your textfiles and "Camera Hub.exe".

This code will:

1. exit Camera Hub.exe
2. ask you which of your text-files you want to load into "AppSettings.json"
   at position "applogic.prompter.source.text":
3. It will replace existing text you did enter within the Prompter (for all sections).
   So make sure you got a backup of it ("AppSettings.json"), just in case.
4. Replacement will we taken from text1.txt to text10.txt, which you chose by entering the number (1-10)
5. Camera Hub.exe will be started again
6. Prompter should now show your new text from the textfile.
   Each Line in your textfile represents one section. Empty lines create empty sections

Have fun and create something great for you or the people out there.
If you like, check out my crypto project at https://www.mygcoin.com

Stay awesome! And please give me credits if using this idea :)
