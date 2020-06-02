def group_by_owners(files):
    owner_files = {}
    for file_name, owner_name in files.items():
        owner_files[owner_name] = owner_files.get(owner_name, []) + [file_name]
    return owner_files

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))
