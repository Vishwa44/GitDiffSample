import statistics

def process_data(data):
    """
    Process the input data
    """
    res = []
    for d in data:
        # Convert to float and multiply
        val = float(d) * 1.5
        res.append(val)
    
    return res

def calculate_metrics(lst):
    """Calculate basic metrics"""
    total = sum(lst)
    avg = total / len(lst)
    
    # Find max value
    m = lst[0]
    for x in lst:
        if x > m:
            m = x
    
    return {
        "total": total,
        "average": avg,
        "maximum": m
    }

class DataAnalyzer:
    def __init__(self):
        self.data = []
    
    def add_numbers(self, nums):
        self.data.extend(nums)

# Example usage
if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5]
    processed = process_data(sample)
    metrics = calculate_metrics(processed)
    print(f"Processed data metrics: {metrics}")
    
    # Using the DataAnalyzer class
    analyzer = DataAnalyzer()
    analyzer.add_numbers(sample)