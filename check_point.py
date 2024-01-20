

def max_guests(times):
    
    timeline = []
    
    for entry in times:
        entry_time, exit_time = entry
        timeline.append((entry_time, 1)) # entry represented by 1
        timeline.append((exit_time, -1)) # entry represented by -1
        
    timeline.sort()
    
    max_count = 0
    current_count = 0
    
    





if __name__ == '__main__':
    times = [(1, 3), (2, 5), (1, 8)]