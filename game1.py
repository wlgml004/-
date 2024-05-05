from random import choice
import time
import random


#글자 한글자씩 출력해주는 함수
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.08)

#스탯
total_brain = 10
total_health = 50
total_stress = 5
total_code = 0
total_money = 50

#교수님 호감도
total_proheart1 = 0
total_proheart2 = 0

#스챗 증감들
def brain(amount):
    global total_brain
    if 0 <= total_brain <=999:
        total_brain += amount

def health(amount):
    global total_health
    if total_health >0:
        total_health += amount
    elif total_health <= 0:
        death()

def stress(amount):
    global total_stress
    if total_stress + amount < 0:
        fix_stress()
    elif total_stress + amount >=0:
        total_stress += amount
        if total_stress >= 100:
            death()
    #스트레스가 0이하로 내려가지 않게 하는 코드
def fix_stress():
    global total_stress
    total_stress = 0

    
def code(amount):
    global total_code
    if 0 <= total_code <= 999:
        total_code += amount
    

def money(amount):
    global total_money
    if total_money >=0:
        total_money += amount

    #교수님 호감도 증감

    #박교수님 호감도
def proheart1():
    global total_proheart1, total_brain, total_code
    if total_proheart1 >= 0:
        plus1 = random.randint(1, 5)
        total_proheart1 += plus1
        return plus1

    #김교수님 호감도
def proheart2():
    global total_proheart2, total_brain, total_code
    if total_proheart2 >= 0:
        plus2 = random.randint(5, 10)
        total_proheart2 += plus2
        return plus2

    #게임 진행하는 코드
def main():
    start_game()
    choice = input("< 시작하기(y)\n")

    if (choice == 'y'):
    
        start_intro()
        main_menu()
    else:
        def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.08)
        print_slow("시작하기 싫으세요?\n")
        main()

    #스트레스 100이상일때 게임오버
def death():
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
    print_slow("준영이는 스트레스로 병에 걸려 생을 마감했습니다...\n")
    print_slow("농담이고요. 당신이 준영이를 혹사시켜서 자퇴했습니다.\n")
    print_slow("하하 이것도 농담이에요. 준영이는 안좋은 선택을 했어요. 당신, 때문에.\n")
    print_slow("이거 다 거짓말인거 아시죠? 아무튼 준영이는 더 이상 무리 ㅠ3ㅠ\n")
    print_slow("다음에는 열심히 해보세요. 당신의 이야기는 여기까지. 바이바이")
    exit()

  #게임시작프린트
def start_game():
    def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.15)
    print_slow("<두근 두근 러브 학점 시물레이션>\n")
    print_slow("     ver. 교수님과의 러브러브 만남\n")
    
    #인트로와,인트로 한글자씩 출력해주는 코드
def start_intro():
    dialogues = [ 
        "준영이 : 아 큰일났다 망했다 아 시험 어떡하지 \n"
        "수뭉이요정 : 힘들어하는 준영이의 목소리를 듣고 요정 등장 ! \n"
        "준영이 : 아 깜짝아 아 뭐야 아 이게 뭐지 벌레인가 \n"
        "수뭉이요정 : 준영아! 걱정마! 내가 첫날로 시간을 되돌려줄게 \n"
        "준영이 : 아 진짜 아 진짜 그러면 좋겠다 \n"
        "수뭉이요정 : 웅 ! \n"
        "준영이 : 어어? 갑자기 머리가 (시야가 핑 돈다)\n"
        "준영이 : 아 안돼 시험 망치고 죽다니...(털석)\n"
        "수뭉이요정 : 후후...이번엔 열심히해 준영아 ! \n"
        "이 때 들은 말을 끝으로 나는 정말로 입학 첫날로 돌아왔다 \n"
        "준영이 : 수뭉이는... 실존했구나. 사랑해요 상명대 ! \n\n"
   ]
    for dialogue in dialogues:
        for char in dialogue:
            print(char,end='', flush = True)
            time.sleep(0.08)

    #인트로 후 메인메뉴
def main_menu():
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.08)
    print("-----메인 메뉴-----")
    print("> 스케쥴 표 (a)\n")
    print("> 교수님 만나기 (s)\n")
    print("> 자판기 (d)\n")
    print("> 스탯 확인 (f)")
    print("------------------")
    choice = input("무엇을 하시겠습니까? : \n")
    if choice == 'a':
        schedule()
    elif choice == 's':
        professor()
    elif choice == 'd':
        store()
    elif choice == 'f':
        status()
    else:
        print_slow("제대로 선택 하세요.\n")
        main_menu()

    #스케쥴 메뉴
def schedule():
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.08)

    print_slow("준영이의 세 달을 정해주세요 !\n")
    while True:
        choice = input("메뉴로 돌아가기(1): \n")
        if choice == '1':
            main_menu()
            break
        else:
            def print_slow(text):
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.08)
            print_slow("제대로 입력하시라고요.\n")
    
    #교수만나기메뉴
def professor():
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.08)
    print("------연구실 앞------")
    print("> 김교수님 만나러 가기 (1)\n")
    print("> 박교수님 만나러 가기 (2)\n")
    print("메누로 돌아가기 (3)\n")
    print("--------------------")
    choice = input("무엇을 하시겠습니까? : \n")

    #교수님 선택
    if choice == '1':
        professor1()

    elif choice == '2':
        professor2()
    elif choice == '3':
        main_menu()
    else:
        print_slow("다시 입력하세요. 제발.\n")
        professor()

    #박교수님 선택
def professor1():
    def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.08)
    print_slow("준영이 : 박교수님 계세요?\n")
    if brain(10) >= 10:
        print_slow("아 준영이 안녕~")
        print_slow("1. 그냥요")
        print_slow("2. 상담하고 싶은게 있어서 왔어요")

        choice = input("어떤 대답을 할까? :\n")
        if choice == '1':
            print_slow("\"그러니. 내가 좀 바빠서 미안해 ㅠㅠ.\"")
        elif choice == '2':
            print_slow("\"아이고 그렇구나 잠시만, 여기 앉으면 돼\"")
            print_slow("준영이와 박교수님은 재밌게 대화를 나눴다")
            like1 = professor1()
            print(f"박교수님의 호감도가 {like1} 올랐다")
        else:
            print_slow("진짜 그럴거에요?")
            professor1()
        
    elif brain < 10:
        print_slow("박소영 교수님은 자리에 안계시는 것 같다.")
        professor()


    #김교수님 선택
def professor2():
    def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.08)
    print_slow("준영이 : 김교수님 계세요?\n")

    if brain(20) >= 20 and code(20) >= 20:
        print_slow("\"그래 어떤일로 왔니\"\n")
        print_slow("1. 그냥요\n")
        print_slow("2. 상담하고 싶은게 있어서 왔어요\n")

        choice = input("어떤 대답을 할까? :\n")
        if choice == '1':
            print_slow("\"그래? 할 말 없으면 이만 가자. 바쁘다 바뻐.\"")
        elif choice == '2':
            print_slow("\"그래? 여기 앉아봐, 뭐 상담 하려고\"")
            print_slow("준영이와 김교수님은 재밌게 대화를 나눴다")
            like2 = professor2()
            print(f"김교수님의 호감도가 {like2} 올랐다")
        else:
            print_slow("진짜 그럴거에요?")
            professor2()
    
    elif brain < 20 and code > 20:
        print_slow("김석규 교수님은 자리에 안계시는 것 같다.")
        professor()

    #자판기 메뉴
def store():
    global total_money
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.09)
    
    if total_money >= 5:
        print_slow(" 무엇을 마시던 상상이상!! 구매하지 않으면 불행이 옵니다.\n")
        print("----------------------자 판 기-------------------------")
        print("> 1. 맛이 좋은 초록 이슬 (5원) \n")
        print("       [스트레스 -20, 지능 -5]\n")
        print_slow("      -마시면 기분이 좋아집니다-\n")
        print("> 2. 스x피 커피우유 (10원) \n")
        print("       [스트레스 +5, 지능 +10]\n")
        print_slow("      -저런...잠을 잘자야 키가 커 준영아-\n")
        print("> 3. 맛이 좋지 않은 사약 한 접시 (15원) \n")
        print("       [스트레스 +10, 체력 +20]\n")
        print_slow("      -사약은 몸에 좋은 재료로 이루어져 있다는 사실-\n")
        print("> 4. 딸기 맛이 나는 해열제 (10원)\n")
        print("      [스트레스 -20]\n")
        print_slow("      -준영아 힘내! 아프지마 유유.-\n")
        print("> 5. 색이알록달록한버섯을우린물 (25원) \n")
        print("       [스트레스 -10, 코딩실력 +10, 지능 +10, 체력 -20]\n")
        print_slow("      -히히...이거 마시면 나도 코딩을...-\n")
        print("------------------------------------------------------")

    elif total_money <= 4:  
        print_slow("돈도 없으면서 뭘 사시려고요 ? 가서 돈벌어와\n")
        main_menu()

    #자판기 메뉴선택
    choice = input("무엇을 드시겠어요? 설마 아무것도 마시지 않는건 아니시죠? (y/n) \n")
    if choice == '1':
        if total_money >= 5:
            print("<스트레스가 해소되고 지능이 떨어졌다 !>\n")
            print_slow("-이슬은 아이셔가 맛있는데-\n")
            stress(-20)
            brain(-5)
            money(-5)
            main_menu()
        elif total_money <= 4:
            print_slow("<소지금이 부족합니다...[거-지]>\n")
            store()

    elif choice == '2': 
        if total_money >= 9:
            print("<스트레스를 받고 지능이 올라갔다 !>\n")
            print_slow("-공부 화이팅... 카페인은 조금만-\n")
            stress(5)
            brain(10)
            money(-10)
            main_menu()
        elif total_money <= 9:
            print_slow("<소지금이 부족합니다...[거-지]>\n")
            store()

    elif choice == '3':
        if total_money >= 15:
            print("<스트레스를 받고 체력이 올라갔다 !>")
            print_slow("-우웩 너무 맛없어!! 하지만 먹는건 준영이다 화이팅! >o<- \n\n")
            stress(10)
            brain(-20)
            money(-15)
            main_menu()
        elif total_money <= 14:
            print_slow("<소지금이 부족합니다...[거-지]>\n")
            store()
        
    elif choice == '4':
        if total_money >=10:
            print("<스트레스가 해소되었다 !>")
            print_slow("-아플때까지 공부하지는 말기로 ㅜㅅㅜ- \n\n")
            stress(-20)
            money(-10)
            main_menu()
        elif total_money <= 9:
            print_slow("<소지금이 부족합니다...[거-지]>\n")
            store()
    elif choice == '5':
        if total_money >= 25:
            print("<스트레스가 해소되고 체력이 떨어지고 코딩실력과 지능이 올라갔다 !>\n")
            print_slow("-코딩 능력자가 되기 위해서는 뭐든 할 수 있어...-\n\n")
            stress(-10)
            brain(10)
            code(10)
            health(-20)
            money(-25)
            main_menu()
        elif total_money <= 24:
            print_slow("<소지금이 부족합니다...[거-지]>\n")
            store()
        
    elif choice == 'y':
        def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.15)
        choice = input("무엇을 드시겠어요? 설마 아무것도 마시지 않는건 아니시죠? (y/n) \n")
        if choice == 'y':
            print_slow("아무것도 사지 않으시겠다고요? \n")
            print_slow("그렇다면... <가지> 를 강제로 먹이겠습니다.\n")
            print_slow("스트레스를 1 받았다. 우웩 \n")
            stress(1)
            main_menu()
            def print_slow(text):
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.08)
                
        elif choice == 'n':
            print_slow("감사합니다! 자판기 숫자를 선택해서 구매하시면 됩니다! \n")
            store()
        else:
            print("뭐하세요? 뭐든 하세요.\n")
            store()

    #스탯 메뉴 
def status():
    print("---------스탯---------")
    print("지능:",total_brain)
    print("체력:",total_health)
    print("스트레스:",total_stress)
    print("코딩실력:",total_code)
    print("소지금:",total_money)
    print("박교수님 호감도:",total_proheart1)
    print("김교수님 호감도:",total_proheart2)
    print("-------------------")

    while True:
        def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.08)
        choice = input("메뉴로 돌아가기 (1): \n")
        if choice == '1':
            main_menu()
            break
        else:
            print_slow("제대로 입력하시라고요.\n")



    


    #main 코드만 실행되게하는 코드(name은 현재 진행중인 코드를 뜻함)
if __name__ == "__main__":
        main()