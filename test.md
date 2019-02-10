<link rel="stylesheet" type="text/css" href="./codehilite.css">

#Code blocks must be indented by 4 whitespaces.
Python-Markdown has a auto-guess function which works
pretty well:

    print("Hello, World")
    # some comment
    for letter in "this is a test":
        print(letter)

In cases where Python-Markdown has problems figuring out which
programming language we use, we can also add the language-tag
explicitly. One way to do this would be:


    :::python
    print("Hello, World")

or we can highlight certain lines to
draw the reader's attention:


    :::python hl_lines="1 5"
    print("highlight me!")
    # but not me!
    for letter in "this is a test":
    print(letter)
    # I want to be highlighted, too!



#A brief test to convert the required markdown elements into HTML.

#This is my first header.
##This is my second header.
###This is my third header.
####This is my fourth header.
#####This is my fifth header.
######This is my sixth header.

#Converting Bold and Italics from Markdown into HTML.

It's **very** easy to do **bold** and *italics*.

It's __very__ easy to do __bold__ and _italics_

#Now we will convert a link written in Markdown into HTML.
[Github](https://pages.github.com/)

#We will convert an unordered list written in Markdown into HTML.

* Bullet 1

* Bullet 2

* Bullet 3

#We will convert an ordered list written in Markdown into HTML.
**This is the Chelsea Football Club squad:**

2. Eden Hazard
1. Gonzalo Higuain
3. Willian

#Converting a quote written in Markdown into HTML.
In the word of Sir Albert Einstein:

> Every action has an equal and opposite reaction.


#Inserting an image in Markdown which is converted into HTML.
![insertion](ok.PNG)

#Converting the sentence into bold and italic:
**This text is _extremely_ important**


#Converting nested lists:

1. First item:
    - First nested list item.
      - Second nested list item.






