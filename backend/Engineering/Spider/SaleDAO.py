import pymysql

class SaleDAO:
    host = "localhost"
    user="root"
    password = "123456"
    charset = "utf8"
    database="car_big_data"

    def insert(self, carModel, saleDatetime, saleRegion):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(F"INSERT INTO `sale_info_table` (`car_model`, `sale_datetime`, `sale_region`) VALUES ('{carModel}', '{saleDatetime}', '{saleRegion}')")
        db.commit()
        cursor.close()
        db.close()


def insert(carModel, saleDatetime, saleRegion):
   saleDAO = SaleDAO
   saleDAO.insert(saleDAO, carModel, saleDatetime, saleRegion)
#test
# saleDAO = SaleDAO
# saleDAO.insert(saleDAO, "1", "1", "2001-10-01 00:00:00", "1")
