def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move container 1 from", source, "to", destination)
        return

    # Move n-1 containers from source to auxiliary
    towers_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the largest container to destination
    print("Move container", n, "from", source, "to", destination)

    # Move n-1 containers from auxiliary to destination
    towers_of_hanoi(n - 1, auxiliary, source, destination)


# Number of containers
n = 3

# A = Source, B = Auxiliary, C = Destination
towers_of_hanoi(n, 'A', 'B', 'C')
