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
