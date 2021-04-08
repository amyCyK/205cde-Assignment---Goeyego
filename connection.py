import pymysql
import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect(host='localhost', user='admin', password='root', database='goeyego')
cursor = db.cursor();

sql_query = 'SELECT VERSION()';

try:
	cursor.execute(sql_query);
	data = cursor.fetchone();
	print('goeyego : %s'%data);

except Exception as e:
	print('Exception :', e);

	connection.close();
else:
	pass
finally:
	pass