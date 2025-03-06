# import pathlib

# current_path = pathlib.Path(__file__).parent.absolute()
# print(current_path)


# parent_path = current_path.parent
# print(parent_path)

# data_path = parent_path / "data"
# print(data_path)

# data_path.mkdir(exist_ok=True)
# file_path = data_path / "data.txt"

# with open(file_path, "w") as file:
#     file.write("Hello, world!")

import requests

link = 'https://ogmmateryal.eba.gov.tr/calisma-defteri/icerik-goster/44'
result_without_redirect = requests.get(link, allow_redirects=False)
print(result_without_redirect.status_code)
print(result_without_redirect.headers)

if result_without_redirect.is_redirect:
    print(result_without_redirect.headers["Location"])

    