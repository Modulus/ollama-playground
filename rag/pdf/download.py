import urllib.request
import sys
import os

from helper import get_root_folder

root_folder = get_root_folder()
print(f"Root folder: {root_folder}")
core_folder = os.path.join(root_folder, "core")
print(f"Core folder: {core_folder}")

sys.path.insert(0, core_folder)


from download import download, save, handle, extract_file_name, handle_binary


urls = [
    "https://www.regjeringen.no/contentassets/c499c3b6c93740bd989c43d886f65924/no/pdfs/nasjonal-digitaliseringsstrategi_ny.pdf",
    "https://www.swift.com/sites/default/files/files/swift-iso20022fordummies-6thedition-2022.pdf",
    "https://www.regjeringen.no/contentassets/7400c9d08a5543b8912fbf700f3344fd/no/pdfs/stm202320240031000dddpdfs.pdf",
]


# if __name__ == "__main__":
#     for url in urls:
        
#         extracted_file_name = extract_file_name(url)

#         print(f"Extracted file name: {extracted_file_name}")
#         handle_binary(url=url, filename=extracted_file_name)
       

#         if not os.path.exists("files"):
#             os.makedirs("files")

#         name = os.path.join(os.path.abspath("files"), extracted_file_name)
#         print(f"Saving file to: {name}")
#         handle(url=url, filename=name)