This challenge is same as pwn250.just have some protect

```
CANARY    : ENABLED

FORTIFY   : disabled

NX        : ENABLED

PIE       : disabled

RELRO     : Partial
```
In this time, NX is enable,so shellcode can not use,try some time ago,you can find server not open ASLR.

so system address are not random.so first time need to find system addres.

Just leak two got and use http://libcdb.com can know libc verson,and get system address.

Then use like pwn250,controller rbp+8,when exit,will ret to system.

But there have a trouble.that after overwrite rbp+8 and before exit,some where are modif rbp+16

So your argv[1] are wrong.

I'm use pop3_ret to solved it.so system and sh point will overwrite in rbp+40
