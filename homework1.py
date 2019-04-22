from time import time

if __name__ == "__main__":  # main 함수, 프로그램 구동시 제일 처음으로 시작됨
    array = [None for _ in range(100000)]  # None으로 초기화된 100000개 크기의 list 선언
    while True:  # 인터페이스 반복
        print("메뉴를 선택하세요")
        print("1. 원소 검색")
        print("2. 원소 추가")
        print("3. 원소 삭제")
        print("4. 배열 원소 출력")
        print("5. 종료")
        inp = int(input())  # 입력 받음
        if inp == 1:
            print("index를 입력하세요")
            idx = int(input())  # index 입력 받은 뒤 정수형으로 변환
            t = time()  # 시작시각 저장
            print(array[idx])
            print("검색에 걸린 시간 :", time()-t)  # 작업 수행 후 시각과 뺄셈하여 걸린시간 측정
        elif inp == 2:
            print("원소 추가 위치를 지정하세요 (0은 맨앞, 99999는 맨 뒤)")
            idx = int(input())
            print("저장할 데이터를 입력하세요")
            inp = input()
            t = time()
            array[idx] = inp  # index 위치의 원소를 입력데이터로 지정
            print("삽입에 걸린 시간 :", time()-t)
        elif inp == 3:
            print("원소 삭제 위치를 지정하세요 (0은 맨앞, 99999는 맨 뒤)")
            idx = int(input())
            t = time()
            array[idx] = None  # 삭제 시 None으로 원소 내용 초기화
            print("삭제에 걸린 시간 :", time()-t)
        elif inp == 4:
            t = time()
            for idx, element in enumerate(array):  # array 배열에 대해, idx는 순서 / element는 원소 내용
                if element != None:  # 원소 내용이 None이 아니면 idx와 내용 출력
                    print("idx", idx, ":", element)
            print("원소 출력에 걸린 시간 :", time()-t)
        elif inp == 5:
            break  # 입력이 5이면 반복문 종료
