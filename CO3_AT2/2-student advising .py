# Student Academic Advising System
# Knowledge Representation and Reasoning

# -----------------------------
# 1. Knowledge Base - Facts
# -----------------------------

student = "Priya"

low_attendance = True
failed_two_or_more = True


# -----------------------------
# 2. Inference Rules
# -----------------------------

# Rule 1:
# Students with low attendance require attendance counseling
if low_attendance:
    attendance_counseling = True
else:
    attendance_counseling = False


# Rule 2:
# Students who fail two or more courses require academic counseling
if failed_two_or_more:
    academic_counseling = True
else:
    academic_counseling = False


# Rule 3:
# Students requiring both counseling types need academic support
if attendance_counseling and academic_counseling:
    academic_support = True
else:
    academic_support = False


# -----------------------------
# 3. Display Facts
# -----------------------------

print("===== STUDENT ACADEMIC ADVISING SYSTEM =====")
print()

print("Student:", student)

print("\n--- Given Facts ---")

if low_attendance:
    print("1. Priya has attendance below 75%.")

if failed_two_or_more:
    print("2. Priya has failed two or more courses.")


# -----------------------------
# 4. Display Inference
# -----------------------------

print("\n--- Inference Results ---")

if attendance_counseling:
    print("3. Priya requires attendance counseling.")

if academic_counseling:
    print("4. Priya requires academic counseling.")

if academic_support:
    print("5. Priya requires academic support.")


# -----------------------------
# 5. Final Decision
# -----------------------------

print("\n--- Final Decision ---")

if academic_support:
    print("RESULT: Priya requires academic support.")
else:
    print("RESULT: Priya does not require academic support.")
