#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

void main(void){

	int fd, con, sin_size;
	char str[100];
	struct sockaddr_in server;

	if ((fd=socket(AF_INET, SOCK_STREAM, 0)) == -1 ){
    		printf("socket() error\n");
    		exit(-1);
  	}

  	server.sin_family = AF_INET;
  	server.sin_port = htons(6000);
  	server.sin_addr.s_addr = inet_addr("127.0.0.1");

	connect(fd ,(struct sockaddr *)&server ,sizeof(server));

  	while(1){
  		printf("Enter a string\n");
  		gets(str);
  		send(fd,str,sizeof(str),0);
  	}

  	close(fd);

}
