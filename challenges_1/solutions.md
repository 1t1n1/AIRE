# chal_1_1

Simple `strings` or open program and directly see flag

`Solution: flag-a_small_step_towards_reverse_engineering`



# chal_1_2

First function in main does a checksum of important function to check if it has been modified.

If not, it is executed. Further analysis reveals that this is ROT4 (chars are separated into uppercase and lowercase).

`Solution: caesarcipher`



# chal_1_3

1. Open in ghidra, understand the task
2. Understand that we want to break at `main+213` then jump at `main+223`
3. Open gdb
4. `start`
5. `b *main+213`
6. `c`
7. Input `4` for "Another Surprise..."
8. `set $rip=*main+223`
9. `c`
10. `cat flag.txt`

`Solution: flag-jump_4r0und!`
