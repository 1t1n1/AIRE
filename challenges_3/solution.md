# chal_3_1

- `solution_chal_3_1_1`: Beautify code using method of your choice (I used browser's built-in beautifier in the developer console)
- `solution_chal_3_1_2`: Give dictionary a meaningful name
- `solution_chal_3_1_3`: Execute first lines (except the last line) and replace dictionary elements with their value
- `solution_chal_3_1_4`: Extract the last line
- `solution_chal_3_1_5`: Replace the entries using the browser's console

### Commmand to automate: 

``` bash
cat solution_chal_3_1_4.js | \
sed -E 's/\(dictionary\)\[ﾟoﾟ\]/'\'\"\''/g' | \
sed -E 's/ﾟεﾟ/'\'return\''/g' | \
sed -E 's/\(dictionary\)\['\'return\''\]/'\'\\\\\''/g' | \
sed -E 's/\\/\\\\/g' | \
sed -E 's/\(c \^ _ \^ o\)/0/g' | \
sed -E 's/\(o \^ _ \^ o\)/3/g' | \
sed -E 's/\(ﾟΘﾟ\)/1/g' | \
sed -E 's/\(ﾟｰﾟ\)/4/g' > solution_chal_3_1_5.js
```

- `solution_chal_3_1_6`: Take the string delimited by `'"'`, execute in console and replace
- `solution_chal_3_1_7`: Replace `\\` with `\` because we needed a second backslash for the previous step
- `solution_chal_3_1_8`: We run the new string on the JS console and get a second JavaScript program remove duplicate `\` from new program.

Final step is to replace `UwU`'s value with `Secwet`'s' and run the program. You get the flag! 

Basically, what the last program does is that it takes a ciphertext and a key and tries to AES-CBC decrypt it. However the first key is wrong so we must correct it.

`Solution: HF-02574f96342c32ce1f641039dceab768`
