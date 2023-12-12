import streamlit as st
from azure.iot.device import IoTHubDeviceClient, Message
import threading
import json

# Set Streamlit page configuration
st.set_page_config(page_title="Pipe Dashboard", page_icon="👋")

# Connection string for pipe1
PIPE1_CS = "Your Azure IoT Hub Connection String for pipe1"

# Initialize pipe status
pipe_status = {'pipe1': 'closed'}

# Function to connect to IoT Hub and receive messages
def run_azure_client():
    client = IoTHubDeviceClient.create_from_connection_string(PIPE1_CS)
    client.connect()

    def message_received_handler(message):
        # Assuming the message payload is a string with the status
        status = message.data.decode('utf-8')
        pipe_status['pipe1'] = status  # Update the status
        # Use Streamlit's session state to trigger a rerun
        st.session_state['pipe1_status'] = status

    client.on_message_received = message_received_handler

    # Keep the client running
    while True:
        continue

# Start the Azure IoT client in a separate thread
thread = threading.Thread(target=run_azure_client)
thread.daemon = True
thread.start()

# Streamlit UI
st.title('Pipe Control Dashboard')

# Display pipe1 status with a graphical button
status_text = "Pipe 1 Status: Open" if pipe_status['pipe1'] == "open" else "Pipe 1 Status: Closed"
status_color = "green" if pipe_status['pipe1'] == "open" else "red"
button_text = "🟢" if pipe_status['pipe1'] == "open" else "🔴"

st.markdown(f"<h2 style='color: {status_color};'>{button_text} {status_text}</h2>", unsafe_allow_html=True)
