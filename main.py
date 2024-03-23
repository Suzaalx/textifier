from download import download
from transcribe import get_files, transcribe
URLS = ['https://www.youtube.com/watch?v=3bn_r1eFmiY']
download(URLS)
get_files()
transcribe(get_files())
