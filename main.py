import task1
import task2

def main():
    while True:
        typeOfPart = input("Insert type of task, 1 for task number 1 or 2 for task number 2: ")
        if typeOfPart=='1':
            print('task1')
            task1.run()
            break
        if typeOfPart=='2':
            print('task2')
            task2.run()
            break


if __name__ == "__main__":
    main()