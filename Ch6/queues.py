from queue import Queue, LifoQueue, Full

# Queue and LifoQueue (stack) follow the same API
# For priority queues, use the heapq library

def show_example(data_structure):
    print("")
    print("Showing example:", data_structure)
    print("")
    print("empty:", data_structure.empty())

    try:
        # if not block, it will wait until an element is available
        # block=False raises an exception if there is no element
        data_structure.get(block=False)
    except Exception as e:
        print("error: tried to access queue with no elements")
        print(e)

    print("putting 3 elements")
    data_structure.put("one")
    data_structure.put("two")
    data_structure.put("three")
    print("putting fourth element; this will raise an error after timeout")
    try:
        data_structure.put("four", timeout=3)
    except Full as e:
        print("error raised:", e.__dict__)

    print("\nqueue full:", data_structure.full())
    for i in range(3):
        print("calling get:", data_structure.get())
    print("empty?", data_structure.empty())

lineup = Queue(maxsize=3)
show_example(lineup)

stack = LifoQueue(maxsize=3)
show_example(stack)





