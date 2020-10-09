#include<iostream>
#include<queue>
#include<string.h>
#include<stdlib.h>
using namespace std;

typedef struct node{
	
	int i,j;
	int maze[3][3];
	int step;
	string path;
	int si,sj;
	
}node;

bool is_exist[1000000000] = {0};
queue<node> q;

queue<node> ready_swap;

int num(node n){
	
	int t = 0;
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
	
	cout<<n.i<<" "<<n.j<<endl;
}

node force_swap(node a,int from,int to){
	if(a.maze[from/3][from%3] == 0){
		a.i = to/3;
		a.j = to%3;
	}else if(a.maze[to/3][to%3] == 0){
		a.i = from/3;
		a.j = from%3;
	}
	swap(a.maze[from/3][from%3],a.maze[to/3][to%3]);
	return a;
}

string full(node n,int swap){
	
	swap = (swap - n.step)/2;
	
	string tmp = "";
	
	if(n.i != 2) tmp = "sw";
	else tmp = "ws";
	
	string res = "";
	while(swap--){
		res += tmp;
	}
	
	return n.path + res;
}

int main(int argc, char *arg[]){
//	int a[9] = {5, 9, 1, 4, 8, 3, 0, 2, 7};
//	int swap = 19;
//	int from = 9;
//	int to = 1;
	int a[9];
	for(int i=1;i<10;i++) a[i-1] = atoi(arg[i]);
	int swap = atoi(arg[10]);
	int from = atoi(arg[11]);
	int to = atoi(arg[12]);
	from--;
	to--;
	
	node first;
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
	
	q.push(first);
	
	is_exist[num(first)] = 1;
	
	string result = "无结果";
	
	int yu = swap%2;
	
	while(!q.empty()){
		
		node now = q.front();
		q.pop();
		
		if(now.step%2 == yu){
			ready_swap.push(now);
		}
		
		if(is_ans(now)){
			result = now.path;
			break;
		}
		
		if(now.step == swap){
			continue;
		}
		
		up(now);
		down(now);
		right(now);
		left(now);
	}
	
	if(result != "无结果"){
		cout<<result;
		return 0;
	}
	
	int q_size = ready_swap.size();
	
	node tmp;
	for(int i = 0; i < q_size; i++) {
		tmp = ready_swap.front();
		if(tmp.step != swap){
			tmp.path = full(tmp,swap);
			tmp.step = swap;
		}
		tmp = force_swap(tmp,from,to);
		ready_swap.push(tmp);
		q.push(tmp);
		ready_swap.pop();
   } 
   
   memset(is_exist,0,sizeof(bool)*1000000000);
   
   while(!q.empty()){
		
		node now = q.front();
		q.pop();
		
		if(is_ans(now)){
			result = now.path;
			if(now.step == swap){
				result += "w";
			}
			break;
		}
		up(now);
		down(now);
		right(now);
		left(now);
	}
	
	if(result != "无结果"){
		cout<<result;
		return 0;
	}
	
	node tem;
	for(int i = 0; i < q_size; i++) {
		tmp = ready_swap.front();
		for(int j = 0; j < 8; j++){
			for(int k = j+1; k < 9; k++){
				tem = force_swap(tmp,j,k);
				tem.si = j+1;
				tem.sj = k+1;
				q.push(tem);
			}
		}
      
      ready_swap.pop();
   } 
	
	while(!q.empty()){
		
		node now = q.front();
		q.pop();
		
		if(is_ans(now)){
			tmp = now;
			if(now.step == swap){
				tmp.path += "w";
			}
			break;
		}
		up(now);
		down(now);
		right(now);
		left(now);
	}
	
	cout<<tmp.path<<",";
	cout<<tmp.si<<",";
	cout<<tmp.sj;
	
	return 0;
} 
