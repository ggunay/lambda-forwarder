import http.client
import json

EXTERNAL_API_ENDPOINT = "YOUR-EXTERNAL-API-ENDPOINT-WITHOUT-HTTP"

def send_external_api_request(query):
    # Prepare the request data
    payload = json.dumps({"query": query})
    headers = {
        "Content-Type": "application/json",
    }

    # Send the request to the external API
    conn = http.client.HTTPSConnection(EXTERNAL_API_ENDPOINT)
    conn.request("POST", "/", payload, headers)
    response = conn.getresponse()

    # Read and return the response data
    response_data = response.read().decode()
    conn.close()
    return response_data

def parse_response(response_data):
    # Parse the JSON response data
    try:
        parsed_response = json.loads(response_data)
        return parsed_response
    except json.JSONDecodeError as e:
        print("Error decoding JSON response:", e)
        return None

def lambda_handler(event, context):
    try:
        #print('Received event:', event)

        # Extract the request body from the event (assuming it's a JSON object)
        body = event.get('body')
        print(type(body))
        if body:
            body_data = json.loads(body)
            query = body_data.get('query')  # Assuming the input contains a 'query' field

            # Process the query (You can add your own logic here)
            if query:
                # Send the query to the external API
                response_data = send_external_api_request(query)

                # Parse the response from the external API
                parsed_response = parse_response(response_data)

                if parsed_response:
                    result = {'message': f'Query received: {query}', 'external_api_response': parsed_response}
                else:
                    result = {'message': 'Error processing response from the external API'}
            else:
                result = {'message': 'No query found in the request'}
        else:
            result = {'message': 'No request body found'}

        # Construct the response for API Gateway
        response = {
            'statusCode': 200,
            'body': json.dumps(result)
        }

        print('Response:', response)
        return response
    except Exception as e:
        # Handle any errors that occurred during the process
        print('Error:', e)

        # Return an error response to API Gateway
        error_response = {
            'statusCode': 500,
            'body': json.dumps({'error': 'Something went wrong'})
        }

        print('Error Response:', error_response)
        return error_response
