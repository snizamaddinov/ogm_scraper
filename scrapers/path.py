import pathlib

current_path = pathlib.Path(__file__).parent.absolute()
print(current_path)


parent_path = current_path.parent
print(parent_path)

data_path = parent_path / "data"
print(data_path)

data_path.mkdir(exist_ok=True)
file_path = data_path / "data.txt"

with open(file_path, "w") as file:
    file.write("Hello, world!")
    