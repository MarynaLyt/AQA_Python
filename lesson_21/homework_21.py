from datetime import datetime
import re


def read_and_filter_lines(filename, key):
    with open(filename, "r") as file:
        return [line for line in file if key in line]


def extract_timestamps(filtered_lines):
    timestamps = []
    for line in filtered_lines:
        match = re.search(r"Timestamp (\d{2}:\d{2}:\d{2})", line)
        if match:
            time_str = match.group(1)
            time_obj = datetime.strptime(time_str, "%H:%M:%S")
            timestamps.append((time_obj, line.strip()))
    return timestamps


def analyze_and_log(timestamps, output_file):
    with open(output_file, "w") as log_file:
        for i in range(1, len(timestamps)):
            prev_time, _ = timestamps[i - 1]
            current_time, current_line = timestamps[i]
            delta = (current_time - prev_time).total_seconds()

            if 31 < delta < 33:
                log_file.write(f"WARNING: delay {delta:.2f} sec at {current_time.time()} | {current_line}\n")
            elif delta >= 33:
                log_file.write(f"ERROR: delay {delta:.2f} sec at {current_time.time()} | {current_line}\n")


def main():
    filtered = read_and_filter_lines("hblog.txt", "TSTFEED0300|7E3E|0400")
    timestamps = extract_timestamps(filtered)
    timestamps.sort(key=lambda x: x[0])
    analyze_and_log(timestamps, "hb_test.log")


if __name__ == "__main__":
    main()
