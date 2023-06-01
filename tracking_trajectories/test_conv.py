def generate_python_script(txt_file_path, py_file_path):
    with open(txt_file_path, 'r') as txt_file:
        content = txt_file.read()

    with open(py_file_path, 'w') as py_file:
        py_file.write(content)

txt_file_path = 'joint_states.txt'
py_file_path = 'tracking_points.py'
generate_python_script(txt_file_path, py_file_path)
