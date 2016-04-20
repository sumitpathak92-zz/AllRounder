import psycopg2
import sys

con = None

try:
    con = psycopg2.connect(database='allrounder', user='sumit')
    cur = con.cursor()
    cur.execute("INSERT INTO users(name, email_id, age, address, is_service_provider, image_path, lat, lon, gender, notifications, services_used, city, state, pincode)"
                                    " VALUES ( 'rahul bardia', 'rahul92@gmail.com', 24, 'marathahalli', 'yes', 's3_bucket_path', 8.55566, 4.33455, 'male', 'yes', 'transport', 'bangalore', 'karnataka', 560037)")
    # cur.execute("INSERT INTO users(name, email_id, age, address, is_service_provider, image_path, lat, lon, gender, notifications, services_used, city, state, pincode)"
    #                                 " VALUES ( 'rahul bardia', 'rahul92@gmail.com', 24, 'marathahalli', 'yes', 's3_bucket_path', 9.75566, 4.33900, 'male', 'yes', 'gardening', 'mysore', 'karnataka', 560033)")

    con.commit()
    # ver = cur.fetchone()
    print "executed"

except psycopg2.DatabaseError, e:
    if con:
        con.rollback()
    print 'Error %s' %e
    sys.exit(1)

finally:
    if con:
        con.close()