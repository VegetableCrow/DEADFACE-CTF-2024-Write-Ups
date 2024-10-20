![image](https://github.com/user-attachments/assets/91ef5a73-2361-4919-8718-a742e8e500d4)

The challenge will give us an ELF format file. Download it and ghidra it as usual when you do any Reverse Engineering challenge. 
I will switch between online decompiler and kali ghidra due to the completeness of the decompilation to understand the code
If don't have ghidra, you can use Decompiler Explorer tot use it (https://dogbolt.org/)

After ghidra the file, you will found a function has leak something about a key and a obfuscated string

![image](https://github.com/user-attachments/assets/ad4597e2-2f80-48dd-a12f-a0aaea3c9011)
secret key leak ("my_secret_key") and weird obfuscated string ("\v\x15>\x14\x1e\x16!V&,F\x0eJ\x14T\r@\x13P \x16G;F\t\x16\x01\x04")

Inside the function, you can find a fucntion that does the validation checking for the program( FUN_00102aa1(param_1,local_56,sVar3,sVar2); )
Tracing to the fucntion, we can found their formula for validation checking for a good key aka the flag.
![image](https://github.com/user-attachments/assets/6a5889af-d972-439b-bf55-10ee78a7cb1e)
XOR function 

Based on the XOR function, the for loop will loop thru each byte of the obfuscated string given how long the obfuscated string is.
Then using the secret key to XOR with the obfuscated string.

![image](https://github.com/user-attachments/assets/093d320f-8784-474c-8b3b-30bf8e94fe27)

**FLAG**

flag{uS3Rs-k3y-R3v3Rs3d-lol}


NOTE:
To check if it can access the website with the flag (x-auth-key), you just try it with chrome (with mod header extension) or curl command in kali
![image](https://github.com/user-attachments/assets/c25bf0a4-5529-4157-8b5f-95231a2ed673)
Chrome

![image](https://github.com/user-attachments/assets/51b298b7-cf27-4a4f-97ba-3795020e62f9)
Kali
