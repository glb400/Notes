#include<iostream>
#include<algorithm>
#include <cstring>
using namespace std;
const int Max = 65;

 

int n, len, stick[Max];
bool flag, vis[Max];

 

bool cmp(int a, int b){
    return a > b;
}

 

void dfs(int dep, int now_len, int u){   // depΪ��ǰ�ѱ��ù���С������uΪ��ǰҪ�����С����
    if(flag) return;
    if(now_len == 0){                    //  ��ǰ����Ϊ0��Ѱ����һ����ǰ�С����
        int k = 0;
        while(vis[k]) k ++;              //  Ѱ�ҵ�һ����ǰ�С����
        vis[k] = true;
        dfs(dep + 1, stick[k], k + 1);
        vis[k] = false;
        return;
    }
    if(now_len == len){                  //  ��ǰ����Ϊlen������ƴ�ճ���һ��ԭ����
        if(dep == n) flag = true;        //  ��ɵı�־�����е�n��С������ƴ���ˡ�
        else dfs(dep, 0, 0);
        return;
    }
    for(int i = u; i < n; i ++)
        if(!vis[i] && now_len + stick[i] <= len){
            if(!vis[i-1] && stick[i] == stick[i-1]) continue;      //  ���ظ�����������Ҫ�ļ�֦��
            vis[i] = true;
            dfs(dep + 1, now_len + stick[i], i + 1);
            vis[i] = false;
        }
}

 

int main(){
    while(scanf("%d", &n) && n != 0){
        int sum = 0;
        flag = false;
        for(int i = 0; i < n; i ++){
            scanf("%d", &stick[i]);
            sum += stick[i];
        }
        sort(stick, stick + n, cmp);     //  �Ӵ�С����
        for(len = stick[0]; len < sum; len ++)
            if(sum % len == 0){          //  ö���ܱ�sum�����ĳ��ȡ�
                memset(vis, 0, sizeof(vis));
                dfs(0, 0, 0);
                if(flag) break;
            }
        printf("%d\n", len);
    }
    return 0;
}
