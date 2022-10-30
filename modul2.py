student_dummy = {
    1: {"name": "Emil", "UAS": 78, "UTS": 80},
    2: {"name": "Tobias", "UAS": 56, "UTS": 50},
    3: {"name": "Linus", "UAS": 89, "UTS": 50},
    4: {"name": "Marie", "UAS": 88, "UTS": 90}
}

student2 = {
    1: {"name": "Emil", "UAS": 78},
    2: {"name": "Tobias", "UAS": 56},
    3: {"name": "Linus", "UAS": 89},
    4: {"name": "Marie", "UAS": 88}
}

student3 = {
    1: {"name": "Emil", "UAS": 78, "ulangan1": 80, "ulangan2": 80, "ulangan3": 90},
    2: {"name": "Tobias", "UAS": 56, "ulangan1": 70, "ulangan2": 80, "ulangan3": 90},
    3: {"name": "Linus", "UAS": 89, "ulangan1": 80, "ulangan2": 80, "ulangan3": 100},
    4: {"name": "Marie", "UAS": 88, "ulangan1": 80, "ulangan2": 90, "ulangan3": 90}
}

teacher = {
    1: {"name": "Izul"},
    2: {"name": "Ez"},
    3: {"name": "Nayir"},
    4: {"name": "Fila"}
}

counter = 0


def main(student: dict, counters: int):
    login(student, counters)


def login(student, counters):
    print("[1] Teacher ")
    print("[2] Student ")
    print(counters)

    role = input("Pilih Role : ")
    if role == "1":
        print("Teacher")
        name = input("Username : ")
        for teacher_id, teacher_data in teacher.items():
            if teacher_data["name"] == name:
                teacher_page(counters, student)

        return login(student, counters)

    elif role == "2":
        name = input("Username : ")
        for student_id, student_data in student.items():
            if student_data["name"] == name:
                student_page(student_id, student, counters)

        return login(student, counters)


def student_page(_id, student, counters):
    for key, student_data in student[_id].items():
        print(key, ":", student_data)

    if "ulangan1" in student[_id] and "ulangan2" in student[_id] and "ulangan3" in student[_id]:
        ulangan_total = (student[_id]["ulangan1"] + student[_id]["ulangan2"] + student[_id]["ulangan3"]) / 3
        print("Nilai akhir : " + str((student[_id]["UAS"] + ulangan_total) / 2))

    elif "ulangan1" in student[_id] and "ulangan2" in student[_id]:
        ulangan_total = (student[_id]["ulangan1"] + student[_id]["ulangan2"]) / 2
        print("Nilai akhir : " + str((student[_id]["UAS"] + ulangan_total) / 2))

    elif 'ulangan1' in student[_id]:
        nilai = lambda x, y: (x + y) / 2
        print("Akhir 2")
        print("Nilai akhir : " + str(nilai(student[_id]["UAS"], student[_id]["ulangan1"])))
        # print("Nilai akhir : " + str((student[_id]["UAS"] + student[_id]["ulangan1"]) / 2))

    else:
        print("Akhir woy")
        print("Nilai akhir : " + str(student[_id]["UAS"]))

    return login(student, counters)


def teacher_page(counters, student):
    print("[1] Input/Create Data Student")
    print("[2] Edit Nilai")
    print("[3] Delete data")
    print("[4] Read List Data")
    print("[5] Adakan Ulangan Harian")
    print("[6] Edit nama")

    menu = input("Pilih Menu : ")

    if menu == "1":
        student_create = create_data_student(student)
        return login(student_create, counters)

    elif menu == "2":
        print("[1] Edit Nilai UAS")
        print("[2] Edit Nilai Ulangan Harian")

        edit = input("Pilih Menu : ")

        if edit == "1":
            return login(edit_ujian(student, "UAS"), counters)

        elif edit == "2":
            print("[1] Edit Ulangan 1")
            print("[2] Edit Ulangan 2")
            print("[3] Edit Ulangan 3")
            choose = input("Pilih Menu : ")

            if choose == "1":
                return login(edit_ujian(student, "ulangan1"), counters)

            elif choose == "2":
                return login(edit_ujian(student, "ulangan2"), counters)

            elif choose == "3":
                return login(edit_ujian(student, "ulangan3"), counters)

        else:
            print("Pilihan tidak ada")

    elif menu == "3":
        print("menu 3")
        print("[1] Delete Data Siswa")
        print("[2] Delete Nilai Siswa")
        choose = input("Pilih : ")

        if choose == "1":
            return login(delete_data_student(student), counters)

        elif choose == "2":
            print("[1] Delete Nilai UAS")
            print("[2] Delete Nilai Ulangan 1")
            print("[3] Delete Nilai Ulangan 2")
            print("[4] Delete Nilai Ulangan 3")
            del_menu = input("Pilih : ")

            if del_menu == "1":
                return login(delete_nilai_student(student, "UAS"), counters)

            elif del_menu == "2":
                return login(delete_nilai_student(student, "ulangan1"), counters)

            elif del_menu == "3":
                return login(delete_nilai_student(student, "ulangan2"), counters)

            elif del_menu == "4":
                return login(delete_nilai_student(student, "ulangan3"), counters)

    elif menu == "4":
        print("menu 4")
        show_students(student)

    elif menu == "5":
        print("menu 5")

        test = count_test(counters, student)
        return login(student, test)

    elif menu == "6":
        print("menu 6")
        return login(edit_name(student), counters)

    else:
        print("Pilihan tidak ada")


def edit_name(student):
    show_students(student)

    id_edit_name = input("Pilih ID Edit name : ")
    new_name = input("Masukkan nama baru : ")
    student[int(id_edit_name)]["name"] = int(new_name)

    show_students(student)

    return student


def delete_nilai_student(student, key: str):
    show_students(student)
    id_delete = input("Pilih by ID yg dihapus : ")
    student[int(id_delete)][key] = 0

    return student


def delete_data_student(student):
    show_students(student)
    id_delete = input("Pilih by ID yg dihapus : ")
    del student[int(id_delete)]
    show_students(student)

    return student


def edit_ujian(student, key: str):
    show_students(student)

    id_to_edit = input("Pilih by ID : ")
    nilai_uh_edit = input("Masukkan Nilai Ulangan 1 : ")
    student[int(id_to_edit)][key] = int(nilai_uh_edit)

    show_students(student)

    return student


def create_data_student(student):
    nama = input("Masukkan Nama Student : ")
    uas = input("Masukkan Nilai UAS : ")
    student[len(student) + 1] = {"name": nama, "UAS": int(uas)}

    show_students(student)

    return student


def count_test(counters, student):
    print(counters)
    if counters == 0:
        add_ulangan(student, "ulangan1")
        counters += 1

    elif counters == 1:
        add_ulangan(student, "ulangan2")
        counters += 1

    elif counters == 2:
        add_ulangan(student, "ulangan3")
        counters += 1

    elif counters > 2:
        print('Batas Ulangan Harian sudah tercapai')

    return counters


def add_ulangan(student, key: str):
    for student_data in student.values():
        student_data.update({key: 0})
        print(student_data)


def show_students(student):
    for student_id, student_data in student.items():
        print("\nStudent ID:", student_id)

        for key in student_data:
            print(key, ':', student_data[key])


main(student2, counter)

# while len(student2) >= counter:
#     student2[counter]['ulangan'] = 0
#     counter += 1


# show_data_student2()
