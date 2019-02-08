# Welcome to the free Markdown-HTML convertor.
 
 This little convertor, will help you to convert all your markdown written files into pure HTML and will generate a website where you can see the final result.(Your file written in markdown)
 
 Anyone can simply build a simple convertor like I did.
 First of all you need to download 2 packages from the Python Community in order to start creating your Markdown-HTML conversion tool:
 - Install Markdown
 - Install Pygments.
 
 **You can get both of them using the (PIP) command or you can just download it in your Pycharm or Visual Studio Code.**
 
 ## What does the markdown package do?
 The markdown package is a great package for converting each and every single document written in markdown zhich will be later generated as HTML.
 
 ## What does the pygment package do?
 The pygment package will allow you to insert some CSS into your final markdown file which will then be generated as HTML and it also use for syntax highlighting
 
 You can create your markdown file online for free *[here](https://stackedit.io)*
 Once you have created your markdown file you just have to download it and it is ready to be used.
 
 ## Let's dig deep into the coding part and algorithm now.
 Now that you already have Markdown and Pygments installed, we are ready to go.
 
**Let's do this step by step.**

1) Import markdown.
- We need to import markdown because Python-Markdown provides an API for third parties to write extensions to the parser adding their own additions or changes to the syntax. ... Strings should only be used when it is impossible to import the Extension Class directly (from the command line or in a template).

2) Import OS.
- The OS module in Python provides a way of using operating system dependent functionality. The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux.

3) Import subprocess.
- The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions. The method is defined as: subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False) # Run command with arguments and return its output as a byte string. **Example usage: #!/usr/bin/env python import subprocess s = subprocess.**

__NOTE: IF YOU DO NOT HAVE THE MODULES MENTIONNED ABOVE MAKE SURE YOU DOWNLOAD IT ON YOUR PYCHARM OR VISUAL STUDIO CODE AND THEN CONTINUE TO FOLLOW THE STEPS__

4) Let's give our program a good look while it will execute and also try to guide our users what they will have to do once the conversion tool is launched. Let's do this with some `PRINT`.

- print('----------Welcome to the Markdown-HTML convertor----------')
- print('***********************************')
- print('1 - Conversion Tool') [this is a choice that the user needs to do. We must make sure that when he/she presses `1` the conversion tool should be lauched.]
- print('2 - Install other packages (make use of <PIP>)') [this is a choice that the user needs to do. We must make sure that when he/she presses 2, the necessary packages are installed.]
- print('Press 1 to use the conversion tool freely')
- print('Press 2 if you want to download other packages.')
- choice = int(input()) [this is the command that will take into consideration the choices made by the user]
  
5) Now let's call the loop depending on whether the user presser the 1 or 2.

- if choice == 1:
    fichier = input("Please kindly insert the markdown file to be converted (markdown.md) : ")
    os.system("python -m markdown -x codehilite " + file_to_be_converted + " > index.html")
    __NOTE: the command *python -m markdown* is used to convert the markdown file into html and if you want the CSS to be applied then you need to use the full command *python -m markdown -x codehilite + "file_to_be_converted +" > index.html*. Remember that the '+' sign is used for concatenation of strings.__
    *Now if the user chooses 1 and the choice is exactly equal to 1 then the user will be able to use the Markdwon-HTML tool.*
    
- elif choice == 2:
    os.system("pip install markdown")
    
    *Now if the user presses 2 and the choice is exactly equal to 2 then the markdown package will automatically start to download.*
    
6) And that's the final step.

- Run the program using the F5 key if you are using Visual Studio Code. The index.html file will be generated in your Desktop. Make sure to open it and savour the success of your hardwork.

**That's it, you are ready to use your free _Markdown-HTML Convertor_**
    
    


 
 
