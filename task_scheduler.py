"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time.
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
 (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
"""
import heapq


def task_scheduler(tasks, n):
    if n == 0:
        return len(tasks)
    time = 0
    # count frequency
    freq = [0]*26
    for task in tasks:
        freq[ord(task)-ord('A')] += 1

    # create priority queue for tasks
    pq = []
    heapq.heapify(pq)
    for f in freq:
        if f != 0:
            heapq.heappush(pq, -1*f)

    while len(pq) > 0:
        print(pq)
        remainingTasks = []
        cycle = n+1
        while cycle > 0 and len(pq) > 0:
            taskFreq = -1*heapq.heappop(pq)
            taskFreq -= 1   # accomplish task
            if taskFreq > 0:
                remainingTasks.append(-1*taskFreq)
            cycle -= 1  # idle time is utilized against task
            time += 1  # time required to execute this task
        for remainingTask in remainingTasks:
            heapq.heappush(pq, remainingTask)
        if len(pq) > 0:
            time += cycle
    return time


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(task_scheduler(tasks, n))
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    print(task_scheduler(tasks, n))

