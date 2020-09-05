#include <stdio.h>  
#include <Winsock2.h>  
//#pragma comment(lib,"ws2_32.lib")
//#pragma warning(disable:4996)
#include <iostream>
 
char baseCh[1000];
char recvBuf[1000];
int fetch_code(char * baseCh)
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
	
	send(sockClient, baseCh, strlen(baseCh), 0);
	recv(sockClient, recvBuf, 50, 0);
	printf("%s\n", recvBuf);
	send(sockClient, "exit", 4, 0);
 
	closesocket(sockClient);
	WSACleanup();
 	puts("haha");
	return 0;
}

#include "stdafx.h"
#include <stdlib.h>
#include <windows.h>

int main(int argc, char* argv[]){
	freopen("running.txt","w",stdout); 
	char share_file[256] = {0,};
	HANDLE question_handle;

	sprintf(share_file, "Get_Question_%d", GetCurrentProcessId());
	puts(share_file);
	question_handle = OpenFileMappingA(FILE_MAP_ALL_ACCESS,FALSE,share_file);
	if (question_handle == NULL)
	{
//		return 0;
	}

	char * share_memory = (char *)MapViewOfFile(question_handle, FILE_MAP_READ | FILE_MAP_WRITE, 0, 0, 0);
	
	printf("question = %s\n",share_memory);
    strcpy(baseCh,"D:\\DigimonMasters\\Code_AI\\train-origin\\#@P4FX.jpg");
    puts(baseCh);
    fetch_code(baseCh);
    puts("lol");
//	strcpy(share_memory,recvBuf);
	puts("zzz");
	UnmapViewOfFile(share_memory);
	CloseHandle(question_handle);
	return 1;
}

