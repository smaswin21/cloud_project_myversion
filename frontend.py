import streamlit as st

# HEAD ----------------------------
st.set_page_config(
    page_title="Valve Dashboard",
    page_icon="👋",
)

# BODY ----------------------------
st.title('Valve Control Dashboard')

# declare the variables for valve status
valves = {
    'Valve 1': 'closed', 
    'Valve 2': 'closed', 
    'Valve 3': 'closed', 
    }

# Function to send command to the backend
def send_valve_command(valveId, command):
    # Here you would add the logic to send a command to your backend,
    # which would then communicate with Azure IoT Hub
    pass

valveId = st.selectbox('Select Valve', ['Valve 1', 'Valve 2', 'Valve 3'])


if st.button('Open Valve'):
    send_valve_command(valveId, 'open')
    # set the corresponding valve to open
    valves[valveId] = 'open'
    st.success('Command sent to open the valve!')

if st.button('Close Valve'):
    send_valve_command(valveId, 'closed')
    # set the corresponding valve to closed
    valves[valveId] = 'closed'
    st.success('Command sent to close the valve!')



# print the status of the corresponding valve
st.write(f'Status: {valves[valveId]}')