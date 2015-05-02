Project Tournament Results
=============

This code is the result I achieved for ***[Udacity Full Stack Developer
Nanodegree](https://www.udacity.com/course/nd004) - Project 2: Tournament
Results***.
Instructions on how to run the application can be found at the bottom of
this README text.

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

## Origin and Modifications
This code is based on the [repository provided by Udacity](https://github.com/udacity/fullstack-nanodegree-vm)
with common code for the Relational Databases and Full Stack Fundamentals
courses.
There are several things I've added or modified:

1. Table definitions have been implemented, and views have been used to
   make database queries more concise.
   *Note: Although the database is already prepared to support multiple
   tournaments, it hasn't been implemented in the Python code yet.*
2. Setup of the database has been added to the script ```pg_config.sh```
   to let Vagrant automatically do it when creating the virtual
   environment.
3. Tests have been added for interaction with the tournaments-table in
   the database.
4. Ordering of player standings is implemented in a view at
   database-level, according to OMW (Opponent Match Wins), and a test
   has been added to make sure the ordering is right.
5. Connection with the database is done in a method with error-handling.
6. Generic methods have been added for ```SELECT COUNT(*)...``` and
   ```DELETE FROM...``` queries, to simply wrap them in a one-liner and
   reduce repeated code blocks with similar code (DRY).
7. Method has been added to bulk register players, to repeat less code
   in the tests where players have to be added.
8. And more...

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
