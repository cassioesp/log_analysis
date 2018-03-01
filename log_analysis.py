#!/usr/bin/env python

import psycopg2


def main():

    print "What is the most articles of all time?"

    DB_NAME = "news"

    conn = psycopg2.connect(database=DB_NAME)

    cursor = conn.cursor()

    cursor.execute("SELECT title, COUNT(*) as views FROM articles, log \
WHERE articles.slug = substring(log.path, '[^/]*$') GROUP BY articles.title \
ORDER BY views DESC LIMIT 3")

    rows = cursor.fetchall()

    for row in rows:
            print row[0] + '-', row[1], ' views'

    print '\n'

    print "- Which are the authors of the articles most popular of all time?"

    cursor.execute("SELECT name, COUNT(*) as views FROM authors, articles, log \
WHERE authors.id = articles.author AND \
articles.slug = substring(log.path, '[^/]*$')  GROUP BY authors.name \
ORDER BY views DESC")

    rows = cursor.fetchall()

    for row in rows:
        print row[0] + '-', row[1], ' views'

    print '\n'

    print "Which days more of 1% of requisitions results on errors?"

    cursor.execute("CREATE OR REPLACE VIEW v1 as SELECT time::date, COUNT(status) \
as total_errors FROM log WHERE status = '404 NOT FOUND' GROUP BY time::date")

    cursor.execute("CREATE OR REPLACE VIEW v2 as SELECT time::date, COUNT(status) \
as total FROM log GROUP BY time::date")

    cursor.execute("SELECT day, percentage FROM (SELECT v2.time as day,\
 ROUND(CAST(v1.total_errors*100/v2.total::float AS NUMERIC), 2) as percentage\
 FROM v1, v2 WHERE v1.time = v2.time) T WHERE percentage > 1;")
    rows = cursor.fetchall()

    for row in rows:
        print row[0], '-', row[1], '%'

if __name__ == "__main__":
    main()

