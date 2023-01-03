# Installing Postgres and CREATING the Database

It's easiest to do this by [creating a new conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) (which can then be used to run the SQL jupyter notebooks as well), as follows: 

Create a conda environment using the following commands **(in Terminal for Mac users or Anaconda Prompt for Windows users):** 

    conda create --name bmi535-db

    conda activate bmi535-db

    conda install -c conda-forge psycopg2 ipython-sql postgresql pgspecial

Install the jupyter kernel so you can run notebooks from this environment: 

    conda install ipykernel

Then, also in your Anaconda Prompt (on Windows) or your Terminal (on Mac) run the following:

## For Windows users

You can also set the `PGDATA` environment variable using the control panel. 

Make sure to sub your `USERNAME` on your machine here. If your windows user name has a space use quotes, e.g. `createdb "John Doe"`

```
#set the database location
#add PGDATA to your environment variables either with the following statement
#or use control panel to add it (it can be user or global)
setx PGDATA C:\Anaconda\pgdata

```
**Note: you may need to re-start Anaconda Prompt after setting the environment variable. Ensure the conda environment you created above is activated in the new prompt. 

**Note: the `createdb` command below will create a user database with the current username, remember this because you'll need to use the same username to connect to any database in the future.

```
#make the database directory
mkdir %PGDATA%
# initialize the database in the PGDATA Folder
pg_ctl initdb
# start the postgres daemon (process that runs in background)
pg_ctl start
# create a user database (by default the database name is the current username)
createdb
# open the prompt so we can add another database
psql
```

## For Mac users

```
#set the database location
#add this line to your .bash_profile or .profile
export PGDATA=~/pgdata

#check to ensure PGDATA is set: 
echo $PGDATA 
#if variable has not been set to appropriate directory, run: 
source .bash_profile
#or
source profile
#in directory containing profile file (home) 

#make the database directory
mkdir $PGDATA
pg_ctl initdb
pg_ctl start

#create a user database (again, the default will be your current username)
createdb
#open the postgres prompt
psql 
```

## For Both types of USERS

in the PSQL prompt, type in the following (note the semicolon!):

```
CREATE DATABASE ensembl;
exit
```

Then continue on here, running the cells below. 

# Cloning the Repository

Run the following to clone this GitHub repository onto your local machine: 

    git clone https://github.com/mooneymi/large_scale_data.git

Then run 'cd' on Windows (Anaconda Prompt) or 'pwd' on Mac (Terminal) to check file path -- will need to replace file paths below to access data files

Now, you can start the jupyter notebook server in your terminal:

    jupyter notebook

#### Last Updated: 3-Jan-2023
