import Utils


class BFS:
    init_state = [7, 2, 4, 5, 0, 6, 8, 3, 1]
    final_state = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 0], [0, 8, 7, 6, 5, 4, 3, 2, 1],
                   [8, 7, 6, 5, 4, 3, 2, 1, 0]]

    def parcours(self):
        game = Utils.Game()
        open = list()
        open.append(self.init_state)
        closed = {}
        i = 0
        j = 0
        while Utils.verify_final_state(self.final_state, closed):
            temp = list(open)
            i = i + 1
            # print("________________")
            # print(i)
            # print('open :',open)
            open = list()

            for l in temp:

                closed[Utils.list_to_string(l)] = i

                if Utils.list_to_string(game.up(l)) not in closed:
                    open.append(game.up(l))
                    j = j + 1
                    # print(game.up(l))
                if Utils.list_to_string(game.down(l)) not in closed:
                    open.append(game.down(l))
                    j = j + 1
                    # print(game.down(l))
                if Utils.list_to_string(game.right(l)) not in closed:
                    open.append(game.right(l))
                    j = j + 1
                    # print(game.right(l))
                if Utils.list_to_string(game.left(l)) not in closed:
                    open.append(game.left(l))
                    j = j + 1
                    # print(game.left(l))
        # print(open)
        print(closed.keys())
        print("profondeur: ", i)
        print("nombre de noeuds visités: ", j)


def main():
    bfs = BFS()
    bfs.parcours()


if __name__ == '__main__':
    main()
