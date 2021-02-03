import pymysql

class WorldCityDB:
    def __init__(self):
        self.db_connection()

    def db_connection(self):
        self.con = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='pythondb', charset='utf8')
        if self.con:
            print('디비 접속 완료')

    def db_free(self):
        if self.con:
            self.con.close()

    def get_country_list(self):
        sql = 'SELECT * FROM worldcity ORDER BY No DESC;'

        with self.con.cursor() as cursor:
            cursor.execute(sql)

        rows = cursor.fetchall()

        result = []
        for row in rows:
            temp_dic = {}
            temp_dic['No'] = row[0]
            temp_dic['Code'] = row[1]         
            temp_dic['Name'] = row[2]
            temp_dic['GNP'] = row[3]
            temp_dic['Population'] = row[4]
            result.append(temp_dic)
        return result

    def get_country_no(self, no):
            sql = 'SELECT * FROM worldcity WHERE No = %s;'

            with self.con.cursor() as cursor:
                cursor.execute(sql, no)

            row = cursor.fetchone()

            result = {}
            result['No'] = row[0]
            result['Code'] = row[1]         
            result['Name'] = row[2]
            result['GNP'] = row[3]
            result['Population'] = row[4]
            return result
            
    def search_country_list(self, name):
        sql = "SELECT * FROM worldcity WHERE Name LIKE %s;"    
        name = '%' + name + '%'
    
        with self.con.cursor() as cursor:
            cursor.execute(sql, name)

        rows = cursor.fetchall()

        result = []
        for row in rows:
            temp_dic = {}
            temp_dic['No'] = row[0]
            temp_dic['Code'] = row[1]         
            temp_dic['Name'] = row[2]
            temp_dic['GNP'] = row[3]
            temp_dic['Population'] = row[4]
            result.append(temp_dic)
        return result

    def country_add(self, code, name, gnp, population):
        sql = 'INSERT INTO worldcity(Code, Name, GNP, Population) VALUES(%s,%s,%s,%s);'

        with self.con.cursor() as cursor:
            cursor.execute(sql, (code, name, gnp, population))
        self.con.commit()

    def country_delete(self, code):
        sql = 'DELETE FROM worldcity WHERE No = %s;'

        with self.con.cursor() as cursor:
            cursor.execute(sql, code)
        self.con.commit()

    def country_update(self, gnp, population, no):
        sql = 'UPDATE worldcity SET GNP=%s, Population=%s WHERE No = %s;'

        with self.con.cursor() as cursor:
            cursor.execute(sql, (gnp, population, no))
        self.con.commit()

if __name__ == '__main__':
    db = WorldCityDB()
    '''
    for item in db.get_country_list():
        print(item['Name'], item['GNP'])
    
    print('='*30)
    item = db.get_country_no(10)
    print(item['No'], item['Name'], item['GNP'])
    '''
    db.country_update(300,300,31)
    db.db_free