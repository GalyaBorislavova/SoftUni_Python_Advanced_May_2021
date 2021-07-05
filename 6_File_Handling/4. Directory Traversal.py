import os

path, directories, files = next(os.walk(input()))

files_ordered_by_extensions = {}
for file in files:
    ext = file.split(".")[-1]
    if ext not in files_ordered_by_extensions:
        files_ordered_by_extensions[ext] = []
    files_ordered_by_extensions[ext].append(file)


with open("report.txt", "w") as file_to_report:
    for ext in sorted(files_ordered_by_extensions.keys()):
        files_with_ext = files_ordered_by_extensions[ext]
        file_to_report.write(f".{ext}\n")
        for file in sorted(files_with_ext):
            file_to_report.write(f"---{file}\n")


