import pymysql


class DataBase:
    def __init__(self, name):
        self.DB = pymysql.connect(host='3.135.170.173',
                     user='muze-staff',
                     password='BOB9-magam-mangham',
                     db='muze_db',
                     charset='utf8')
        self.cursor = self.DB.cursor()

        self.name = name


    def Select_Site(self):
        query = "SELECT data FROM site_json WHERE name = '" + self.name + "' LIMIT 1"
        self.cursor.execute(query)

        select = self.cursor.fetchall()

        return str(select)[3:-5]  # (( 등 전처리 위해


    def Insert_Site(self):
        sql = "INSERT INTO site_json (name, path) VALUES (%s, %s)"

        datapath = '/home/ubuntu/json/' + self.name + '.json'
        self.cursor.execute(sql, (self.name, datapath))

        self.DB.commit()


    def close(self):
        self.DB.close()


if __name__ == '__main__':
    db = DataBase('naver_pre')
    db.Insert_Site()