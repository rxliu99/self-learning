#!/usr/bin/env python3
#
# An HTTP server that's a message board.
#
# When a user goes to http://localhost:8000/ in their browser, 
#   a form for writing messages is displayed, as well as 
#   a list of the previously written messages.
# Submitting the form will send a request to the server, 
#   which stores the submitted message and then re-displays it on the page.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

memory = []

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # How long was the message?
        length = int(self.headers.get('Content-length', 0))

        # Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()
        # Extract the "message" field from the request data.
        message = parse_qs(data)["message"][0]

        # Escape HTML tags in the message so users can't break world+dog.
        message = message.replace("<", "&lt;")

        # Store the message in memory.
        memory.append(message)

        # Send a 303 redirect back to the root page.
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Put the form and the stored messages together to create a response.
        response = form.format("\n".join(memory))
        
        # Send the response.
        self.wfile.write(response.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
