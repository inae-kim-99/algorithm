#include <iostream>
#include <vector>
#include <string>
using namespace std;

string checkStr(string str) {
	vector<char> v;
	// 열기 -> 저장, 닫기 -> 마지막으로 연 괄호와 일치하는지 확인
	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '(' || str[i] == '[') { // 괄호 닫기
			v.push_back(str[i]);
		}
		else if (str[i] == ')') { // 괄호 닫기
			if (v.size() > 0 && v.back() == '(')
				v.pop_back();
			else
				return "no";
		}
		else if (str[i] == ']') { // 괄호 닫기
			if (v.size() > 0 && v.back() == '[')
				v.pop_back();
			else {
				return "no";
			}
		}
	}
	if (v.size() == 0)
		return "yes";
	else
		return "no";
}

int main() {
	vector<string> answer;
	while (true) {
		string str = "", input;
		// 한 문장 읽기
		while (true) {
			getline(cin, input);
			str += input;
			if (input[input.length() - 1] == '.')
				break;
		}
		if (str == ".")
			break;
		// 문장 검사
		answer.push_back(checkStr(str));
	}
	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i] << endl;
	}

	return 0;
}