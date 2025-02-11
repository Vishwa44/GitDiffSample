def process_data(data):
    """Process input data and return results"""
    output = []
    for item in data:
        output.append(float(item) * 2)
    return output

def analyze_results(results):
    """Analyze and return statistics"""
    if not results:
        return None
    
    return {
        'mean': sum(results) / len(results),
        'max': max(results),
        'min': min(results)
    }

# Process sample data
sample = 1, 2, 3, 4, 5
print(analyze_results(process_data(sample)))