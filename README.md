# udacity_fullstack_02

## Dependencies
The script requires that your system has PostegreSQL installed,
to check if you have PostegreSQl installed, run the follwing command
in your terminal:
    >psql
If you successfully entered the PostegreSQL command line prompt, proceed
to the setting up of database, otherwise, run the follwing command
    >pip install psycopg2
Use root user access if necessary
    > sudo pip install psycopg2



## Setting up database
To set up the database, enter the PostegreSQL command line prompt
    >psql

Load the "tournament.sql" file by running:
    >\i tournament.sql

This script will create a database named "tournament", use that database,
and create a table named "players".

Note: if you already have a tournament database or table "players" created, the script
will skip creating database and execute the following command.


## Running the "tournament.py" script
In the regular command line window, run the following command:
    $ python tournament.py


## Testing
To run unit tests against the "tournament.py" script, in the regular command
line window, run the following command
    $ python tournament_test.py

