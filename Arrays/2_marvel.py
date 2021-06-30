hero = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1. Length of the list
print(len(hero))

# 2. Add 'black panther' at the end of this list
hero.append('black panther')
print(hero)

# 3. Add black panther after hulk
hero.remove('black panther')
hero.insert(3, 'black panther')
print(hero)

# 4 Replace thor and hulk because they get angry quickly
hero[1:3] = ['doctor strange']
print(hero)

# 5. Sort the list in alphabetical order
hero.sort()
print(hero)