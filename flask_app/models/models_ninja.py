from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas"
class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # classmethod for creating a new ninja  and assigning that ninja to a dojo
    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id)
                VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"""
        return connectToMySQL(db).query_db(query, data)

    #classmethod for selecting a ninja to edit
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s";
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    #classmethod for updating the edited ninja
    @classmethod
    def update(cls, data):
        query = """UPDATE ninjas INTO first_name=%(first_name)s, last_name=%(last_name)s,
                age=%(age)s, updated_at=NOW() WHERE id = %(id)s;"""
        return connectToMySQL(db).query_db(query, data)

    # classmethod for deleting a ninja
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)