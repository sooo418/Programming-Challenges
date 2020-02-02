max_word = 1000
num_ram = 1000
num_register = 10

reg = list()
ram = list()
# 케이스 입력
num_case = int(input())
print('')

while num_case > 0:
    # 명령어 입력
    instruction = input()
    while instruction != '':
        ram.append(int(instruction))
        instruction = input()
    # 램 초기화
    for i in range(len(ram), num_ram):
        ram.append(0)    
    # 레지스터 초기화
    for i in range(10):
        reg.append(0)

    # 명령어 실행
    num_executed = 0
    pc = 0
    done = 0
    while done == 0:
        inst = int(ram[pc] // 100)
        arg1 = int((ram[pc] / 10) % 10)
        arg2 = int(ram[pc] % 10)
        pc += 1
        num_executed += 1

        if inst == 1:
            done = 1
        elif inst == 2:
            reg[arg1] = arg2
        elif inst == 3:
            reg[arg1] = (reg[arg1] + arg2) % max_word
        elif inst == 4:
            reg[arg1] = (reg[arg1] * arg2) % max_word
        elif inst == 5:
            reg[arg1] = reg[arg2]
        elif inst == 6:
            reg[arg1] = (reg[arg1] + reg[arg2]) % max_word
        elif inst == 7:
            reg[arg1] = (reg[arg1] * reg[arg2]) % max_word
        elif inst == 8:
            reg[arg1] = ram[reg[arg2]]
        elif inst == 9:
            ram[reg[arg2]] = reg[arg1]
        elif inst == 0:
            if reg[arg2] != 0:
                pc = reg[arg1]
    
    print(num_executed)

    num_case -= 1
    if num_case > 0:
        print('')