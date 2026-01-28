import csv

# The data we want to put in the file
data = [
    ['timestamp', 'source_ip', 'attempts_per_minute', 'failed_success_ratio', 'unique_usernames'],
    ['2023-10-01 10:00:01', '192.168.1.5', 2, 0.1, 1],
    ['2023-10-01 12:05:00', '45.76.12.33', 150, 0.99, 85],
    ['2023-10-01 12:10:00', '103.22.140.5', 45, 0.92, 12],
    ['2023-10-01 12:15:00', '172.16.0.5', 1, 0.0, 1]
]

# Writing to the file
with open('test_logs.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("File 'test_logs.csv' has been created successfully!")
