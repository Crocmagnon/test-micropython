## Setup / Clean flash

```shell
# Wipe the board's flash (remove all files)
mpremote connect id:e6614104032e192a \
  exec --no-follow "import os, machine, rp2; os.umount('/'); bdev = rp2.Flash(); os.VfsLfs2.mkfs(bdev, progsize=256); vfs = os.VfsLfs2(bdev, progsize=256); os.mount(vfs, '/'); machine.reset()"
echo "Board clean"
sleep 3

# Install dependencies and copy project
cd src/
mpremote connect id:e6614104032e192a \
  mip install github:miguelgrinberg/microdot/src/microdot.py \
    github:miguelgrinberg/microdot/src/microdot_asyncio.py + \
  cp -r . : + \
  reset
cd ..
```

## Update code
```shell
cd src/
mpremote connect id:e6614104032e192a \
  cp -r . : + \
  reset
cd ..
```
