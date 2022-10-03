student = {
    1: {"name": "Emil", "UAS": 78, "UTS": 80},
    2: {"name": "Tobias", "UAS": 56, "UTS": 50},
    3: {"name": "Linus", "UAS": 89, "UTS": 50},
    4: {"name": "Marie", "UAS": 88, "UTS": 90}
}

teacher = {
    1: {"name": "Izul"},
    2: {"name": "Ez"},
    3: {"name": "Nayir"},
    4: {"name": "Fila"}
}


def main():
    login()


def login():
    print("[1] Teacher ")
    print("[2] Student ")

    role = input("Pilih Rule : ")
    if role == "1":
        print("Teacher")
        name = input("Username : ")
        for teacher_id, teacher_data in teacher.items():
            if teacher_data["name"] == name:
                teacher_page()
            else:
                print("Usernmae Tidak Ditemukan")
                break
        login()

    elif role == "2":
        name = input("Username : ")
        for student_id, student_data in student.items():
            if student_data["name"] == name:
                student_page(student_id)
            else:
                print("Username Tidak Ditemukan")
                break
        login()


def student_page(_id):
    print("[1] Nilai Akhir Anda")
    input("Pilih Menu : ")

    print("Nilai akhir : " + str((student[_id]["UAS"] + student[_id]["UTS"]) / 2))
    login()


def teacher_page():
    print("[1] Input Data Student")
    print("[2] Edit Nilai")

    menu = input("Pilih Menu : ")

    if menu == "1":
        nama = input("Masukkan Nama Student : ")
        uas = input("Masukkan Nilai UAS : ")
        uts = input("Masukkan Nilai UTS : ")

        student[len(student) + 1] = {"name": nama, "UAS": int(uas), "UTS": int(uts)}
        show_data_student()
        login()

    elif menu == "2":
        print("[1] Edit Nilai UAS")
        print("[2] Edit Nilai UTS")

        edit = input("Pilih Menu : ")

        if edit == "1":
            show_data_student()
            id_to_edit = input("Pilih by ID : ")

            nilai_uas_edit = input("Masukkan Nilai UAS : ")
            student[int(id_to_edit)]["UAS"] = int(nilai_uas_edit)
            show_data_student()
            login()

        elif edit == "2":
            show_data_student()
            id_to_edit = input("Pilih by ID : ")

            nilai_uts_edit = input("Masukkan Nilai UTS : ")
            student[int(id_to_edit)]["UAS"] = int(nilai_uts_edit)
            show_data_student()
            login()
        else:
            print("Pilihan tidak ada")

    else:
        print("Pilihan tidak ada")


def show_data_student():
    for student_id, student_data in student.items():
        print("\nStudent ID:", student_id)

        for key in student_data:
            print(key, ':', student_data[key])


main()
