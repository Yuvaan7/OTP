import streamlit as st
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace with your own email details
SENDER_EMAIL = "U23D7247sunvalleyncr.in"
SENDER_PASSWORD = "svis@12345"

# Generate a random 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Send the OTP to the user's email
def send_email(receiver_email, otp):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver_email
        msg['Subject'] = "Your OTP Code"

        body = f"Your OTP code is: {otp}"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

# Streamlit App
st.title("🔐 Email OTP Verification")

# Step 1: User enters their email
user_email = st.text_input("Enter your email address to receive an OTP:")

if st.button("Send OTP"):
    if user_email:
        otp = generate_otp()
        st.session_state['otp'] = otp
        st.session_state['email_sent'] = send_email(user_email, otp)
        if st.session_state['email_sent']:
            st.success("✅ OTP sent to your email.")
    else:
        st.warning("Please enter a valid email address.")

# Step 2: User enters received OTP
if st.session_state.get('email_sent'):
    user_otp_input = st.text_input("Enter the OTP sent to your email:")

    if st.button("Verify OTP"):
        if user_otp_input == st.session_state.get('otp'):
            st.success("🎉 OTP verified successfully!")
        else:
            st.error("❌ Invalid OTP. Please try again.")
