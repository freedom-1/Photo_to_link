import asyncio
import streamlit as st
from photograph import photo_link
from io import BytesIO
import time

st.set_page_config(
    page_title="JPG_TO_LINK",
    page_icon="🧑‍💻",
    layout="wide")
st.markdown("<h3 style='text-align:center;'>Bizga bir yoki bir nechta 🖼 rasm yuboring biz har bir rasm uchun 🔗havola yasab beramiz</h3>", unsafe_allow_html=True)
st.caption("Dastur yaratuvchisi: 🧑‍💻<a href='http://t.me/shohabbosdev'>Shoh Abbos Ulug'murodov</a>", unsafe_allow_html=True)

async def main():
    try:
        pictures_files = st.file_uploader("Rasmni shu qismga kiritasiz", type=['jpg', 'png', 'gif'],accept_multiple_files=True)
        for picture in pictures_files:
            photo_bytes = BytesIO(picture.read())
            if picture is not None:
                st.balloons()
                link = await photo_link(photo_bytes)
                ustun1,ustun2 = st.columns(2)
                ustun1.image(picture, f"Siz kiritgan tasvir fayli nomi: {picture.name}", width=300)
                ustun2.markdown(f"<h6 align='left'>Rasm linki👇👇👇</h6> <a href='{link}''>✅ Yuklab olish</a>",unsafe_allow_html=True)

        else:
            st.info("", icon='🥱')
    except Exception as e:
        st.error(f"Xatolik paydo bo'ldi: {e}", icon='⛔️')

if __name__ == "__main__":
    asyncio.run(main())

# async def main():
#     with open(picture, 'rb') as photo_file:  
