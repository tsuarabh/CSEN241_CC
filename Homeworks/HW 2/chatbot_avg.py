import requests
import time

# Endpoint of your chatbot
CHATBOT_ENDPOINT = "http://10.101.54.43:8080/function/chatbot"

def calculate_response_time(input_data, iterations=1):
    """Calculate the response time for either a single or an averaged over multiple requests."""
    cumulative_time = 0
    for _ in range(iterations):
        start = time.time()
        response = requests.post(CHATBOT_ENDPOINT, data=input_data)
        finish = time.time()
        cumulative_time += (finish - start)
        if iterations == 1:  # Directly return for a single request
            return finish - start
    return cumulative_time / iterations  # Average time if multiple iterations

def main():
    # Measuring response times for various scenarios
    # a. Time for initial request without invoking figlet
    time_first_no_figlet = calculate_response_time("What is your name?")
    print(f"a. Response time for the initial request (without figlet): {time_first_no_figlet:.4f} seconds")

    # b. Time for second request, also without figlet invocation
    time_second_no_figlet = calculate_response_time("What is your name?")
    print(f"b. Response time for the second request (without figlet): {time_second_no_figlet:.4f} seconds")

    # c. Average time across 10 requests, not using figlet
    avg_time_no_figlet = calculate_response_time("What is your name?", iterations=10)
    print(f"c. Average response time for 10 requests (without figlet): {avg_time_no_figlet:.4f} seconds")

    # d. Response time for initial request that does involve figlet
    time_first_with_figlet = calculate_response_time("Generate a figlet for Hello")
    print(f"d. Response time for the initial request (with figlet): {time_first_with_figlet:.4f} seconds")

    # e. Time for the subsequent request, invoking figlet
    time_second_with_figlet = calculate_response_time("Generate a figlet for Hello")
    print(f"e. Response time for the second request (with figlet): {time_second_with_figlet:.4f} seconds")

    # f. Time for a figlet-invoking request following a non-figlet request
    # Record time for initial non-figlet request
    calculate_response_time("What is your name?")
    # Then, for a figlet request
    time_following_no_figlet = calculate_response_time("Generate a figlet for Hello")
    print(f"f. Response time for the subsequent request (with figlet, after a non-figlet request): {time_following_no_figlet:.4f} seconds")

    # g. Average response time over 10 requests invoking figlet
    avg_time_with_figlet = calculate_response_time("Generate a figlet for Hello", iterations=10)
    print(f"g. Average response time for 10 requests (with figlet): {avg_time_with_figlet:.4f} seconds")

if __name__ == "__main__":
    main()
