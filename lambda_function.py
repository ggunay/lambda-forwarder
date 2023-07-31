import http.client
import json

def lambda_handler(event, context):
    try:
        print('Received event:', event)

        # Extract the request body from the event (assuming it's a JSON object)
        body = event.get('body')
        print(type(body))
        if body:
            body_data = json.loads(body)
            query = body_data.get('query')  # Assuming the input contains a 'query' field

            # Process the query (You can add your own logic here)
            if query:
                # Make the API request
                connection = http.client.HTTPSConnection("API_endpoint_to_forward_to")
                headers = {'Content-type': 'application/json'}
                data = json.dumps({"query": query})
                connection.request("POST", "/", data, headers)
                
                # Get the response from the API
                response = connection.getresponse()
                result = response.read().decode()

                # Close the connection
                connection.close()

                # Parse the response from the API
                response_data = json.loads(result)
            else:
                response_data = {'error': 'No query found in the request'}
        else:
            response_data = {'error': 'No request body found'}

        # Construct the response for API Gateway
        response = {
            'statusCode': 200,
            'body': json.dumps(response_data)
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
