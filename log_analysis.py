import psycopg2


def main():
    DB_NAME = "news"

    conn = psycopg2.connect(database=DB_NAME)

    cursor = conn.cursor()

    cursor.execute("SELECT title, COUNT(*) as views FROM articles, log \
WHERE articles.slug = substring(log.path, '[^/]*$') GROUP BY articles.title \
ORDER BY views DESC")

    rows = cursor.fetchall()

    for row in rows:
            print row[0] + '-', row[1], ' views'

    print '\n'

    cursor.execute("SELECT name, COUNT(*) as views FROM authors, articles, log \
WHERE authors.id = articles.author AND \
articles.slug = substring(log.path, '[^/]*$')  GROUP BY authors.name \
ORDER BY views DESC")

    rows = cursor.fetchall()

    for row in rows:
        print row[0] + '-', row[1], ' views'

    print '\n'

    cursor.execute("SELECT SUBSTRING(to_char(log.time, 'DD/MM/YYYY'),0,11) AS day, \
COUNT(status)*100/CAST((SELECT COUNT(*) FROM log) AS Float) AS percentage \
FROM log WHERE status = '404 NOT FOUND' GROUP BY day \
HAVING COUNT(status)*100/CAST((SELECT COUNT(*) FROM log) AS Float) > 1;")

    rows = cursor.fetchall()

    for row in rows:
        print row[0] + '-', row[1], ' views'

if __name__ == "__main__":
    main()
