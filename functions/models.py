def make_models(unprinted, completed):

    while unprinted:
        print(f" Unprinted models: {unprinted}")
        completed.append(unprinted.pop())
        print(f"Completed: {completed}")

    return completed

not_printed = ['Car', 'Bike', 'House']
completed_models = []

completed = make_models(not_printed[:], completed_models)
print()
print(f"Not_printed: {not_printed}")
print(f"Completed-models: {completed_models}")
print(completed)

