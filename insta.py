def getUsernames(filename):
    file = open(filename) 
    usernames = file.read().splitlines()
    file.close()
    return usernames


followers = getUsernames("followers.txt")
subscriptions = getUsernames("subscriptions.txt")

counter = 0
for subscription in subscriptions:
    if subscription not in followers:
        counter += 1
        print(f"{subscription}")

print(counter)