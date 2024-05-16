import boto3
import time
import os

log_group_name = 'picon-log'
log_stream_name = 'tream-picon'


def send_logs_to_cloudwatch(log_group_name, log_stream_name, message):

    log_events = [
    {
        'timestamp': int(round(time.time() * 1000)),
        'message': f"{message}"
    }]


    client = boto3.client('logs')
    response = client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=log_events
    )
    print(response)


def get_new_lines(file_path, last_position):
    with open(file_path, 'r') as file:
        # Move to the last known position in the file
        file.seek(last_position)
        # Read new lines
        new_lines = file.readlines()
        # Update last position
        last_position = file.tell()
    return new_lines, last_position

def main():
    file_path = 'test.log'
    # Store the last known position in the file
    last_position = 0

    while True:
        if os.path.exists(file_path):
            new_lines, last_position = get_new_lines(file_path, last_position)
            if new_lines:
                print("New lines detected:")
                for line in new_lines:
                    print(line.strip())
                    send_logs_to_cloudwatch(log_group_name, log_stream_name, line.strip())
            else:
                print("No new lines.")
        else:
            print("File doesn't exist.")

        # Check for updates every 1 second (adjust as needed)
        time.sleep(10)

main()


