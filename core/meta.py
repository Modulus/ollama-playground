
def extract_collection_name(file):
    file_name =  file.split("/")[-1].split(".")[0]
    file_name = file_name.replace("-", "_")
    return file_name


