class Summa:

    def __init__(self):
        self.need = self.lis = None

    def set_list(self, lis):
        self.lis = lis

    def run(self, need):
        self.need = need
        self.get_lis([], 0, 0)

    def get_lis(self, res, pre, i):
        if i == 10:
            if pre == self.need:
                self.print_res(res)
        else:
            if i < 10:
                self.get_lis(res + ["+"] + [self.lis[i]], pre + self.lis[i], i + 1)
                self.get_lis(res + ["-"] + [self.lis[i]], pre - self.lis[i], i + 1)
            if i < 9:
                a = self.lis[i]*10 + self.lis[i + 1]
                self.get_lis(res + ["+"] + [a], pre + a, i + 2)
                self.get_lis(res + ["-"] + [a], pre - a, i + 2)

    def print_res(self, res):
        i = 0
        summa = 0
        string = ""
        while i < len(res):
            if res[i] == "+":
                summa += res[i + 1]
                if i != 0:
                    string += res[i]
                string += str(res[i+1])

            else:
                summa -= res[i+1]
                string += res[i] + str(res[i + 1])
            i += 2
        if summa == self.need:
            string += "=" + str(summa)
            print(string)

def main():
    a = Summa()
    a.set_list([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    a.run(200)

if __name__ == '__main__':
    main()

