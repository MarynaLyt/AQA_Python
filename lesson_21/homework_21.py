from datetime import datetime
import re

with open("hblog.txt", "r") as file:
    lines = file.readlines()

filtered_lines = [line for line in lines if "TSTFEED0300|7E3E|0400" in line]

timestamps = []
for line in filtered_lines:
    match = re.search(r"Timestamp (\d{2}:\d{2}:\d{2})", line)
    if match:
        time_str = match.group(1)
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        timestamps.append((time_obj, line.strip()))

timestamps.sort(key=lambda x: x[0])

with open("hb_test.log", "w") as log_file:
    for i in range(1, len(timestamps)):
        prev_time, _ = timestamps[i - 1]
        current_time, current_line = timestamps[i]
        delta = (current_time - prev_time).total_seconds()

        if 31 < delta < 33:
            log_file.write(f"WARNING: delay {delta:.2f} sec at {current_time.time()} | {current_line}\n")
        elif delta >= 33:
            log_file.write(f"ERROR: delay {delta:.2f} sec at {current_time.time()} | {current_line}\n")
