![image](https://github.com/user-attachments/assets/270c9db9-9e45-449f-8bd6-f53845634bf7)

The challenge says look for product id, and is from a non-compliant Windows host and not his work-provided laptop by Garry Sartoris. 
At first I thought it was RDP but it show up nothing so I check for more detailes from Analyze Protocol Hierarchy
![image](https://github.com/user-attachments/assets/f42fc557-90cc-4d3c-b11f-ad1f6fd071c8)

With this information I start looking through the possible protocols that shows up in the Analyze Protocol Hierarchy and I stumble upon some information when I apply <udp contains "ProductId"> as the filter
And the flag is found
![image](https://github.com/user-attachments/assets/16e5085e-98e6-4626-9994-fde59e0315ff)
![image](https://github.com/user-attachments/assets/68b7b1ee-70a3-48cc-9cb7-d93b924f5d92)

**FLAG**

flag{00326-10000-00000-AA973}
