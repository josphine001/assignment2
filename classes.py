class students:
    total_students = 0

    def __init__(self, fname,lname,marks,reg_no,):
        self.fname = fname
        self.lname = lname
        self.marks = marks
        self.reg_no = reg_no
        self.email = fname + "." + lname + "@ttukenya.ac.ke"

    def get_total_students(self):
        return students.total_students
        
stud1 = students("john","doe", 45, 123456)
stud2 = students("jane","doe", 50, 123457)
stud3 = students("james","doe", 60, 123458)

print("total students:", students.total_students)



class courses:
    course_list = []
    def __init__(self,cname,code,units):
        self.cname = cname
        self.code = code
        self.units = units

    def add_course(self):
        courses.course_list.append(self.cname)
        return courses.course_list

course1 = courses("python", "cit 101", 3)
course2 = courses("java", "cit 102", 3)

print("course list:", course1.add_course)


class library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
    def get_book_info(self):
        return f"book name: {self.book_name}, author: {self.author}"
    
book1 = library("python programming", "juma doe")
book2 = library("java programming", "henry smith")

print(book1.get_book_info())