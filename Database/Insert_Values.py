# Write to DB
f_SET = open("Database/Settings.db", "r+b")
DB_SET = btree.open(f_SET)

DB_SET[str(10)] = "2520"
DB_SET.flush()

DB_SET.close()
f_SET.close()
