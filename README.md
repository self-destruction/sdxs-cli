# sdxs-cli
___
## Setup
To use SDXS you'll need to have [Termux](https://termux.dev), this app allows you to use a linux distro in your mobile phone.
Download [Termux](https://termux.dev) and install it on your phone.

### Install a linux distro
```bash
pkg install proot-distro -y
proot-distro install debian
```
Note: the distro will be located at `/data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/debian/root`.

### Allow Termux to make a storage mount next to $HOME ([wiki](https://wiki.termux.com/wiki/Termux-setup-storage)).
```bash
apt upgrade -y
termux-setup-storage
```

### Login to the linux distro
```bash
proot-distro login debian --shared-tmp
```

### Install sdxs-cli inside the linux distro
```bash
apt update -y
apt install git git-lfs vim python3 python3-pip python3-venv -y
git clone https://github.com/self-destruction/sdxs-cli
cd sdxs-cli/
```

### Install deps of sdxs-cli
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run cli (it will take longer to run the first time, cause model is being downloaded)
```bash
python app.py --prompt "A majestic goat with a realistic sunset and a blue lake, very detailed, a masterpiece"
```

#### Usage params:
```bash
Params:
  --prompt     # prompt string
  --large_vae  # (optional) not exist by default, takes 4 times longer
```

### To get access the generated pictures, you have to exit the linux dist (`exit` command) and copy the contents of the generation folder to mount with the following command:
```bash
cp -r /data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/debian/root/sdxs-cli/output $HOME/storage/downloads
```
Note: now the output folder with generations can be found in the file manager in the root folder `Download`.

### Launching on next times when everything is installed
```bash
proot-distro login debian --shared-tmp
cd sdxs-cli/ && source venv/bin/activate
python app.py --prompt "A majestic goat with a realistic sunset and a blue lake, very detailed, a masterpiece"
```
Don't forget to sync output folder to the mounted one.

## Results
Testing was done on the Snapdragon 8 gen 3. 12+8 gb ram.

| Image                                        | Command                                                                                                           | Result                                                       |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| ![Image](./output/sunset_goat_vae.png)       | `python app.py --prompt "A majestic goat with a realistic sunset and a blue lake, very detailed, a masterpiece"`  | 1/1 [00:03<00:00,  3.94s/it].  Execution time: 7.472 seconds |
| ![Image](./output/sunset_goat_large_vae.png) | `python app.py --prompt "A majestic goat with a realistic sunset and a blue lake, very detailed, a masterpiece" --large_vae` | 1/1 [00:03<00:00,  3.63s/it].  Execution time: 35.191 seconds |
