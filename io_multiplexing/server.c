//IO multiplexing
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/select.h>
#define PORT 6000
#define BACKLOG 5
void main(void){

	int fd, fd1[5], sin_size , max_fd ,ret , i=0,j;char str[100];struct sockaddr_in server,client;fd_set read_fd,curr_fd;struct timeval timeout;
  	FD_ZERO(&read_fd);
	  if ((fd=socket(AF_INET, SOCK_STREAM, 0)) == -1 ){printf("socket() error\n");exit(-1);}
	  server.sin_family = AF_INET;server.sin_port = htons(PORT);server.sin_addr.s_addr = inet_addr("127.0.0.1");
	  if(bind(fd,(struct sockaddr *)&server,sizeof(struct sockaddr_in))==-1){printf("bind error\n");exit(-1);}
	  if(listen(fd,BACKLOG) == -1){printf("listen error\n");exit(-1);}
	  FD_SET(fd,&read_fd);
  max_fd = fd + 1;
  sin_size=sizeof(struct sockaddr_in);
  while(1){
        timeout.tv_sec = 10;timeout.tv_usec = 0;curr_fd = read_fd;
        ret = select(max_fd,&curr_fd,NULL,NULL,&timeout);
        if(ret==-1)
                printf("Select Error\n");
        else if(ret==0)
                printf("Timeout\n");
        else{
                if(FD_ISSET(fd,&curr_fd)){
                        fd1[i] = accept(fd,(struct sockaddr *)&client,&sin_size);
                        if(fd1[i]==-1){
                                printf("accept error\n");
                        }
                        else{
                                printf("You got a connection from %s\n",inet_ntoa(client.sin_addr));
                                FD_SET(fd1[i],&read_fd);
                                //curr_fd = read_fd;
                                if(fd1[i]>=max_fd)
                                        max_fd=fd1[i]+1;
                                i++;
                        }
                }
                //ret = select(max_fd,&curr_fd,NULL,NULL,&timeout);
                for(j=0;j<i;j++){
					if(FD_ISSET(fd1[j],&curr_fd)){
							recv(fd1[j],str,sizeof(str),0);printf("Client Said %s\n",str);
					}
				}
        }
  }
     close(fd);
 }
