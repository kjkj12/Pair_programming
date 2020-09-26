#include<iostream>
#include<queue>
#include<stdlib.h>
using namespace std;

typedef struct node{
	
	int i,j;
	int maze[3][3];
	int is_swap;
	int step;
	string path;
	
}node;

bool is_exist[1000000000] = {0};
queue<node> q;

int num(node n){
	
	int t = n.is_swap;
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			t = t*10 + n.maze[i][j];
		}
	}
	
	return t;
}

int is_ans(node n){
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			if(n.maze[i][j] != i*3+j+1 && n.maze[i][j] ){
				return 0;
			}
		}
	}
	
	return 1;
}

void up(node n){
	if(n.i!=0){
		swap(n.maze[n.i][n.j],n.maze[n.i-1][n.j]);
		if(!is_exist[num(n)]){
			n.path += "w";
			n.i--;
			n.step++;
			is_exist[num(n)] = 1;
			q.push(n);
		}
	} 
}

void down(node n){
	if(n.i!=2){
		swap(n.maze[n.i][n.j],n.maze[n.i+1][n.j]);
		if(!is_exist[num(n)]){
			n.path += "s";
			n.i++;
			n.step++;
			is_exist[num(n)] = 1;
			q.push(n);
		}
	} 
}

void left(node n){
	if(n.j!=0){
		swap(n.maze[n.i][n.j],n.maze[n.i][n.j-1]);
		if(!is_exist[num(n)]){
			n.path += "a";
			n.j--;
			n.step++;
			is_exist[num(n)] = 1;
			q.push(n);
		}
	} 
}

void right(node n){
	if(n.j!=2){
		swap(n.maze[n.i][n.j],n.maze[n.i][n.j+1]);
		if(!is_exist[num(n)]){
			n.path += "d";
			n.j++;
			n.step++;
			is_exist[num(n)] = 1;
			q.push(n);
		}
	} 
}

void print(node n){
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<n.maze[i][j]<<" ";
		}
		cout<<endl;
	}
}

node before;

int main(int argc, char *arg[]){
//	int a[9] = {9, 6, 0, 5, 1, 7, 2, 4, 8};
//	int swap = 7;
//	int from = 6;
//	int to =9;
	int a[9];
	for(int i=1;i<10;i++) a[i-1] = atoi(arg[i]);
	int swap = atoi(arg[10]);
	int from = atoi(arg[11]);
	int to = atoi(arg[12]);
	
	before.step = swap + 1;
	
	node first;
	
	first.is_swap = 0;
	first.step = 0;
	first.path = "";
	
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			first.maze[i][j] = a[i*3+j];
			if(a[i*3+j] == 0){
				first.i = i;
				first.j = j;
			}
		}
	}
	
	is_exist[num(first)] = 1;
	
	q.push(first);
	
	string result = "нч╫А╧Ш";
	
	while(!q.empty()){
		
		node now = q.front();
		q.pop();
		if(is_ans(now)){
			result = now.path;
			//print(now);
			break;
		}
		up(now);
		down(now);
		right(now);
		left(now);
		
		
	}
	
	cout<<result;
	
	return 0;
} 
