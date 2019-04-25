class Node:  # 각 노드의 객체로 사용될 class
    def __init__(self, year):
        self.year = year
        self.link = None

class LinkedList:
    def __init__(self):  # class 생성 시 가장 처음 실행되는 함수
        self.dummy = Node("NULL")  # 마지막 Node를 NULL로 지정
        self.head = self.dummy  # head가 NULL를 가리키도록 초기화

    def insert(self, idx, year):  # 입력 함수
        newNode = Node(year)  # 새로 만든 노드
        if idx == 0:  # linked list의 맨 앞에 추가
            newNode.link = self.head  # 새 노드의 link를 head로 지정
            self.head = newNode  # linked list의 head가 새 노드를 가리키도록 지정
        elif idx == -1:  # 맨 마지막에 노드를 추가하는 경우
            temp = self.head
            if temp.link == None: # linked list가 비었을 경우
                self.insert(0, year)  # 맨 앞에 추가
                return 0  # 함수 종료
            while temp.link.link != None:  # linked list의 끝 부분(dummy 이전) 나올 때까지 반복
                temp = temp.link  # 다음 노드로 이동
            newNode.link = temp.link  # temp.link는 NULL를 가리키는 포인터
            temp.link = newNode  # 마지막 노드에 새로 만든 노드 이어줌
        else:  # 처음과 끝 사이의 특정 index에 추가하는 경우
            temp = self.head
            for _ in range(idx-1):
                temp = temp.link  # idx-1 만큼 link를 타고 이동
            newNode.link = temp.link  # 새로운 노드를 temp의 link로 연결
            temp.link = newNode  # temp와 새 노드를 이어줌

    def remove(self, idx):
        temp = self.head
        if idx == 0:  # 맨 앞 노드 삭제
            self.head = self.head.link
        elif idx == -1:  # 맨 뒤 노드 삭제
            while temp.link.link != self.dummy:  # 뒤에서 두번째 노드에서 멈춰야 마지막 노드 삭제 가능
                temp = temp.link
            temp.link = self.dummy  # 뒤에서 두번쨰 노드에서 마지막 노드 참조를 지움
        else:
            for _ in range(idx-1):
                temp = temp.link  # idx-1만큼 link를 타고 이동
            temp.link = temp.link.link

    def search(self, idx):  # index로 검색해서 year값 print하는 함수
        temp = self.head
        if idx == -1:  # 맨 마지막
            while temp.link != self.dummy:  # linked list의 끝 부분(dummy 이전) 나올 때까지 반복
                temp = temp.link
        for _ in range(idx):
            temp = temp.link  # idx 만큼 linked list를 타고 검색
        print(temp.year)  # 출력

    def print_all(self):
        temp = self.head
        print(temp.year)
        while temp.link != None:  # 끝 Node에 도달할 때까지 반복
            temp = temp.link
            print(temp.year)
        print("\n")

if __name__ == "__main__":  # 메인함수
    L = LinkedList()
    inp = 0
    while inp != 5:
        print("\n메뉴를 선택하세요")
        print("1. 노드 추가")
        print("2. 노드 삭제")
        print("3. 노드 검색")
        print("4. 노드 출력")
        print("5. 종료")
        inp = int(input())
        print('')
        if inp == 1:
            print("노드 추가 위치를 입력하세요 (0은 맨앞, -1은 맨뒤)")
            idx = int(input())
            print("year값을 입력하세요")
            year = int(input())
            L.insert(idx, year)
        elif inp == 2:
            print("삭제할 노드의 위치를 입력하세요 (0은 맨앞, -1은 맨뒤)")
            idx = int(input())
            L.remove(idx)
        elif inp == 3:
            print("검색할 노드의 위치를 입력하세요 (0은 맨앞, -1은 맨뒤)")
            idx = int(input())
            L.search(idx)
        elif inp == 4:
            L.print_all()

