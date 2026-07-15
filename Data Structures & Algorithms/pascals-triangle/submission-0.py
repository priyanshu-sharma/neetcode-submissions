class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        initial_data = [1]
        output.append(initial_data)
        for i in range(1, numRows):
            initial_data.insert(0, 0)
            initial_data.insert(len(initial_data), 0)
            intermediate_output = []
            for j in range(0, len(initial_data) - 1):
                intermediate_output.append(initial_data[j] + initial_data[j + 1])
            initial_data.pop(0)
            initial_data.pop(len(initial_data) - 1)
            initial_data = intermediate_output
            output.append(intermediate_output)
        return output