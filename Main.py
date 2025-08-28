import streamlit as st
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ========== Gmail SMTP Settings ==========
GMAIL_EMAIL = "u23d7247@sunvalleyncr.in"           # Your Gmail address
GMAIL_APP_PASSWORD = "hnek xgzf bqcw cdgg
"  # Your 16-character Gmail App Password

# ========== Generate a 6-digit OTP ==========
def generate_otp():
    return str(random.randint(100000, 999999))

# ========== Send Email ==========
def send_email(receiver_email, otp):
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_EMAIL
        msg['To'] = receiver_email
        msg['Subject'] = "Your OTP Code"

        body = f"Your OTP code is: {otp}"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

# ========== Streamlit UI ==========
st.title("📧 Send OTP via Gmail")

user_email = st.text_input("Enter your email address:")

if st.button("Send OTP"):
    if user_email:
        otp = generate_otp()
        if send_email(user_email, otp):
            st.success(f"✅ OTP sent to {user_email}")
            st.code(otp, language='text')  # Show OTP for testing only
    else:
        st.warning("⚠️ Please enter an email address.")
