class Game:

    def up(self, liste):
        liste1=list(liste)
        pos = liste.index(0)
        if pos < 6:
            temp = liste[pos+3]
            liste1[pos] = temp
            liste1[pos+3] = 0
        return liste1

    def down(self, liste):
        liste1=list(liste)

        pos = liste.index(0)
        if pos > 2:
            temp = liste[pos - 3]
            liste1[pos] = temp
            liste1[pos - 3] = 0
        return liste1

    def right(self, liste):
        liste1=list(liste)

        pos = liste.index(0)
        if pos % 3 != 0:
            temp = liste[pos - 1]
            liste1[pos] = temp
            liste1[pos - 1] = 0
        return liste1

    def left(self, liste):
        liste1=list(liste)

        pos = liste.index(0)
        if pos % 3 != 2:
            temp = liste[pos + 1]
            liste1[pos] = temp
            liste1[pos + 1] = 0
        return liste1


class BFS:
    init_state = [1, 2, 3, 4, 5, 0,6, 7, 8]
    final_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def parcours(self):
        game = Game()
        open = list()
        open.append(self.init_state)
        closed = list()
        i=0
        while len(open) != 0 and self.final_state not in open:
            temp = list(open)
            i=i+1
            print("________________")
            print(i)
            print('open :',open)
            print('closed :',closed)
            open = list()

            for l in temp:

                closed.append(l)

                if list(game.up(l)) not in closed:
                    open.append(game.up(l))
                    print(game.up(l))
                if game.down(l) not in closed:
                    open.append(game.down(l))
                    print(game.down(l))
                if game.right(l) not in closed:
                    open.append(game.right(l))
                    print(game.right(l))
                if game.left(l) not in closed:
                    open.append(game.left(l))
                    print(game.left(l))
       # print(open)
        print(i)
        print(open )

def main():

    bfs = BFS()
    bfs.parcours()

if __name__ == '__main__':
    main()

