This project is a basic implementation of a server with clients, where clients log in to the server using their credentials and are allowed to transfer files from their directories. 
The project was developed using the C programming language with socket connections, following the workflow diagram provided.

Here Server program acts as console with the access to clients directory can perform followiing functions: File transfer from
From C1
From C2
From C3
C1 From C2
C1 From C3
C2 From C1
C2 From C3
C3 From C1
C3 From C2
From the above console we can see that the this project is capable of txt file transfer from server-client and client-client transfer.
the Workflow of server-client and client-client file transfer are as follows:
server-client:

client-client:

In case of client to client file transfer the transferred files arestored in server directory, as “server_copy.txt”, which can beseen using the “ls” command and can be read and editedusing “gedit server_copy.txt” command.
When the same thing happens in client-to-client file transfer,but file is saved as “clientfileCopier.txt“.
