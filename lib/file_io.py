# def write_file(file_name, file_content):
#         if not file_name.endswith('.txt'):
#           file_name += '.txt'

#         with open(file_name, 'w') as file:
#           file.write(file_content)
    

# def append_file(file_name, append_content):
#     if not file_name.endswitch('.txt'):
#         append_content += '.txt'

#         with open(file_name , 'w') as file:
#             file.write(append_content)

#     pass
# def read_file(file_name):
#     if not file_name.endswitch('.txt'):
#         file_name += '.txt'

#     pass

def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt') as f:
        return f.read()