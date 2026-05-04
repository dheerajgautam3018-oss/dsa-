from collections import deque

# Social network graph
social_network = {
    "Aman": ["Riya", "Karan", "Simran"],
    "Riya": ["Aman", "Karan"],
    "Karan": ["Aman", "Riya", "Rahul"],
    "Simran": ["Aman"],
    "Rahul": ["Karan"]
}


# Display network
def display_network():
    print("Social Network:")
    for user in social_network:
        print(user, "->", social_network[user])


# BFS Traversal
def bfs(start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("\nBFS Traversal:")
    while queue:
        user = queue.popleft()
        print(user, end=" ")

        for friend in social_network[user]:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)


# DFS Traversal
def dfs(user, visited=None):
    if visited is None:
        visited = set()

    if user not in visited:
        print(user, end=" ")
        visited.add(user)

        for friend in social_network[user]:
            dfs(friend, visited)


# Friend Suggestion
def suggest_friends(user):
    friends = set(social_network[user])
    suggestions = set()

    for friend in friends:
        suggestions.update(social_network[friend])

    suggestions -= friends
    suggestions.discard(user)

    return suggestions


# Main
display_network()

bfs("Aman")

print("\n\nDFS Traversal:")
dfs("Aman")

print("\n\nFriend Suggestions for Aman:")
print(suggest_friends("Aman"))