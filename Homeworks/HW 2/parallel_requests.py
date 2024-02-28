import concurrent.futures
import requests
import time

# Define the URL where the chatbot service is hosted
SERVICE_ENDPOINT = "http://10.101.54.43:8080/function/chatbot-service"

def send_request_to_service(data_payload):
    """Function to send data to the chatbot service endpoint."""
    try:
        response = requests.post(SERVICE_ENDPOINT, data=data_payload)
        return response.status_code
    except Exception as e:
        return str(e)

def perform_concurrent_requests(req_per_sec, duration_sec=10):
    """Function to send concurrent requests to the service."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_tasks = []
        time_start = time.time()
        
        while time.time() - time_start < duration_sec:
            for _ in range(req_per_sec):
                future = executor.submit(send_request_to_service, "What's the weather like?")
                future_tasks.append(future)
            time.sleep(1)  # Wait before sending the next batch of requests

        results = [future.result() for future in future_tasks]

    successful_results = [result for result in results if result == 200]
    print(f"Total requests sent: {len(results)}")
    print(f"Successful responses: {len(successful_results)}")
    print(f"Success Rate: {(len(successful_results) / len(results)) * 100:.2f}%")

# Example of calling the function:
request_rate = 5  # You can adjust this value to test different load scenarios
perform_concurrent_requests(request_rate)
