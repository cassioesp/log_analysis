#!/usr/bin/env python2

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

    cursor.execute("SELECT to_char(log.time, 'DD/MM/YYYY') AS day, \
(SELECT COUNT(status) FROM log)/(SELECT COUNT(*) FROM log) AS percentage \
FROM log WHERE status = '404 NOT FOUND' GROUP BY day;")

    rows = cursor.fetchall()

    for row in rows:
        print row[0]

if __name__ == "__main__":
    main()
