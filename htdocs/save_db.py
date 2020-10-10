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

