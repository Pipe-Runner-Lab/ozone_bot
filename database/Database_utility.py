import sqlite3


class Database_utility(object):
    def __init__(self):
        # creating database cursor
        self.connection = sqlite3.connect('data.db')
        self.cursor = self.connection.cursor()

    def show_all_table():
        print "z"

    def insert_user_data(self, user_id, username):
        try:
            sql = '''INSERT INTO users(user_id,username) VALUES(?,?)'''
            self.cursor.execute(sql, (user_id, username))
            self.connection.commit()
        except:
            sql = '''CREATE TABLE users(user_id integer,username text)'''
            self.cursor.execute(sql)
            self.connection.commit()

    def get_user_data(self, user_id):
        try:
            sql = '''SELECT * FROM users WHERE user_id=?'''

            self.cursor.execute(sql, (user_id,))

            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            if(len(rows) == 0):
                return None
            else:
                return (rows[0])
        except Exception as e:
            print(e)
            return None

    def delete_user_data(self):
        try:
            sql = '''DELETE FROM users'''

            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(e)
            return None
