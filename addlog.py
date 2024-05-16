import datetime
import time
def add_log_to_file(file_path, log_message):
    with open(file_path, 'a') as file:
        file.write(log_message + '\n')

def main():
    file_path = 'test.log'

    while True:
        log_message = f"{datetime.datetime.now()} - logs message test"
        add_log_to_file(file_path, log_message)
        print("Log added to file.")
        time.sleep(3)  # Adjust sleep time as needed

main()