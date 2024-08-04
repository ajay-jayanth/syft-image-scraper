
import streamlit as st
from google_images_download import google_images_download
import os
import shutil


def scrape_images(args):
    response = google_images_download.googleimagesdownload()
    paths = response.download(args)
    return paths

st.title('Syft Internal Images Scraping App')
keywords = st.text_input('Enter keywords to search and separate with comma (,):')
search_limit = st.number_input(label='Enter maximum images to download from each keyword search:', value=20, min_value=1)
submit_button = st.button('Submit')

if st.button('Reset', type='secondary'):
    try:
        shutil.rmtree('downloads')
    except FileNotFoundError as e:
        pass
    os.makedirs('downloads', exist_ok=True)
    st.write(os.listdir('downloads'))

if submit_button:
    args = {
        'keywords': keywords,
        'limit': search_limit,
        'print_urls': True
    }
    paths = scrape_images(args)

    keyword_list = keywords.split(',')

            