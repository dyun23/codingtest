from sys import stdin

amount, n = map(int, input().split())

pokemon_name, pokemon_num = dict(), dict()

for i in range(amount):
    name = stdin.readline().strip()
    pokemon_name[name] = i + 1
    pokemon_num[i + 1] = name

for _ in range(n):
    quiz = stdin.readline().strip()
    if quiz.isdigit():
        print(pokemon_num[int(quiz)])
    else:
        print(pokemon_name[quiz])