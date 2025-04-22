import asyncio
import json
import logging
import os
import threading
import time

import ipfshttpclient
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Flask app to serve UI and API
app = Flask(__name__, static_folder='static')
CORS(app)  # Enable cross-origin requests


class Web3Chat:
    def __init__(self, channel='web3-realtime-chat', ipfs_url='/ip4/127.0.0.1/tcp/5001'):
        self.channel = channel
        self.messages = []
        self.connected = False

        # Try to connect to IPFS
        try:
            logger.info(f"Trying to connect to IPFS at {ipfs_url}")
            self.client = ipfshttpclient.connect(ipfs_url)
            self.connected = True
            logger.info(f"Successfully connected to IPFS at {ipfs_url}")
        except Exception as e:
            logger.error(f"Failed to connect to IPFS: {e}")
            # Create messages directory for local storage
            self.messages_dir = os.path.join(os.getcwd(), "static", "messages")
            os.makedirs(self.messages_dir, exist_ok=True)

    def store_message(self, user_id, message_text):
        """Store a message in IPFS or local file system and return its CID or ID."""
        message = {
            'user': user_id,
            'text': message_text,
            'timestamp': int(time.time() * 1000)  # Use milliseconds for JS compatibility
        }

        if self.connected:
            try:
                # Add the message to IPFS
                res = self.client.add_json(message)
                cid = res
                message['cid'] = cid
                self.messages.append(message)
                # Publish to PubSub
                try:
                    self.client.pubsub.publish(self.channel, json.dumps(message).encode('utf-8'))
                    logger.info(f"Published message to channel {self.channel}")
                except Exception as e:
                    logger.error(f"PubSub publish failed: {e}")
                return message
            except Exception as e:
                logger.error(f"Error storing message to IPFS: {e}")
                # Fall back to local storage
                return self._store_locally(message)
        else:
            # Store locally
            return self._store_locally(message)

    def _store_locally(self, message):
        # Store locally instead
        message_id = f"{int(time.time())}_{hash(message['text'])}"
        message['id'] = message_id
        self.messages.append(message)

        # Save to local file
        file_path = os.path.join(self.messages_dir, f"{message_id}.json")
        with open(file_path, 'w') as f:
            json.dump(message, f)

        logger.info(f"Message stored locally at {file_path}")
        return message

    def retrieve_message(self, id_or_cid):
        """Retrieve a message from IPFS or local storage using its CID or ID."""
        if self.connected:
            try:
                message = self.client.get_json(id_or_cid)
                return message
            except Exception as e:
                logger.error(f"Error retrieving message from IPFS: {e}")
                # Try local fallback
                return self._retrieve_locally(id_or_cid)
        else:
            # Try to retrieve from local storage
            return self._retrieve_locally(id_or_cid)

    def _retrieve_locally(self, message_id):
        file_path = os.path.join(self.messages_dir, f"{message_id}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return None

    def get_recent_messages(self, limit=50):
        """Get recent messages (from memory or local storage)"""
        return self.messages[-limit:] if self.messages else []

    def pubsub_listener(self):
        """Listen for messages on the PubSub channel."""
        if not self.connected:
            logger.warning("PubSub listener not available without IPFS connection")
            return

        try:
            for message in self.client.pubsub.subscribe(self.channel):
                try:
                    if message['data']:
                        msg_data = json.loads(message['data'].decode('utf-8'))
                        logger.info(f"Received message: {msg_data}")
                        # Add to messages if not already present (avoid duplicates)
                        if msg_data not in self.messages:
                            self.messages.append(msg_data)
                except Exception as e:
                    logger.error(f"Error processing PubSub message: {e}")
        except Exception as e:
            logger.error(f"Error in PubSub listener: {e}")

    def start_listener(self):
        """Start the PubSub listener in a separate thread."""
        if not self.connected:
            logger.warning("Cannot start PubSub listener without IPFS connection")
            return

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.pubsub_listener())
        loop.close()


# Initialize the chat
chat = Web3Chat()

# Create static directory if it doesn't exist
os.makedirs("static", exist_ok=True)

# Write the HTML/JS to static folder
with open("static/index.html", "w") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web3 Realtime Chat</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      margin: 0;
    }
    .chat-container {
      max-width: 600px;
      margin: 20px auto;
      padding: 20px;
      background-color: white;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    .chat-box {
      height: 400px;
      overflow-y: scroll;
      border: 1px solid #ddd;
      padding: 10px;
      margin-bottom: 10px;
      background-color: #fafafa;
      border-radius: 4px;
    }
    .message {
      margin: 8px 0;
      padding: 8px;
      border-radius: 4px;
      background-color: #e6f3ff;
    }
    .message strong {
      color: #333;
    }
    .message small {
      color: #777;
      margin-left: 10px;
    }
    .input-container {
      display: flex;
      gap: 10px;
    }
    input {
      flex: 1;
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
      font-size: 16px;
    }
    button {
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      margin-top: 10px;
    }
    .status {
      text-align: right;
      color: #666;
      font-size: 12px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <div class="chat-container">
    <h2>Web3 Realtime Chat</h2>
    <div class="status" id="ipfs-status">Checking IPFS status...</div>
    <div class="chat-box" id="chat-box"></div>
    <div class="input-container">
      <input type="text" id="message-input" placeholder="Type your message..." />
      <button id="send-button">Send</button>
    </div>
    <div class="error" id="error-box"></div>
  </div>

  <script>
    // Generate a random user ID
    const userId = 'user_' + Math.random().toString(36).substr(2, 9);

    // DOM elements
    const chatBox = document.getElementById('chat-box');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const errorBox = document.getElementById('error-box');
    const statusBox = document.getElementById('ipfs-status');

    // Check IPFS status
    fetch('/api/status')
      .then(response => response.json())
      .then(data => {
        if (data.ipfs_connected) {
          statusBox.textContent = 'IPFS Connected ✓';
          statusBox.style.color = 'green';
        } else {
          statusBox.textContent = 'IPFS Offline ✗ (Using local storage)';
          statusBox.style.color = 'orange';
        }
      })
      .catch(error => {
        statusBox.textContent = 'Server error ✗';
        statusBox.style.color = 'red';
        console.error('Error checking status:', error);
      });

    // Load existing messages
    function loadMessages() {
      fetch('/api/messages')
        .then(response => response.json())
        .then(messages => {
          chatBox.innerHTML = '';
          messages.forEach(displayMessage);
          chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch(error => {
          console.error('Error loading messages:', error);
          errorBox.textContent = 'Failed to load messages.';
        });
    }

    // Display a message in the chat box
    function displayMessage(message) {
      const messageDiv = document.createElement('div');
      messageDiv.className = 'message';

      const sender = document.createElement('strong');
      sender.textContent = message.user + ': ';

      const text = document.createTextNode(message.text);

      const timestamp = document.createElement('small');
      timestamp.textContent = `(${new Date(message.timestamp).toLocaleTimeString()})`;

      messageDiv.appendChild(sender);
      messageDiv.appendChild(text);
      messageDiv.appendChild(timestamp);

      chatBox.appendChild(messageDiv);
    }

    // Send a message
    function sendMessage() {
      const text = messageInput.value.trim();
      if (!text) return;

      // Clear input
      messageInput.value = '';

      // Send to server
      fetch('/api/send', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          user: userId,
          text: text
        })
      })
      .then(response => response.json())
      .then(message => {
        displayMessage(message);
        chatBox.scrollTop = chatBox.scrollHeight;
        errorBox.textContent = '';
      })
      .catch(error => {
        console.error('Error sending message:', error);
        errorBox.textContent = 'Failed to send message. Please try again.';
      });
    }

    // Event listeners
    sendButton.addEventListener('click', sendMessage);

    messageInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        sendMessage();
      }
    });

    // Poll for new messages every 2 seconds
    // This is a fallback for when IPFS pubsub is not working
    setInterval(loadMessages, 2000);

    // Initial message load
    loadMessages();
  </script>
</body>
</html>
""")


# Flask routes
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/status')
def status():
    return jsonify({
        'ipfs_connected': chat.connected,
        'message_count': len(chat.messages)
    })


@app.route('/api/messages')
def get_messages():
    return jsonify(chat.get_recent_messages())


@app.route('/api/send', methods=['POST'])
def send_message():
    data = request.json
    user_id = data.get('user')
    text = data.get('text')

    if not user_id or not text:
        return jsonify({'error': 'Missing user or text'}), 400

    message = chat.store_message(user_id, text)
    return jsonify(message)


@app.route('/api/message/<id_or_cid>')
def get_message(id_or_cid):
    message = chat.retrieve_message(id_or_cid)
    if message:
        return jsonify(message)
    return jsonify({'error': 'Message not found'}), 404


if __name__ == "__main__":
    # Start IPFS listener in a separate thread if connected
    if chat.connected:
        listener_thread = threading.Thread(target=chat.start_listener)
        listener_thread.daemon = True
        listener_thread.start()
        logger.info(f"Listening for messages on channel: {chat.channel}")
    else:
        logger.warning("Running in limited mode without IPFS connection")

    # Run the Flask app
    logger.info("Starting web server at http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
