import random

names = ['Иванова', 'Кузнецов', 'Поливанов']
events = ['Кто последний? Я -', 'Я только спросить! Я -', 'Следующий!']
responses = ['Заходит', 'В очереди никого нет']
eventList = list()
n = 0
while True:
    rnd = random.randint(0, 2)
    n += 1
    if n >= 50:
        rnd = 2
    if rnd == 0:
        rndName = names[random.randint(0, 2)]
        print(events[0], rndName)
        eventList.append([events[0], rndName])
    if rnd == 1:
        rndName = names[random.randint(0, 2)]
        print(events[1], rndName)
        eventList.insert(0, [events[1], rndName])
    if rnd == 2:
        print(events[2])
        if len(eventList) == 0:
            print(responses[1])
            break
        else:
            print(responses[0], eventList.pop(0)[1])

