import time
statement = "Well..."

things = ["| ", "/ ", "—— ", "\\ ", "| ", "/ ", "——", "\\ "]


for t in things:
    # print(t)
    print(f"\r{statement} {t}", end="")
    time.sleep(1)

print("\rFUCK!      ", end="")