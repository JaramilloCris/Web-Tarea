import mysql.connector


class AnimalitosDb:


    def __init__(self, user, password):

        self.db = mysql.connector.connect(

            host = "localhost",
            user = user,
            password = password,
            database = "tarea2"
        )
        self.cursor = self.db.cursor()
    
    def save_domicilio(self, data):

        sql = '''

            INSERT INTO domicilio(fecha_ingreso, comuna_id, nombre_calle, numero, sector, nombre_contacto, email, celular)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

        '''
        self.cursor.execute(sql, data)
        self.db.commit()

    def save_mascota_domicilio(self, data):

        sql= '''

            INSERT INTO mascota_domicilio(tipo_mascota_id, edad, color, raza, esterilizado, vacunas_al_dia, domicilio_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)

        '''
        self.cursor.execute(sql, data)
        self.db.commit()
    
    def save_foto_mascota(self, data):

        sql = '''

        INSERT INTO foto_mascota(ruta_archivo, nombre_archivo, mascota_domicilio_id)
        VALUES(%s, %s, %s)
        '''

        self.cursor.execute(sql, data)
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

    def mascora_from_domicilio(self, domicilio_id):

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

    def mascota_by_id(self, id_mascota):

        sql = f'''
        SELECT nombre FROM tipo_mascota WHERE id = {id_mascota}
        '''

        self.cursor.execute(sql)
        return self.cursor.fetchall()