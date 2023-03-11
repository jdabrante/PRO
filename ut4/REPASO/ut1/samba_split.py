# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    smb_path = smb_path.strip("/")
    sidebar = smb_path.find("/")
    host = smb_path[:sidebar]
    path = smb_path[sidebar:]
    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')