import streamlit as st
import io
import base64
import glob
import os
from PIL import Image

# Đặt tiêu đề cho ứng dụng
st.set_page_config(
    page_title="MMTeam",
    page_icon="https://freelogopng.com/images/all_img/1681038242chatgpt-logo-png.png"
)

# title
st.title("[Stable Cascade model] Text to Image")


# Danh sách để lưu trữ các tin nhắn
if "messages" not in st.session_state:
    st.session_state.messages = []


def img_to_base64(img):
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return base64.b64encode(buffer.read()).decode()

# Hàm để xóa tất cả hình ảnh trong thư mục "images"


def clear_images_folder(folder_path):
    for img_path in glob.glob(os.path.join(folder_path, "*")):
        os.remove(img_path)

# Hàm để hiển thị lịch sử chat


def display_chat():
    for msg in st.session_state.messages:
        if "user" in msg:
            st.markdown(
                f"""
               <div style="background-color: rgb(244,244,244); padding: 10px; border-radius: 15px; margin-bottom: 5px; display: inline-block; text-align: right; float: right;">
                  {msg['user']}
               </div>
               """,
                unsafe_allow_html=True
            )
        elif "bot" in msg:
            # Thay thế chữ "Bot" bằng hình logo
            st.markdown(
                f"""
               <div style="display: flex; align-items: flex-start; margin-bottom: 10px; padding: 10px">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/1/13/ChatGPT-Logo.png" alt="ChatGPT Logo" style="width: 50px; height: auto; border-radius: 15px; margin-right: 10px; align-self: flex-start;"/>
                  <img src="data:image/png;base64,{img_to_base64(msg['bot'])}" alt="Hình ảnh phản hồi từ chương trình" style="border-radius: 15px; width: 400px"/>
               </div>
               """,
                unsafe_allow_html=True
            )


# Giao diện nhập tin nhắn
user_input = st.chat_input("What do you want to see?")

# Xử lý khi người dùng gửi tin nhắn
if user_input:
    # Lưu tin nhắn của người dùng vào session state
    st.session_state.messages.append({"user": user_input})

    # Xử lý prompt và tạo hình ảnh (ở đây là hình ảnh mẫu)
    # Bạn có thể thay thế bằng logic của riêng mình
    # Thay thế bằng đường dẫn đến hình ảnh của bạn
    img = Image.open("./gen_img/cascade.png")

    # Lưu hình ảnh phản hồi (có thể dựa trên logic của bạn)
    st.session_state.messages.append({"bot": img})

    # Hiển thị lịch sử chat
    display_chat()

# Tùy chọn để xóa tin nhắn
if st.button("Clear history"):
    st.session_state.messages = []
    clear_images_folder("./gen_img")
