# chal_2_1

Take the bytes (it's machine code!) and disassemble it.

1. Jump to 0x0000002D (`jmp 0x0000002D`)
2. `call 0x0000000002`. This places the stack pointer on the following address (the return address)
3. XOR byte at address pointed by `RSI` with `0x13` 0x22 times (size of encrypted data)
4. `RSI` set to start of decrypted string (`write`'s `const char *buf` param)
5. `RAX` set to `0x01` (syscall for `write`)
6. `RDI` set to `0x01` (fd for `STDOUT`)
7. `RDX` set to `0x24` (size of decrypted string)
8. Print decrypted string to stdout
9. Set `RAX` to `0x3C` (syscall for `exit`)
10. Exit

We must then XOR the bytes with the correct key

Note 1: In ghidra, the hex values are in big-endian (human readable). Once disassembled, the hex values are in little-endian (computer readable).
Note 2: The key is the wrong one.

For reference, here is the encrypted hex: `0x0C060B0D670F231E07303F20053A043D13092F2F383C1B070C252E7A22271002090A`

And the disassembled code:
```
0x00000000 EB2B                            JMP 0x0000002D
0x00000002 5E                              POP RSI
0x00000003 4831C9                          XOR RCX,RCX
0x00000006 80C122                          ADD CL,0x22
0x00000009 803613                          XOR BYTE PTR [RSI],0x13
0x0000000C 48FFC6                          INC RSI
0x0000000F E2F8                            LOOP 0x00000009
0x00000011 4883EE22                        SUB RSI,0x22
0x00000015 4831C0                          XOR RAX,RAX
0x00000018 B001                            MOV AL,0x01
0x0000001A 4889C7                          MOV RDI,RAX
0x0000001D 4889FA                          MOV RDX,RDI
0x00000020 4883C223                        ADD RDX,0x23
0x00000024 0F05                            SYSCALL
0x00000026 4831C0                          XOR RAX,RAX
0x00000029 B03C                            MOV AL,0x3C
0x0000002B 0F05                            SYSCALL
0x0000002D E8D0FFFFFF                      CALL 0x00000002
0x00000032 0C06                            OR AL,0x06
0x00000034 0B0D670F231E                    OR ECX,DWORD PTR [0x0000000-0xE1DCF05F]
0x0000003A 07                              ???
0x0000003B 303F                            XOR BYTE PTR [RDI],BH
0x0000003D 20053A043D13                    AND BYTE PTR [0x0000000-0xECC2FB83],AL
0x00000043 092F                            OR DWORD PTR [RDI],EBP
0x00000045 2F                              ???
0x00000046 383C1B                          CMP BYTE PTR [RBX+RBX],BH
0x00000049 07                              ???
0x0000004A 0C25                            OR AL,25
0x0000004C 2E7A22                          HNT  JP 0x00000071
0x0000004F 27                              ???
0x00000050 1002                            ADC BYTE PTR [RDX],AL
0x00000052 090A                            OR DWORD PTR [RDX],ECX
```

See `solution_chal_2_1.py`

`Solution: FLAG-EiTMzujOpNwYCeervQMFod0hmZHC`



# chal_2_2

At first, it looks like the first hex decryption is interesting, but it's just deception that prints "lmfao it isnt that simple".

Then we check `ctfhash` which hashes the user input using this formula: `hash[i] = i + input[i] * 100 - 10`. 
Important to note that hash is an integer!

We can write a simple program to revert the hash. 

See `solution_chal_2_2.py`

`Solution: CTF_kittbyyy :D`
