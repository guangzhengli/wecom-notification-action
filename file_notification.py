from asyncore import read
import os
import random

class FileNotification:
    def get_message(self):
        message = self.read_file()
        self.write_file(message)
        return message

    def read_file(self):
        with open(self.get_file_name, 'r', encoding='utf-8') as f:
            read_type = self.get_file_read_type()
            if read_type == 'first':
                return f.readline().strip()
            elif read_type == 'last':
                return f.readline()[-1].strip()
            elif read_type == 'random':
                lines = open('file.txt').read().splitlines()
                return random.choice(lines).strip()
            elif read_type == 'all':
                return f.read().splitlines()
            else:
                raise ValueError(f"error parse file read type: {type}")
                
    def write_file(self, message):
        write_type = self.get_file_write_type
        if write_type == 'loop':
            self.write_file_loop_content()
        elif write_type == 'delete':
            self.write_file_delete_content()

    def write_file_loop_content(file_name):
        with open(file_name, 'r') as file:
            data = file.readlines()
        # make sure the last line ends with newline (may not be the case)
        if not data[-1].endswith("\n"):
            data[-1] += "\n"
        with open (file_name,'w') as fi:
            fi.writelines(data[1:])
            fi.write(data[0])

    def write_file_delete_content(file_name, message):
        with open(file_name, "r") as f:
            lines = f.readlines()
        with open(file_name, "w") as f:
            for line in lines:
                if line.strip("\n") != message:
                    f.write(line)

    def get_file_name():
        return os.environ.get("INPUT_FILE_NAME")

    def get_file_read_type():
        return os.environ.get("INPUT_FILE_READ_TYPE")

    def get_file_write_type():
        return os.environ.get("INPUT_FILE_WRITE_TYPE")