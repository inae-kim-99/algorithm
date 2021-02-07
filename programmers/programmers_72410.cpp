#include <string>
#include <vector>
using namespace std;

string solution(string new_id) {
    string answer = "";

    // 1�ܰ�
    string id1 = "";
    for (int i = 0; i < new_id.length(); i++) {
        id1 += tolower(new_id[i]);
    }

    // 2�ܰ�
    string id2 = "";
    for (int i = 0; i < id1.length(); i++) {
        char ch = id1[i];
        if ((ch >= 'a' && ch <= 'z') ||
            (ch >= '0' && ch <= '9') ||
            ch == '-' ||
            ch == '_' ||
            ch == '.') {
            id2 += ch;
        }
    }

    // 3�ܰ�
    string id3 = "";
    bool check = false;
    for (int i = 0; i < id2.length(); i++) {
        if (id2[i] == '.') {
            if (!check) { // �����Ͽ� .�� �ִ� ��찡 �ƴϸ�
                id3 += '.';
                check = true;
            }
        }
        else {
            id3 += id2[i];
            check = false;
        }
    }

    // 4�ܰ�
    string id4 = id3;
    if (id4[0] == '.')
        id4 = id4.substr(1, id4.length() - 1);
    if (id4[id4.length() - 1] == '.')
        id4 = id4.substr(0, id4.length() - 1);

    // 5�ܰ�
    string id5 = "";
    if (id4.length() == 0)
        id5 = "a";
    else
        id5 = id4;

    // 6�ܰ�
    string id6 = id5;
    if (id5.length() >= 16) {
        if (id5[14] == '.')
            id6 = id5.substr(0, 14);
        else
            id6 = id5.substr(0, 15);
    }

    // 7�ܰ�
    string id7 = id6;
    int len6 = id6.length();
    if (len6 <= 2) {
        int endChar = id6[len6 - 1];
        int repeat = 3 - len6;
        for (int i = 0; i < repeat; i++) {
            id7 += endChar;
        }
    }

    answer = id7;

    return answer;
}