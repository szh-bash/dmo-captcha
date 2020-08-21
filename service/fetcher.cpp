#include <cstdio>  
#include <Winsock2.h>  
#pragma comment(lib,"ws2_32.lib")
#pragma warning(disable:4996)
#include <iostream>
 
int fetch_code()
{
	WORD wVersionRequested;
	WSADATA wsaData;
	int err;
 
	wVersionRequested = MAKEWORD(1, 1);
 
	err = WSAStartup(wVersionRequested, &wsaData);
	if (err != 0) {
		return -1;
	}
 
	if (LOBYTE(wsaData.wVersion) != 1 ||
		HIBYTE(wsaData.wVersion) != 1) {
		WSACleanup();
		return -1;
	}
	SOCKET sockClient = socket(AF_INET, SOCK_STREAM, 0);
 
	SOCKADDR_IN addrSrv;
	addrSrv.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");
	addrSrv.sin_family = AF_INET;
	addrSrv.sin_port = htons(4444);
	connect(sockClient, (SOCKADDR*)&addrSrv, sizeof(SOCKADDR));
	
	char baseCh[100];
	scanf("%s", baseCh);
	send(sockClient, baseCh, strlen(baseCh), 0);
	char recvBuf[500];
	recv(sockClient, recvBuf, 50, 0);
	printf("%s\n", recvBuf);
	send(sockClient, "exit", 4, 0);
 
	closesocket(sockClient);
	WSACleanup();
 
	getchar();
	return 0;
}
int main(){
	
	fetch_code();
	return 0;
}

