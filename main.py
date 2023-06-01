# python3

def parallel_processing(n, m, data):
    output = []
    # Create a list to store the finish time for each thread
    finish_time = [0] * n

    for i in range(m):
        # Find the thread with the earliest finish time
        min_finish_time = min(finish_time)
        # Find the index of the thread with the earliest finish time
        min_finish_time_thread = finish_time.index(min_finish_time)

        # The start time for the current job is the finish time of the thread
        start_time = finish_time[min_finish_time_thread]
        # The finish time for the current job is the start time plus the processing time
        finish_time[min_finish_time_thread] += data[i]

        # Append the thread index and start time to the output
        output.append((min_finish_time_thread, start_time))

    return output

def main():
    # Read input from the user
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # Call the parallel_processing function
    result = parallel_processing(n, m, data)

    # Print the output
    for thread, start_time in result:
        print(thread, start_time)

if __name__ == "__main__":
    main()
