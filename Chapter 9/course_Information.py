course_Room = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
course_Instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
course_Meeting_Time = {'CS101': '8:00 AM', 'CS102': '9:00 AM', 'CS103': '10:00 AM', 'NT110': '11:00 AM', 'CM241': '1:00 PM'}

print("Please enter your course number:")
course_Number = input('>')

print("\nCourse information:")
print("Room:", course_Room[course_Number])
print("Instructor:", course_Instructor[course_Number])
print("Meeting Time:", course_Meeting_Time[course_Number])
