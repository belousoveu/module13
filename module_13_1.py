from asyncio import sleep, create_task, run, gather


class Strongman:

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def begin(self):
        print("Силач " + self.name + " начал соревнование.")

    async def raise_ball(self, ball_number):
        await sleep(1 / self.strength)
        print("Силач " + self.name + " поднял шар " + str(ball_number))

    def end(self):
        print("Силач " + self.name + " закончил соревнование.")

    async def start(self, balls):
        self.begin()
        for i in range(balls):
            await self.raise_ball(i + 1)
        self.end()


async def start_tournament(balls, *participants):
    tasks = []
    for participant in participants:
        tasks.append(create_task(participant.start(balls)))
    await gather(*tasks)


if __name__ == '__main__':
    number_of_balls = 5
    strongman_1 = Strongman("Pasha", 3)
    strongman_2 = Strongman("Denis", 4)
    strongman_3 = Strongman("Apollon", 5)

    run(start_tournament(number_of_balls, strongman_1, strongman_2, strongman_3))
