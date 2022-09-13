UDP vs TCP Questions:

Question 1: How did the reliability of UDP change when you added 50% loss to your local environment? Why did this occur?

The number of packets that the server was able to receive decreased by about 50%, as UDP does not have any failsafe 
or reliability to resubmit a packet that was dropped.

Question 2: How did the reliability of TCP change? Why did this occur?

TCP had a much greater reliability, as the files were able to be resent if they were not properly received by the 
server. This is due to the socket that connected the two communicating ports, and the failsafes build into the 
message/packet to assist in flagging and resubmiting dropped packets.

Question 3: How did the speed of the TCP response change? Why might this happen?

TCP was slower than the UDP counterpart, mainly due to the fact that the messages/packets being sent were much bigger 
due to the additional information required for TCP to operate.

--------------------------------------------------------------------

tcp_server.c Questions:

Question 1: What is argc and *argv[]?

They are the arguments for main, and are filled in by the strings/values input on the command line after the command to run the executable.
argc is the number of arguments, while *argv[] is an array of strings that holds the characters that make up each argument, with argv[0] being
the executable command.

Question 2: What is a UNIX file descriptor and file descriptor table?

A UNIX file descriptor is a unique identifier or handle for a file or I/O resource, like a socket. The file descriptor table is a map of file 
descriptors to functions that are carried out, like reading a file, writing a new file, removing a file, etc.

Question 3: What is a struct? What's the structure of sockaddr_in?

A struct is like a simple class that has public data members by default; a way to group several related variables into one place and under one 
variable name. The sockaddr_in's structure is storing the IP address of the server and the the client in that order, which can be reference with 
dot notation and will be critical with the TCP message structure requiring both of those pieces of information.

Question 4: What are the input parameters and return value of socket()? 

The input parameters of socket() are the communications domain/address, the type of socket to be created, and the communciations protocol that 
will be employed. The return value is either a negative number to signal an error occured or the socket's file descriptor.

Question 5: What are the input parameters of bind() and listen()?

The bind() function has the input parameters of the socket's file descriptor, the address, and the address's length of the socket with 
which you want to bind to. The listen() function has the input parameters of the socket you want to listen on and the length of the 
listening queue for said socket (i.e. how many responses do you want to listen for).

Question 6: Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?

Since the port is open to receiving packets and is actively listening for them at all times, we use a while (1) loop to automatically set the 
code back into a state where it can receive the next packet after it is done with processing the first packet. If there are multiple 
simultaneous connections to this port that is listening for packets, then the first one to arrive would be processed, and during the 
processing any other packets that arrive would be lost. Only after the program is finished processing a packet can it listen and accept more, 
and by then the packet may have already been lost.

Question 7: Research how the command fork() works. How can it be applied here to better handle multiple connections?

The fork() command works to allow multiple segments of the same code to run essentially side by side. By calling the fork() command, you 
create a child and parent process that each have different process IDs. With this, you could have the port listen for a packet, and as soon as 
one is found, call fork(). The parent process would then continue to listen on the port, using an if statement to check if the process ID 
(pid) matches that of the parent and then running continue. The child process would fail this check, and would go on to process the packet. 
This would allow for a greater amount of packets to be processed, as fewer would get lost during the processing segment of the code.

Question 8: This program makes several system calls such as 'bind', and 'listen.' What exactly is a system call?

A system call is an interaction between the code/program and the operating system of the machine it is running on. When you call bind() 
or listen(), the program is then interacting with the OS to directly configure and receive information from the communication ports, which 
are a part of the OS. These system calls directly give instructions to the OS and its registers, rather than being confinded to the scope of 
the current code.