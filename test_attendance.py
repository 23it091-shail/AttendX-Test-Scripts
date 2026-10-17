
import unittest

def mark_attendance(student_id, status):
    if not student_id:
        return "Invalid Student ID"
    if status not in ["Present", "Absent"]:
        return "Invalid Attendance Status"
    return "Attendance Marked Successfully"


class TestAttendance(unittest.TestCase):

    def test_valid_attendance(self):
        result = mark_attendance("STU101", "Present")
        self.assertEqual(result, "Attendance Marked Successfully")

    def test_invalid_attendance(self):
        result = mark_attendance("STU101", "Late")
        self.assertEqual(result, "Invalid Attendance Status")


if __name__ == "__main__":
    unittest.main()
