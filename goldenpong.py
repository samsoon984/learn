from datetime import date

def soloXmas(plusYear=int(input("입력: "))):
    xmasDate, goldenSum, pongdangSum = date(2020, 12, 25), 0, 0
    for i in range(0, plusYear):
        xmasDate = date(2020+i, 12, 25)
        if xmasDate.weekday() in [0, 4]:
            goldenSum += 1
            print(xmasDate, "황금 연휴")
        elif xmasDate.weekday() in [1, 3]:
            pongdangSum += 1
            print(xmasDate, "퐁당")
        else:
            print(xmasDate)
    print(f"총 황금연휴: {goldenSum}, 총 징검다리: {pongdangSum}")

if __name__ == "__main__":
    soloXmas()