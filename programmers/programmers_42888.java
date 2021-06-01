// https://programmers.co.kr/learn/courses/30/lessons/42888
// 프로그래머스 42888번 : 2019 KAKAO BLIND RECRUITMENT - 오픈채팅방

import java.util.HashMap;

public class programmers_42888 {

    public static String[] solution(String[] record) {
        int len = record.length;
        int ENTER = 0, LEAVE = 1, CHANGE = 2;
        HashMap<String, String> userMap = new HashMap<>(); // MAP : Id, Nickname
        String[] userID = new String[len];
        Integer[] userPerform = new Integer[len]; // Enter(0) or Leave(1) or Change(2)

        int EnterAndLeave = 0; // ENTER, LEAVE 횟수
        for (int i = 0; i < len; i++) {
            String[] command = record[i].split(" ");
            if (command[0].equals("Enter")) {
                userMap.put(command[1], command[2]);
                userPerform[i] = ENTER;
                EnterAndLeave++;
            } else if (command[0].equals("Change")) {
                userMap.put(command[1], command[2]);
                userPerform[i] = CHANGE;
            } else { // Leave
                userPerform[i] = LEAVE;
                EnterAndLeave++;
            }

            userID[i] = command[1];
        }

        String[] answer = new String[EnterAndLeave];
        String[] perform = {"들어왔습니다.", "나갔습니다."};
        int count = 0;
        for (int i = 0; i < len; i++) {
            if (userPerform[i] != CHANGE) {
                answer[count++] = userMap.get(userID[i]) + "님이 " + perform[userPerform[i]];
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"};
        solution(record);
    }

}
