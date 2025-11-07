
student_ids = [101, 102, 103, 104, 101, 105, 102]

unique_ids = set(student_ids)

if len(student_ids) != len(unique_ids):
    print("ნაპოვნია განმეორებული ID-ები")
else:
    print("ყველა ID უნიკალურია.")

print("უნიკალური ID-ები:", unique_ids)
