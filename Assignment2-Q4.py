def gps(initial_state, goal_state, operators):
    state = initial_state[:]
    plan = []
    tried_actions = set()

    while not all(goal in state for goal in goal_state):
        applied = False
        for op in operators:
            if op["action"] in tried_actions:
                continue
            if all(p in state for p in op["preconds"]):
                for d in op["delete"]:
                    if d in state:
                        state.remove(d)
                for a in op["add"]:
                    if a not in state:
                        state.append(a)
                plan.append(op["action"])
                tried_actions.add(op["action"])
                print("Applied:", op["action"])
                print("Current state:", state)
                applied = True
                break
        if not applied:
            print("No applicable operator found. Stopping.")
            break

    print("\nFinal state reached:", state)
    print("Plan:", plan)



disk_ops = [
    {
        "action": "move-green-from-pole-to-table",
        "preconds": ["green-disk-on-pole", "green-disk-on-top"],
        "add": ["green-disk-on-table"],
        "delete": ["green-disk-on-pole", "green-disk-on-top"]
    },
    {
        "action": "move-blue-from-pole-to-table",
        "preconds": ["blue-disk-on-pole", "blue-disk-on-top"],
        "add": ["blue-disk-on-table"],
        "delete": ["blue-disk-on-pole", "blue-disk-on-top"]
    },
    {
        "action": "move-red-from-pole-to-table",
        "preconds": ["red-disk-on-pole", "red-disk-on-top"],
        "add": ["red-disk-on-table"],
        "delete": ["red-disk-on-pole", "red-disk-on-top"]
    },
    {
        "action": "move-green-from-table-to-pole",
        "preconds": ["green-disk-on-table"],
        "add": ["green-disk-on-pole", "green-disk-on-top"],
        "delete": ["green-disk-on-table"]
    },
    {
        "action": "move-blue-from-table-to-pole",
        "preconds": ["blue-disk-on-table"],
        "add": ["blue-disk-on-pole", "blue-disk-on-top"],
        "delete": ["blue-disk-on-table"]
    },
    {
        "action": "move-red-from-table-to-pole",
        "preconds": ["red-disk-on-table"],
        "add": ["red-disk-on-pole", "red-disk-on-top"],
        "delete": ["red-disk-on-table"]
    }
]

gps(
    ["red-disk-on-pole", "blue-disk-on-pole", "green-disk-on-pole", "green-disk-on-top"],
    ["green-disk-on-pole", "blue-disk-on-pole", "red-disk-on-pole", "red-disk-on-top"],
    disk_ops
)
