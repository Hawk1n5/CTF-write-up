This challenage have some difference as pwn350.

First one is test,it need to crack a sha1,like this:

Solve a puzzle: find an x such that SHA1(x)[-3:]=='\xff\xff\xff' and len(x)==29 and x[:24]==161d1717101b1217191a1514

You can find the solve in https://fail0verflow.com/blog/2014/plaidctf2014-crypto375-wheeeee.html.

Copy the code to a.py the run this script to get solved.

And another difference is system have ASLR.

So I want a easy solution.write a ROP in heap which is first add paper name.then leak libc base,overwrite rbp to ret to heap,and execution ROP,I want to call mprotect,and ret to shellcode.I find a gadget can use.

  4019d0:	4c 89 ea             	mov    %r13,%rdx

  4019d3:	4c 89 f6             	mov    %r14,%rsi

  4019d6:	44 89 ff             	mov    %r15d,%edi

  4019d9:	41 ff 14 dc          	callq  *(%r12,%rbx,8)

  4019dd:	48 83 c3 01          	add    $0x1,%rbx

  4019e1:	48 39 eb             	cmp    %rbp,%rbx

  4019e4:	75 ea                	jne    4019d0 <time@plt+0xfd0>

  4019e6:	48 83 c4 08          	add    $0x8,%rsp

  4019ea:	5b                   	pop    %rbx

  4019eb:	5d                   	pop    %rbp

  4019ec:	41 5c                	pop    %r12

  4019ee:	41 5d                	pop    %r13

  4019f0:	41 5e                	pop    %r14

  4019f2:	41 5f                	pop    %r15

  4019f4:	c3                   	retq

it can easy to call any function when you know address..
