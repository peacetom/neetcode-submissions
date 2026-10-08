class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        i = 0
        count = 0
        while i < len(sandwiches):
            if count >= len(queue):
                return count
            student_preference = queue.popleft()
            if student_preference == sandwiches[i]:
                i += 1
                count = 0
            else:
                queue.append(student_preference)
                count += 1
        return 0

