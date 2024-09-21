def fifo_page_replacement(pages: list[int], frame_size: int) -> int:
    memory = []  # List to store pages in memory
    page_faults = 0  # Count of page faults

    for page in pages:
        if page not in memory:
            if len(memory) == frame_size:
                memory.pop(0)  # Remove the oldest page (FIFO)
            memory.append(page)  # Add the new page
            page_faults += 1

    return page_faults

def lru_page_replacement(pages: list[int], frame_size: int) -> int:
    memory = []  # List to store pages in memory
    page_faults = 0  # To count page faults

    for page in pages:
        if page not in memory:
            if len(memory) == frame_size:
                memory.pop(0)  # Remove the least recently used page
            memory.append(page)  # Add the new page
            page_faults += 1
        else:
            # Refresh the page by moving it to the end
            memory.remove(page)
            memory.append(page)

    return page_faults

# Test cases for comparing FIFO and LRU page replacement algorithms

# 1. Simple Repeated Pages
pages1 = [1, 1, 1, 1, 1]
frame_sizes1 = [1, 2, 3]

# 2. Sequential Access
pages2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
frame_sizes2 = [2, 3, 4]

# 3. Alternating Pattern
pages3 = [1, 2, 1, 2, 1, 2, 1, 2]
frame_sizes3 = [1, 2, 3]

# 4. Mixed Pattern
pages4 = [3, 2, 1, 4, 2, 5, 2, 3, 7, 6, 3, 2, 1, 4, 3, 2, 1]
frame_sizes4 = [3, 4, 5]

# 5. Worst-Case for FIFO
pages5 = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frame_sizes5 = [3, 4]

# Function to run test cases and show only page faults
def run_test_cases():
    print(f"{'Test Case':<12}{'Frame Size':<12}{'FIFO Faults':<12}{'LRU Faults':<12}")
    print("-" * 48)
    
    # Test Case 1: Simple Repeated Pages
    for size in frame_sizes1:
        print(f"Case 1    {size:<12}{fifo_page_replacement(pages1, size):<12}{lru_page_replacement(pages1, size):<12}")
    
    # Test Case 2: Sequential Access
    for size in frame_sizes2:
        print(f"Case 2    {size:<12}{fifo_page_replacement(pages2, size):<12}{lru_page_replacement(pages2, size):<12}")
    
    # Test Case 3: Alternating Pattern
    for size in frame_sizes3:
        print(f"Case 3    {size:<12}{fifo_page_replacement(pages3, size):<12}{lru_page_replacement(pages3, size):<12}")
    
    # Test Case 4: Mixed Pattern
    for size in frame_sizes4:
        print(f"Case 4    {size:<12}{fifo_page_replacement(pages4, size):<12}{lru_page_replacement(pages4, size):<12}")
    
    # Test Case 5: Worst-Case for FIFO
    for size in frame_sizes5:
        print(f"Case 5    {size:<12}{fifo_page_replacement(pages5, size):<12}{lru_page_replacement(pages5, size):<12}")

# Run all test cases
run_test_cases()
