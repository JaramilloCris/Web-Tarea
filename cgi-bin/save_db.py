import mysql.connector
import datetime



class AnimalitosDb:


    def __init__(self, user, password):

        self.db = mysql.connector.connect(

            host = "localhost",
            user = user,
            password = password,
            database = "tarea2"
        )
        self.cursor = self.db.cursor()

    def get_last_id(self):

        sql = '''SELECT LAST_INSERT_ID()'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]
    
    def save_domicilio(self, data):

        sql = '''

            INSERT INTO domicilio(fecha_ingreso, comuna_id, nombre_calle, numero, sector, nombre_contacto, email, celular)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

        '''
        self.cursor.execute(sql, data)
        self.db.commit()
        return self.get_last_id()


    def save_mascota_domicilio(self, data):

        sql= '''

            INSERT INTO mascota_domicilio(tipo_mascota_id, edad, color, raza, esterilizado, vacunas_al_dia, domicilio_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)

        '''
        self.cursor.execute(sql, data)
        self.db.commit()
        return self.get_last_id()
    
    def save_foto_mascota(self, data):

        sql = '''

        INSERT INTO foto_mascota(ruta_archivo, nombre_archivo, mascota_domicilio_id)
        VALUES(%s, %s, %s)
        '''

        self.cursor.execute(sql, data)
        self.db.commit()

    def save_new_mascota(self, name):

        sql = '''
        INSERT INTO tipo_mascota(nombre) 
        VALUES(%s)
        '''
        self.cursor.execute(sql, (name,))
        self.db.commit()
        

    def get_all(self, table):

        self.cursor.execute(f'SELECT * FROM {table}')
        return self.cursor.fetchall()

    def get_domicilio_id(self, nombre_calle,sector, nombre_contacto):

        id_domicilio = f'''
            SELECT id FROM domicilio WHERE nombre_calle = '{nombre_calle}' AND sector = '{sector}' AND nombre_contacto = '{nombre_contacto}';
        '''
        self.cursor.execute(id_domicilio)
        value = self.cursor.fetchall()
        return value[0][0]

    def get_comuna_id(self, comuna):

        id_comuna = f'''

            SELECT id FROM comuna WHERE nombre = '{comuna}';
            '''

        self.cursor.execute(id_comuna)
        value = self.cursor.fetchall()
        return value[0][0]

    def get_mascota_id(self, tipo, edad, color, id_domicilio, raza):

        id_mascota = f'''

        SELECT id FROM mascota_domicilio WHERE tipo_mascota_id = '{tipo}' AND edad = '{edad}' AND color = '{color}' AND domicilio_id = '{id_domicilio}' AND raza = '{raza}';
        '''

        self.cursor.execute(id_mascota)
        value = self.cursor.fetchall()
        return value[0][0]

    def ultimo_domicilio(self, cantidad):

        sql= f'''
        SELECT * FROM domicilio ORDER BY fecha_ingreso DESC LIMIT {cantidad}
        '''

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def comuna_by_id(self, id_comuna):

        sql =f'''
        SELECT nombre FROM comuna WHERE id = '{id_comuna}'
        '''

        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def region_by_comunaid(self, id_comuna):

        sql =f'''
        SELECT nombre FROM region INNER JOIN (SELECT id as id_comuna, nombre as nombre_comuna, region_id FROM comuna WHERE id = {id_comuna}) AS comuna_id ON region.id = comuna_id.region_id         
        '''

        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def mascota_from_domicilio(self, domicilio_id):

        sql = f'''
        SELECT * FROM mascota_domicilio WHERE domicilio_id = '{domicilio_id}'
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_sum_mascotas(self, id_domicilio):

        sql = f'''
        SELECT tipo_mascota_id, COUNT(*) as total FROM mascota_domicilio WHERE domicilio_id = {id_domicilio} GROUP BY tipo_mascota_id
        '''

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def count_all_mascotas(self, id_domicilio):

        sql = f'''
        SELECT COUNT(*) FROM mascota_domicilio WHERE domicilio_id = {id_domicilio}
        '''

        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0] 

    def mascota_by_id(self, id_mascota):

        sql = f'''
        SELECT nombre FROM tipo_mascota WHERE id = {id_mascota}
        '''

        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def id_mascota_by_name(self, name):

        sql = f'''
        SELECT id FROM tipo_mascota WHERE nombre = '{name}'
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def image_from_domicilio(self, id_domicilio, limite):

        sql = f'''
        SELECT ruta_archivo FROM mascota_domicilio INNER JOIN foto_mascota ON mascota_domicilio.id = foto_mascota.mascota_domicilio_id WHERE domicilio_id = {id_domicilio} LIMIT {limite}
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def count_fotos_mascota(self, id_mascota):

        sql = f'''
        SELECT COUNT(*) FROM foto_mascota WHERE mascota_domicilio_id = {id_mascota}
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_tipos_mascotas(self):

        sql = f'''
        SELECT * FROM tipo_mascota

        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def esterilizado(self, value):

        if value == 0:
            return "No"
        elif value == 1:
            return "Si"
        else:
            "No aplica"



    # -------------------- Funciones para graficos ---------------------


    def read_date(self):

        """
        Entrega la consulta sql con la cantidad de censos realizados por dias
        :return: Consulta SQL
        """

        sql = f'''SELECT DATE(fecha_ingreso) Date, COUNT(DISTINCT id) totalCOunt FROM domicilio GROUP BY DATE(fecha_ingreso);'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def read_mascotas(self):

        """
        Entrega la consulta sql con la cantidad de las distintas mascotas presentes en la base de datos
        :return: Consulta SQL
        """

        sql = f'''SELECT nombre, cantidad FROM tipo_mascota INNER JOIN (SELECT tipo_mascota_id, COUNT(tipo_mascota_id) AS cantidad FROM mascota_domicilio GROUP BY tipo_mascota_id) AS F ON tipo_mascota.id = f.tipo_mascota_id 

        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def read_gatos_perros(self):

        """
        Entrega una consulta sql con la cantidad de perros y gatos censados en cada mes
        :return: Consulta SQL
        """

        sql = '''SELECT Fecha, coalesce(Perros, 0) AS Perros, coalesce(Gatos, 0) AS Gatos FROM (


            SELECT * FROM (SELECT Fecha1, COUNT(tipo_mascota_id) AS Perros FROM (SELECT EXTRACT(YEAR_MONTH FROM fecha_ingreso) AS Fecha1, tipo_mascota_id FROM (SELECT fecha_ingreso, tipo_mascota_id FROM domicilio INNER JOIN mascota_domicilio ON domicilio.id = mascota_domicilio.domicilio_id) AS masct WHERE masct.tipo_mascota_id = 1) AS conteo GROUP BY Fecha1) AS table1

            LEFT JOIN (SELECT Fecha, COUNT(tipo_mascota_id) AS Gatos FROM (SELECT EXTRACT(YEAR_MONTH FROM fecha_ingreso) AS Fecha, tipo_mascota_id FROM (SELECT fecha_ingreso, tipo_mascota_id FROM domicilio INNER JOIN mascota_domicilio ON domicilio.id = mascota_domicilio.domicilio_id) AS masct WHERE masct.tipo_mascota_id = 2) AS conteo GROUP BY Fecha) AS table2 ON table1.Fecha1 = table2.Fecha

            UNION

            SELECT * FROM (SELECT Fecha1, COUNT(tipo_mascota_id) AS Perros FROM (SELECT EXTRACT(YEAR_MONTH FROM fecha_ingreso) AS Fecha1, tipo_mascota_id FROM (SELECT fecha_ingreso, tipo_mascota_id FROM domicilio INNER JOIN mascota_domicilio ON domicilio.id = mascota_domicilio.domicilio_id) AS masct WHERE masct.tipo_mascota_id = 1) AS conteo GROUP BY Fecha1) AS table1

            RIGHT JOIN (SELECT Fecha, COUNT(tipo_mascota_id) AS Gatos FROM (SELECT EXTRACT(YEAR_MONTH FROM fecha_ingreso) AS Fecha, tipo_mascota_id FROM (SELECT fecha_ingreso, tipo_mascota_id FROM domicilio INNER JOIN mascota_domicilio ON domicilio.id = mascota_domicilio.domicilio_id) AS masct WHERE masct.tipo_mascota_id = 2) AS conteo GROUP BY Fecha) AS table2 ON table1.Fecha1 = table2.Fecha) AS uwu'''

        self.cursor.execute(sql)
        return self.cursor.fetchall()
