students = ["Kutay Dündar", "Alp Turan", "Emre Acar", "Melih Turgut"]

loop = True
def menu():
    sec = input("Lütfen işlem seçiniz: \n"
                "1 - Öğrenci Ekle\n"
                "2 - Öğrenci Sil\n"
                "3 - Öğrencileri Listele\n"
                "4 - Öğrenci Numarası Öğrenme\n")

    if sec == "1":
        addStudent()
    if sec == "2":
        removeStudent()
    if sec == "3":
        studentsList()
    if sec == "4":
        studentNum()


# öğrenci kayıt
def addStudent():
    print(students)
    add = input("Eklemek istediğiniz öğrencinin ismini ve soy ismini giriniz: \n ")
    students.append(add)
    print(students)
    print("Öğrenci kaydedildi.")

    def cont():
        sec = input("Daha fazla ekleme işlemi yapmak için 1 seçeneğini giriniz.\n"
                    "Devam etmek için 2 seçeneğini giriniz.\n")
        if sec == "1":
            addStudent()
        if sec == "2":
            return menu()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()

    cont()


# öğenci silme
def removeStudent():
    print(students)
    remove = input("Silmek istediğiniz öğrencinin ismini ve soy ismini giriniz: \n ")
    if remove in students:
        students.remove(remove)
        print("Öğrenci kaydı silinmiştir.")
    else:
        print("hatalı giriş yaptınız veri bulunamadı tekrar deneyin")

        removeStudent()
    print(students)

    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için 1 seçeneğini giriniz.\n"
                    "Devam etmek için 2 seçeneğini giriniz.\n")
        if sec == "1":
            removeStudent()
        if sec == "2":
            return menu()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()

    cont()

def studentsList():
    for student in students:
        print(student)
        return menu()

def studentNum():
    print(students)
    num = input("Numrasını öğrenmek istediğiniz öğrencinin ismini ve soy ismini giriniz: \n ")
    stunum = students.index(num)
    print("{} Öğrencinin numarası: {} ".format(num, stunum))

    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için 1 seçeneğini giriniz.\n"
                    "Devam etmek için 2 seçeneğini giriniz.\n")
        if sec == "1":
            studentNum()
        if sec == "2":
            return menu()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()

    cont()


while loop:
    menu()