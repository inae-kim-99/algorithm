#include <iostream>
#include <vector>
#include <string>
using namespace std;

string checkStr(string str) {
	vector<char> v;
	// ���� -> ����, �ݱ� -> ���������� �� ��ȣ�� ��ġ�ϴ��� Ȯ��
	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '(' || str[i] == '[') { // ��ȣ �ݱ�
			v.push_back(str[i]);
		}
		else if (str[i] == ')') { // ��ȣ �ݱ�
			if (v.size() > 0 && v.back() == '(')
				v.pop_back();
			else
				return "no";
		}
		else if (str[i] == ']') { // ��ȣ �ݱ�
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
		// �� ���� �б�
		while (true) {
			getline(cin, input);
			str += input;
			if (input[input.length() - 1] == '.')
				break;
		}
		if (str == ".")
			break;
		// ���� �˻�
		answer.push_back(checkStr(str));
	}
	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i] << endl;
	}

	return 0;
}