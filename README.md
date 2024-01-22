# PrompterTextSwitcher
Switching Elgato Prompter Text for Camera Hub

This Python code was created to give you an idea how you could code your own Switcher
for the Elgato Prompter. I created this for my own usage, so use and modify this at
your own risk and don't forget to change the path to your textfiles and "Camera Hub.exe".

<b>This code will:</b>

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


<b>Disclaimer for Provided Code</b>

Please be aware that the code provided is for demonstration and educational purposes only and should be considered as a proof of concept. I do not assume any responsibility for the functionality, error-free operation, or any consequences arising from the use of this code. Use of the code is at your own risk.

It is recommended to test and evaluate the code in a safe and controlled environment before deploying it in a production setting or for critical applications. I will not be liable for any direct or indirect damages that may result from the use of the code, including but not limited to operational disruptions, data loss, or system failures.

This code is not intended for use in situations where errors or inaccuracies could lead to harm to individuals, property, or the environment. Each user is responsible for complying with relevant laws, regulations, and best practices.
