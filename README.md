Project Tournament Results
=============

This code is the result I achieved for ***[Udacity Full Stack Developer Nanodegree](https://www.udacity.com/course/nd004) - Project 2: Tournament Results***.
Instructions on how to run the application can be found at the bottom of this README text.

This code has been *reviewed by me*. According to me, based on the rubric
used by the Udacity reviewer, this code at least:
- [x] Exceeds Specifications: The module passes the unit tests; and
  separately, one or more of the extra credit options are implemented.
- [x] Exceeds Specifications: Tables have meaningful names and there are
  no unnecessary tables defined. In addition, views are used to make
  queries more concise.
- [x] Exceeds Specifications: Table columns have meaningful names, are of
  the proper data type and there are no unnecessary columns defined. In
  addition, primary and foreign keys are correctly specified.
- [x] Exceeds Specifications: Code is ready for personal review, is
  neatly formatted and makes use of query parameters appropriately. All
  sorting and aggregation are performed in the database.
- [x] Meets Specifications: Comments are present and effectively explain
  longer code procedures.
- [x] Meets Specifications: A README file is included detailing all
  steps required to successfully run the application.

A list of websites, books, forums, blog posts, Github repositories etcetera
that I have referred to or used in this submission can be found in the
[references.txt](https://github.com/swesterveld/udacity-nd004-p2-tournament-results/blob/master/references.txt)
file.

## Run the application
1. Make sure Git, Vagrant and VirtualBox have been installed on your computer
2. Make sure your computer is connected to the internet
3. Clone this repository to a directory on your computer
4. Change directory to the ```vagrant``` directory in the repository
5. Issue ```vagrant up``` to start the virtual environment and let
   vagrant prepare the database for this project.
6. Issue ```vagrant ssh``` to login to the virtual environment
7. You're in the virtual environment now. Finally, to run the tests,
   issue: ```python /vagrant/tournament/tournament_test.py```
