import streamlit as st

st.set_page_config(
    page_title="Valve Dashboard",

    page_icon="👋",
)

st.title('Valve Control Dashboard')

# Assuming you have a function to get the current status of the valve
def get_valve_status(valve_id, command):
    # This function should interact with your backend to get the current status
    # For now, let's just return a placeholder
    return command

# Function to send command to the backend
def send_valve_command(valve_id, command):
    # Here you would add the logic to send a command to your backend,
    # which would then communicate with Azure IoT Hub
    pass

valve_id = st.selectbox('Select Valve', ['Valve 1', 'Valve 2', 'Valve 3'])

if st.button('Open Valve'):
    send_valve_command(valve_id, 'open')
    st.success('Command sent to open the valve!')

if st.button('Close Valve'):
    send_valve_command(valve_id, 'close')
    st.success('Command sent to close the valve!')

st.write(f'Status: {get_valve_status(valve_id)}')

# st.sidebar.success("Select a demo above.")



