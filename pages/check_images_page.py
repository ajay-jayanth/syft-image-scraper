import streamlit as st
import os
import zipfile
import io


st.title('Look through images')
kept_images = {}

for search_name in os.listdir('downloads'):
    st.header(search_name)
    kept_images[search_name] = [f'downloads/{search_name}/{image}' for image in os.listdir(f'downloads/{search_name}')]

    for image in os.listdir(f'downloads/{search_name}'):
        image_path = f'downloads/{search_name}/{image}'
        st.image(image_path)
        image_toggle = st.toggle('Include image', value=True, key=image_path)

        if not image_toggle:
            kept_images[search_name].remove(image_path)

create_zip = st.button('Create Zip File')
zip_buffer = io.BytesIO()
disable_download = True

if create_zip:
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        for search_name, files in kept_images.items():
            for file_path in files:
                arcname = os.path.join('downloads', search_name, os.path.basename(file_path))
                zipf.write(file_path, arcname)
    st.write('Zip File Created and ready to download!')
    disable_download = False

zip_buffer.seek(0)
download_button = st.download_button(
    label='Download Zip',
    data=zip_buffer,
    file_name='images.zip',
    mime='application/zip',
    disabled=disable_download
)
