
#include <stdio.h>
#include <string.h>
 
#include "osapi/osapi.h"
 
int main()
{
	// ??Socket
	OS_TcpSocket client_sock;
	client_sock.Open();
 
	// ?????
	OS_SockAddr serv_addr("127.0.0.1", 4444);
	if(	client_sock.Connect( serv_addr ) < 0)
	{
		printf("???????!\n");
		return -1;
	}
 
	char buf[1024];
 
	// ????
	strcpy(buf, "help me");
	int n = strlen(buf);
	client_sock.Send(buf, n);
 
	// ????
	n = client_sock.Recv(buf, sizeof(buf));
	buf[n] = 0;
	printf("Got: %s \n", buf);
 
	// ??Socket
	client_sock.Close();
	return 0;
}
