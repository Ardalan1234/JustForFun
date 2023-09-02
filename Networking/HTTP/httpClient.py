import http.client

HOST = ''
PORT = 8000

# Create an HTTP connection
conn = http.client.HTTPConnection(HOST, PORT)

# Send an HTTP GET request
conn.request("GET", "/")

# Get the response
response = conn.getresponse()

# Print the response status code and body
print("Response Status:", response.status)
print("Response Body:", response.read().decode())

# Close the connection
conn.close()
