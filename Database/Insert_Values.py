# Write to DB
f_SET = open("Database/Settings.db", "r+b")
DB_SET = btree.open(f_SET)

DB_SET[str(40)] = "9000"
DB_SET.flush()

DB_SET.close()
f_SET.close()
