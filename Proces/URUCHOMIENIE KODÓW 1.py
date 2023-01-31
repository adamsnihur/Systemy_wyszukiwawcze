import os
import subprocess


scraping_file = "/Users/joachimuetake/Lewoniewski projekt/RTV euro AGD/SCRAPING + FORMATOWANIE 2.py"
final_scrap_file = "/Users/joachimuetake/Lewoniewski projekt/AVANS/FINAL SCRAP 5.py"

subprocess.call(["python", scraping_file])
subprocess.call(["python", final_scrap_file])