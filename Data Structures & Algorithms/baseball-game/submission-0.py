class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                score_popped = record.pop()
                new_score = score_popped + record[-1]
                record.append(score_popped)
                record.append(new_score)
            elif op == 'D':
                record.append(record[-1]*2)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))

        print(record)
        return sum(record)
