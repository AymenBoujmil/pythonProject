import Utils


class State:
    liste = list()
    profond: int

    def __init__(self, liste, profond):
        self.liste = liste
        self.profond = profond


class DFSIterative:
    init_state = [7, 2, 4, 5, 0, 6, 8, 3, 1]
    final_state = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 0], [0, 8, 7, 6, 5, 4, 3, 2, 1],
                   [8, 7, 6, 5, 4, 3, 2, 1, 0]]

    def parcours(self):
        game = Utils.Game()
        open = list()
        profond = 0
        state = State(self.init_state, profond)
        open.append(state)
        closed = {}
        iterations = 0
        nbr_noeuds = 0
        limit = 0

        while Utils.verify_final_state(self.final_state, closed):
            limit = limit + 1
            open = list()
            open.append(state)
            closed = {}
            profond = 0

            while len(open) != 0 and Utils.verify_final_state(self.final_state, closed):
                if profond < limit:
                    temp = list(open)

                    profond = profond + 1

                    # iterations = iterations + 1
                    # print("________________")
                    # print(profond)
                    # for i in open:
                    #   print('open :', i.liste)
                    # print('closed :', closed)
                    s = open.pop(0)
                    l = s.liste
                    closed[Utils.list_to_string(l)] = profond
                    priorite = 0
                    if Utils.list_to_string(game.up(l)) not in closed:
                        open.insert(priorite, State(game.up(l), profond))
                        # print('up', game.up(l))
                        if profond == limit:
                            s = open.pop(priorite)
                            priorite = priorite - 1
                            l1 = s.liste
                            closed[Utils.list_to_string(l1)] = profond
                        priorite = priorite + 1
                        # nbr_noeuds = nbr_noeuds + 1

                    if Utils.list_to_string(game.down(l)) not in closed:
                        open.insert(priorite, State(game.down(l), profond))
                        # print('down', game.down(l))
                        if profond == limit:
                            s = open.pop(priorite)
                            priorite = priorite - 1
                            l1 = s.liste
                            closed[Utils.list_to_string(l1)] = profond
                        priorite = priorite + 1
                        # nbr_noeuds = nbr_noeuds + 1

                    if Utils.list_to_string(game.right(l)) not in closed:
                        open.insert(priorite, State(game.right(l), profond))
                        # print('right', game.right(l))
                        if profond == limit:
                            s = open.pop(priorite)
                            priorite = priorite - 1
                            l1 = s.liste
                            closed[Utils.list_to_string(l1)] = profond
                        priorite = priorite + 1
                        # nbr_noeuds = nbr_noeuds + 1

                    if Utils.list_to_string(game.left(l)) not in closed:
                        open.insert(priorite, State(game.left(l), profond))
                        # print('left', game.left(l))
                        nbr_noeuds = nbr_noeuds + 1
                        if profond == limit:
                            s = open.pop(priorite)
                            l1 = s.liste
                            closed[Utils.list_to_string(l1)] = profond
                else:
                    # print(open[0].liste, '||', open[0].profond)
                    # print('___________', closed)
                    profond = open[0].profond
                # print("closed : ", closed)

                # print(game.left(l))
                # print(open)
                # print("nombre de noeuds: ", nbr_noeuds)
                # print("iterations: ", iterations)
        print('closed: ', closed)
        print('Limit:', limit)


def main():
    dfsI = DFSIterative()

    dfsI.parcours()


if __name__ == '__main__':
    main()
