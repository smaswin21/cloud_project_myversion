import streamlit as st
from azure.iot.device import IoTHubDeviceClient, Message
import os
# HEAD
st.set_page_config(
    page_title="pipe Dashboard",
    page_icon="👋",
)

pipeCS = {
    "pipe1": "HostName=watervalve.azure-devices.net;DeviceId=pipe1;SharedAccessKey=kAAaYB/f+A9NwCSnfUCsbKMp9soTpgwAeAIoTGFWyAM=",
    "pipe2": "HostName=watervalve.azure-devices.net;DeviceId=pipe2;SharedAccessKey=gSAJds4rqKRwT2TvOT6XUUObPVcYWshJeAIoTEvNpwo=",
    "pipe3": "HostName=watervalve.azure-devices.net;DeviceId=pipe3;SharedAccessKey=c/GiJjUjA/IHLK+noHIrcOdT9c0r6+YCIAIoTMg4f9U=",
    "pipe4": "HostName=watervalve.azure-devices.net;DeviceId=pipe4;SharedAccessKey=bR/XNH2R9yVxpG3ghwgeYI2nQ5XoJqNuRAIoTJM2tBw=",
    }

# declare the variables for pipe status
pipeStates = {
    'pipe1': 'closed', 
    'pipe2': 'closed', 
    'pipe3': 'closed', 
    'pipe4': 'closed'
}

def message_to_hub(whichPipe: str, message: str):
    # connecting to iot hub directly from streamlit
    client = IoTHubDeviceClient.create_from_connection_string(pipeCS[whichPipe])
    client.connect()
    # sending message
    client.send_message(Message(message))
    st.success(f"\nMessage {message} sent to {whichPipe}\n")
    client.disconnect()


# BODY
# tab title
st.title('Pipe Control Dashboard')
# Make columns for UX design
col1, col2 = st.columns((1, 1))

# LEFT COL. The selectbox and Open / Close buttons
with col1:
    pipeId = st.selectbox('Select Pipe', list(pipeStates.keys()))
    # st.markdown(f'**State of {pipeId}: {pipeStates[pipeId]}**')

# RIGHT COL. pipe status and success message
with col2:
    btnOpenPipe = st.button('Open pipe')
    btnClosePipe = st.button('Close pipe')

    # Check if a button was pressed
    if btnOpenPipe or btnClosePipe:
        newState = 'open' if btnOpenPipe else 'closed'
        # send state update to iot hub
        message_to_hub(pipeId, newState)
        pipeStates[pipeId] = newState
        # st.session_state['pipeUpdate'] = f'The {pipeId} is now {new_status}'
    
    # Display success message if available
    if 'pipeUpdate' in st.session_state:
        st.success(st.session_state['pipeUpdate'])

