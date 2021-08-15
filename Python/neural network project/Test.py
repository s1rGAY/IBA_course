import cv2
import pytesseract

print()


def work_with_file(file):
    img = cv2.imread(file)

    # converting an image to the desired format
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img


def img_to_sting(img):
    # oem version for correct work
    config = r'--oem 3 --psm 6'

    # reading text
    text = pytesseract.image_to_string(img, config=config)

    return text


def find_info(text):
    print('Please, enter your fragment ', end=': ')
    key = input()
    print('WORK!')
    return


def find_in_pic(img):
    data = pytesseract.image_to_data(img, config=r'--oem 3 --psm 6')
    for i, el, in enumerate(data.splitlines()):
        # the first iteration outputs unnecessary data
        if i == 0:
            continue
        el=el.split()
        try:
            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
            cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
        except IndexError:
            print('Error')
# all_words = text.split()

# print("Your text : ", text)


def main():
    print("Hello! Please, enter the name of your file : ")
    img = work_with_file(input())
    text = img_to_sting(img)
    while True:
        print()
        print('What do you want to do with your text : ')
        print('Show all text - 1')
        print('Display text by words - 2')
        print('Find a fragment or a word in the text - 3')
        print('Show a fragment or a word in the picture - 4')
        # print('Show your img - 4')
        print('Exit - 0')
        print('Your input ', end=': ')
        i = int(input())
        print()
        if i == 1:
            print('Your text : ')
            print(text)
        if i == 2:
            print(text.split())
        if i == 3:
            find_info(text)
        if i == 4:
            find_in_pic(img)
            cv2.imshow('IBA final Project', img)
            cv2.waitKey(0)
        if i == 0:
            break


main()

print()
