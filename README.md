# Log Analysis
This project uses a pycopg2 library to do queries on a PostGreSQL database.

Given a populate tables some questions will be answer like:
- What is the most articles of all time?
- Which are the authors of the articles most popular of all time?
- Which days more than 1% of requisitions results on errors?


### How to run
1. Clone this project with:
`git clone https://github.com/cassioesp/log_analysis.git`

2. Download and Install Vagrant and Virtualbox from:
- https://www.vagrantup.com/downloads.html
- https://www.virtualbox.org/

3. Download th database schema from:
- https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

4. Initialize a VM with Vagrant using the following command:
`sudo vagrant up`
`sudo vagrant ssh`

5. Copy and paste the newsdata.sql file into your FSND-Virtual-Machine/vagrant folder.

6. Run the following command to execute the SQL commands on the downloaded file.
`psql -d news -f newsdata.sql`

5. Run log_analysis.py with Python:
`python log_analysis.py`

6. Be sure to have Python, psycopg2 library and PostGreSQL installed!
- https://www.postgresql.org/
- https://www.python.org/
- http://initd.org/psycopg/
