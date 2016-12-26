First one,we need to check the file info,and protect
```
web_of_Science: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=85e0df26435ee411258ad39668c9700b1ebadec9, stripped
```

    CANARY    : ENABLED

    FORTIFY   : disabled

    NX        : disabled

    PIE       : disabled

    RELRO     : Partial
begin the execute,you need to pass a simple test,just a equation.

And the you have some features about add paper.

In add paper,there are format string vulnerability in "[3]. Add abstract"

And we know first add name is in `0x6020a0`.

so.need to add one paper to leak rbp address and write shellcode to 0x6020a0.

then controller rbp.when you exit can jump to shellcode.
