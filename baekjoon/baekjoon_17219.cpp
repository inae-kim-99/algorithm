// https://www.acmicpc.net/problem/17219

#include <iostream>
#include <string>
#include <map>
using namespace std;
int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int siteNum, findNum;
	cin >> siteNum >> findNum;

	map<string, string> m;
	
	// N개의 사이트 주소와 비밀번호
	for (int i = 0; i < siteNum; i++) {
		string site, password;
		cin >> site >> password;
		m[site] = password;
	}

	// M개의 찾으려는 비밀번호의 사이트 주소
	for (int i = 0; i < findNum; i++) {
		string findSite;
		cin >> findSite;
		map<string, string>::iterator it = m.find(findSite);
		if (it != m.end()) {
			cout << it->second << "\n";
		}
	}

	return 0;
}