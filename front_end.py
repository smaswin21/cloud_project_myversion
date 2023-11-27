import streamlit as st
# time is not typically recommended for use in Streamlit for delaying operations
# Streamlit's rerun feature should be used instead

# HEAD
st.set_page_config(
    page_title="Valve Dashboard",
    page_icon="👋",
)

# body

# Function to send command to the backend
def send_valve_command(valveId, command):
    # Implement the logic to send a command to your backend,
    # which would then communicate with Azure IoT Hub
    pass

# tab title
st.title('Valve Control Dashboard')

# declare the variables for valve status
valves = {
    'Valve 1': 'closed', 
    'Valve 2': 'closed', 
    'Valve 3': 'closed',
    'Valve 4': 'closed',  # Added fourth valve
}

# Make columns for UX design
col1, col2 = st.columns((1, 1))

# LEFT COL. The selectbox and Open / Close buttons
with col1:
    valveId = st.selectbox('Select Valve', list(valves.keys()))
    btnOpenValve = st.button('Open Valve')
    btnCloseValve = st.button('Close Valve')

    # Check if a button was pressed
    if btnOpenValve or btnCloseValve:
        new_status = 'open' if btnOpenValve else 'closed'
        send_valve_command(valveId, new_status)
        valves[valveId] = new_status
        st.session_state['valveUpdate'] = f'The {valveId} is now {new_status}'

# RIGHT COL. Valve status and success message
with col2:
    st.markdown(f'**Status of {valveId}: {valves[valveId]}**')

    # Display success message if available
    if 'valveUpdate' in st.session_state:
        st.success(st.session_state['valveUpdate'])
