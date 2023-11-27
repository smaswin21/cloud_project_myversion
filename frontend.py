import streamlit as st
import time

# HEAD ----------------------------
st.set_page_config(
    page_title="Valve Dashboard",
    page_icon="👋",
)


# BODY ----------------------------

# Function to send command to the backend
def send_valve_command(valveId, command):
    # Here you would add the logic to send a command to your backend,
    # which would then communicate with Azure IoT Hub
    pass

def generate_temporary_success(message, seconds):
    # generate the success
    successContainer = st.success(message)
    # wait amout of time
    time.sleep(seconds)
    # elimilate success
    successContainer.empty()

# tab title
st.title('Valve Control Dashboard')

# create the valveUpdate variable to 
# avoid a specific bug
valveUpdate = ''

# declare the variables for valve status
valves = {
    'Valve 1': 'closed', 
    'Valve 2': 'closed', 
    'Valve 3': 'closed'
    }

# Make columns for UX design
col1, col2 = st.columns((1, 1))

# LEFT COL. The selectbox and Open / Close buttons
with col1:
    # Create a selectbox element which contains the valves
    valveId = st.selectbox('Select Valve', ['Valve 1', 'Valve 2', 'Valve 3'])
    btnOpenValve = st.button('Open Valve')
    btnCloseValve = st.button('Close Valve')

    # the open button is pressed
    if btnOpenValve:
        # send_valve_command() is used in the backend

        send_valve_command(valveId, 'open')
        # set the corresponding valve to open
        valves[valveId] = 'open'
        valveUpdate = f'The valve is {valves[valveId]}'
    
    # the close button is pressed
    if btnCloseValve:
        # send_valve_command() is used in the backend
        
        send_valve_command(valveId, 'closed')
        # set the corresponding valve to closed
        valves[valveId] = 'closed'
        valveUpdate = f'The valve is {valves[valveId]}'
    
# RIGHT COL. Valve status and success message
with col2:
    # print the status of the corresponding valve
    st.markdown(f'**Status: {valves[valveId]}**')
    # print success message after either button
    generate_temporary_success(valveUpdate, 1)

