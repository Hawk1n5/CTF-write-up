First one,we need to check the file info,and protect


$ file web_of_Science


web_of_Science: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=85e0df26435ee411258ad39668c9700b1ebadec9, stripped


gdb-peda$ checksec 
CANARY    : ENABLED
FORTIFY   : disabled
NX        : disabled
PIE       : disabled
RELRO     : Partial
