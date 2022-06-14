# Learn Python Programming – Second Edition

<a href="https://www.packtpub.com/application-development/learn-python-programming-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781788996662 "><img src="https://d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/ppv4_main_book_cover/B10074_New1cover.png" alt="Learn Python Programming - Second Edition" height="256px" align="right"></a>

This is the code repository for [Learn Python Programming - Second Edition](https://www.packtpub.com/application-development/learn-python-programming-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781788996662), published by Packt.

**Build a solid foundation in coding by utilizing the language and its core characteristics**

## What is this book about?
Learn Python Programming creates a foundation for those who are interested in developing their skills in Python programming. The book starts with the fundamentals of programming with Python and ends by exploring different topics such as GUIs and real-world apps.

This book covers the following exciting features:
* Get Python up and running on Windows, Mac, and Linux 
* Grasp fundamental concepts of coding using data structures and control flow 
* Write elegant, reusable, and efficient code in any situation 
* Understand when to use the functional or object-oriented programming (OOP) approach 
* Walk through the basics of security and concurrent/asynchronous programming 

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1788996666) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter01.

**Setup**


Create a virtual environment with a Python version 3.7.*.


**Installing requirements**

Install all the requirements text files via pip like this:

    $ pip install -r requirements.txt

Requirements for the data science chapter can be cumbersome to install
so I kept them separated, in the `requirements.data.science.txt` file.

If you wish to install all requirements at once, just execute the following:

    $ pip install -r all.txt


**Updating requirements**

To update requirements you can use `pip-tools` to compile the `*.in`
sources in the `requirements` folder.

To compile and update a single `.in` file, run the following:

    $ pip-compile -U requirements.in

If you want to compile all requirements into one single `.txt` file,
run the following:

    $ pip-compile -U -o all.txt *.in

This will read all the `.in` files and compile them together into the
`all.txt` file.

The sample code will look like the following:
```
# we define a function, called local
def local():
    m = 7
    print(m)
```

**Following is what you need for this book:**
Learn Python Programming is for individuals with relatively little experience in coding or Python. It's also ideal for aspiring programmers who need to write scripts or programs to accomplish tasks. The book takes you all the way to creating a full-fledged application.

With the following software and hardware list you can run all code files present in the book (Chapter 1-14).
### Software and Hardware List
| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1-14        | Python 3.7                     | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it]().

### Related products
* Secret Recipes of the Python Ninja [[Packt]](https://www.packtpub.com/application-development/secret-recipes-python-ninja?utm_source=github&utm_medium=repository&utm_campaign=9781788294874) [[Amazon]](https://www.amazon.com/dp/1788294874)

* C++ High Performance [[Packt]](https://www.packtpub.com/application-development/python-programming-blueprints?utm_source=github&utm_medium=repository&utm_campaign=9781787120952) [[Amazon]](https://www.amazon.com/dp/1786468166)

## Get to Know the Author
**Fabrizio Romano**
Fabrizio Romano was born in Italy in 1975. He holds a master's degree in computer science engineering from the University of Padova. He is also a certified scrum master, Reiki master and teacher, and a member of CNHC.

He moved to London in 2011 to work for companies such as Glasses Direct, TBG/Sprinklr, and student.com. He now works at Sohonet as a Principal Engineer/Team Lead.

He has given talks on Teaching Python and TDD at two editions of EuroPython, and at Skillsmatter and ProgSCon, in London.

## Other book by the author
[ Learning Python](https://www.packtpub.com/application-development/learning-python?utm_source=github&utm_medium=repository&utm_campaign=9781783551712 )

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.
