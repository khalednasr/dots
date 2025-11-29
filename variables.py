import socket

hostname = socket.gethostname()
username = "nasrk"
git_username = "khalednasr"
git_email = "k.nasr92@gmail.com"

home_dir = f"/home/{username}"
config_dir = f"{home_dir}/.config"
repo_dir = f"{home_dir}/dots"

if hostname == "yoyo":
    cpu = "amd"
    gpus = ["amd", "nvidia"]
    laptop = True
    gaming = True

if hostname == "numerino":
    cpu = "intel"
    gpus = ["nvidia"]
    laptop = False
    gaming = True
    displays = {
        "DP-2": {
            "mode": "2560x1440@143.972",
            "scale": "1",
        },
    }
