import Utils


class DFS:
    init_state = [7, 2, 4, 5, 0, 6, 8, 3, 1]
    final_state = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 0], [0, 8, 7, 6, 5, 4, 3, 2, 1],
                   [8, 7, 6, 5, 4, 3, 2, 1, 0]]

    def parcours(self):
        game = Utils.Game()
        open = list()
        open.append(self.init_state)
        closed = {}
        iterations = 0
        nbr_noeuds = 0
        while Utils.verify_final_state(self.final_state,closed):
            temp = list(open)
            iterations = iterations + 1
            # print("________________")
            # print(iterations)
            # print('open :',open)
            # print('closed :',closed)
            l = open.pop(0)
            closed[Utils.list_to_string(l)] = '1'
            priorite = 0
            if Utils.list_to_string(game.right(l)) not in closed:
                open.insert(priorite, game.right(l))
                priorite = priorite + 1
                nbr_noeuds = nbr_noeuds + 1
            if Utils.list_to_string(game.up(l)) not in closed:
                open.insert(priorite, game.up(l))
                priorite = priorite + 1
                nbr_noeuds = nbr_noeuds + 1
                # print(game.up(l))
            if Utils.list_to_string(game.down(l)) not in closed:
                open.insert(priorite, game.down(l))
                priorite = priorite + 1
                nbr_noeuds = nbr_noeuds + 1
                # print(game.down(l))
            if Utils.list_to_string(game.right(l)) not in closed:
                open.insert(priorite, game.right(l))
                priorite = priorite + 1
                nbr_noeuds = nbr_noeuds + 1
                # print(game.right(l))
            if Utils.list_to_string(game.left(l)) not in closed:
                open.insert(priorite, game.left(l))
                nbr_noeuds = nbr_noeuds + 1

                # print(game.left(l))
        # print(open)
        print(closed.keys())
        print("nombre de noeuds: ", nbr_noeuds)
        print("iterations: ", iterations)


def main():
    dfs = DFS()
    dfs.parcours()


if __name__ == '__main__':
    main()
