import json
from shared import FILE_PATH_ROOT

# klasa koja pohranjuje emailove u datoteku
class EmailsRepo:
    def __init__(self, file_path=FILE_PATH_ROOT + "emails.json"):
        self.file_path = file_path

    def save_mail(self, email):
        with open(self.file_path, "w") as file_writer:
            json.dump(email, file_writer, indent=4)
    
    def get_all_emails(self):
        try:
            with open(self.file_path, "r") as file:
                emails = [line.strip() for line in file.readlines()]
                return emails
        except FileNotFoundError:
            print(f'File not found {self.file_path}')
        except Exception as ex:
            print(f"Error reading emails from file: {ex}")
            return []