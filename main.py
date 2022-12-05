"""
for now, just having a set amount of users, and the ability to change their email and password with password encryption, and then add them into a database. Then check with john on if this is ok for the assignment or do I need the ability for the user to add in custom users or not 
"""


import sqlite3
from datetime import datetime
import bcrypt
import csv

connection = sqlite3.connect("User Database.db")
cursor = connection.cursor()


def make_db():
    with open("data.sql") as creator:
        queries = creator.read()

        cursor.executescript(queries)
        connection.commit()


def import_users(user_list):

    with open("import_users.csv", "w", newline="") as writing_csv:
        writer = csv.writer(writing_csv)
        writer.writerow(
            [
                "user_id",
                "first_name",
                "last_name",
                "email",
                "hashed_password",
                "city",
                "state",
                "administrator",
                "active",
                "date_created",
            ]
        )
        for data in user_list:
            writer.writerow(data)

    insert_query = "INSERT INTO Users (user_id, first_name, last_name, email, hashed_password, city, state, administrator, active, date_created) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

    with open("import_users.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        csv_data = []

        fields = next(reader)
        # print(fields)
        for row in reader:
            csv_data.append(row)

    for user in csv_data:
        cursor.execute(insert_query, user)

    connection.commit()


class Users:
    def __init__(
        self, user_id, first_name, last_name, email, city, state, administrator, active
    ):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = None
        self.city = city
        self.state = state
        self.administrator = administrator
        self.active = active
        self.date_created = str(datetime.now())
        self.attributes = [
            self.id,
            self.first_name,
            self.last_name,
            self.email,
            self.password,
            self.city,
            self.state,
            self.administrator,
            self.active,
            self.date_created,
        ]

    def user_info(self):
        print(
            f"User ID: {self.id} \nName: {self.first_name} {self.last_name} \nEmail: {self.email} \nHashed Password: {self.password} \nCity: {self.city} \nState: {self.state} \nAdministrator: {self.administrator} \nActive: {self.active} \nDate Created: {self.date_created}"
        )

    def update_db(self):
        values = [self.id, self.first_name, self.last_name, self.city, self.state]
        cursor.execute("INSERT OR UPDATE WHERE user_id = ?", values)


def change_password(user_id):
    user_id = f"{user_id}"
    salt = bcrypt.gensalt()
    update_query = "SELECT * FROM Users WHERE user_id = ?"
    row = cursor.execute(update_query, (user_id,)).fetchone()

    if not row[4]:
        first_password = input(
            "Password not found. Please input password \n (PRESS ENTER TO RETURN) \n > "
        )
        if first_password:
            encoded_pass = first_password.encode()
        else:
            return None

    if row[4]:
        pass_check = input("Input current password \n (PRESS ENTER TO RETURN) \n > ")
        pass_check = pass_check.encode()
        print(pass_check)
        while True:
            if pass_check:
                print(pass_check)
                encoded_pass_check = row[4].encode()
                password_matches = bcrypt.checkpw(pass_check, encoded_pass_check)
                print(password_matches)
                if password_matches == True:
                    new_pass = input(
                        "Please input new password \n(PRESS ENTER TO RETURN) \n > "
                    )
                    if new_pass:
                        check_password = input(
                            "Type in the same password \n(PRESS ENTER TO RETURN) \n > "
                        )
                        if check_password:
                            if new_pass == check_password:
                                print("Password changed")
                                encoded_pass = new_pass.encode()
                            elif new_pass != check_password:
                                print("New passwords do not match \n")
                                continue
                        else:
                            return None
                    else:
                        return None
                else:
                    pass_check = input(
                        "Incorrect password. Please input correct password. \n (PRESS ENTER TO RETURN) \n > "
                    )
                    continue
            else:
                return None

    hashed_password = bcrypt.hashpw(encoded_pass, salt)
    hashed_password = hashed_password.decode()
    update_query = "UPDATE Users SET hashed_password = ? WHERE user_id = ?"
    values = (hashed_password, user_id)
    cursor.execute(update_query, values)
    # connection.commit()


def change_email(user_id, new_email):
    update_query = "UPDATE Users SET email = ? WHERE user_id = ?"
    values = (new_email, user_id)

    cursor.execute(update_query, values)
    connection.commit()


def view_users(filter=None):
    user_rows = cursor.execute("SELECT * FROM Users;").fetchall()

    if not filter:
        print(
            f'{"User ID":<10} {"First and last name":20} {"Email":<30} {"Admin":^10} Active'
        )

        print(
            f"{'-------':<10} {'-------------------':20} {'-----------------':<30} {'-----':^10} {'------'}"
        )

        for row in user_rows:
            print(
                f"{row[0]:<10} {row[1]} {row[2]:20} {row[3]:<30} {row[7]:^10} {row[8]}"
            )

    elif filter:
        filter = f"{filter}"
        row = cursor.execute(
            "SELECT * FROM Users WHERE user_id = ?", (filter,)
        ).fetchone()

        print(
            f"{'User ID: '} {row[0]} \n{'Name: '} {row[1]} {row[2]} \n{'Email: '} {row[3]} \n{'Hashed Password: '} {row[4]} \n{'City: '} {row[5]} \n{'State: '} {row[6]} \n{'Admin: '} {row[7]} \n{'Active: '} {row[8]} \n{'Date Added: '} {row[9]} \n"
        )


user_1 = Users(
    1, "John", "Doe", "john.doe@fake.com", "Salt Lake City", "UT", "True", "True"
)


user_2 = Users(
    2, "Steve", "Lexington", "steve.lexington@fake.com", "Orem", "UT", "False", "True"
)


user_3 = Users(
    3, "Sherry", "Berry", "SherriesBerries@fake.com", "Layton", "UT", "False", "False"
)


lists_of_list_of_users = [
    user_1.attributes,
    user_2.attributes,
    user_3.attributes,
]

make_db()
# import_users(lists_of_list_of_users)

while True:
    view_users()
    inquiry_1 = input(
        "To view more information on a user and make changes, type in their User ID \n [Q] Quit \n > "
    )

    if inquiry_1.upper() == "Q":
        quit("Goodbye")

    elif inquiry_1.isnumeric():
        view_users(inquiry_1)
        inquiry_2 = input(
            "[1] Change/add password \n[2] Change email \n[PRESS ENTER TO GO BACK]"
        )
        if inquiry_2:
            if inquiry_2 == "1":
                change_password(inquiry_1)
            elif inquiry_2 == "2":
                email_inqury = input("Enter new email\n > ")
                change_email(inquiry_1, email_inqury)
                print("Email has been changed \n")
            else:
                print("Input not recognized")
                inquiry_2 = input(
                    "[1] Change/add password \n[2] Change email \n[PRESS ENTER TO GO BACK]"
                )
        if not inquiry_2:
            pass

    else:
        print("Input not reccognized, please try again. \n")


# Create user object from SELECT (SELECT * FROM Users WHERE ID = ?)-> Users(id,name,city,email) -> update user object -> push that back to DB

# SELECT * -> First Name, Last Name, City, Email, Acitve, Date
# Create user using -> TUPLE Call it my_user:
# first_name = my_user[1]
# last_name = my_user[2]
# id = my_user[0]
# my_class_object = Users(first_name, last_name, ir)
