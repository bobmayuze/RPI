# Author: Yuze Bob Ma
# Date: Sept, 30th, 2016
# This code is write for RPI CSCI 1100 course, HW 3 part 3

# define functions
def move(x, y, direction, amount=20):
	if direction == 'right':
		x = x + amount
		x = min(x, 400)
		return[x, y, 'right']
	elif direction == 'up':
		y = y - amount
		y = max(y, 0)
		return[x, y, 'up']
	elif direction == 'left':
		x = x - amount
		x = max(x, 0)
		return[x, y, 'left']
	else:
		y = y + amount
		y = min(y, 400)
		return[x, y, 'down']

def turn(direction):
	if direction == 'right':
		direction = 'up'
		return direction
	elif direction == 'up':
		direction = 'left'
		return direction
	elif direction == 'left':
		direction = 'down'
		return direction
	else:
		direction = 'right'
		return direction

# Init variables
status = [200, 200, 'right']
cmd_list = []
sleep = 1

print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))


# Imput cmd
if sleep > 0:
	cmd_1 = input('Command (move,jump,turn,sleep) => ')
	print(cmd_1)
	cmd_new = cmd_1.lower()
	if cmd_new == 'move':
		status = move(status[0], status[1], status[2])
	elif cmd_new == 'jump':
		status = move(status[0], status[1], status[2], 50)
	elif cmd_new == 'turn':
		status[2] = turn(status[2])
	elif cmd_new == 'sleep':
		print('Turtle falls asleep.')
		sleep = -sleep 
	else:
		status = status
	print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))
	cmd_list.append(cmd_1)
else:
	print('Turtle is currently sleeping ... no command this turn.')
	sleep = -sleep
	print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))


if sleep > 0:
	cmd_2 = input('Command (move,jump,turn,sleep) => ')
	print(cmd_2)
	cmd_new = cmd_2.lower()
	if cmd_new == 'move':
		status = move(status[0], status[1], status[2])
	elif cmd_new == 'jump':
		status = move(status[0], status[1], status[2], 50)
	elif cmd_new == 'turn':
		status[2] = turn(status[2])
	elif cmd_new == 'sleep':
		print('Turtle falls asleep.')
		sleep = -sleep 
	else:
		status = status
	print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))
	cmd_list.append(cmd_2)
else:
	print('Turtle is currently sleeping ... no command this turn.')
	sleep = -sleep
	print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))


if sleep > 0:
	cmd_3 = input('Command (move,jump,turn,sleep) => ')
	print(cmd_3)
	cmd_new = cmd_3.lower()
	if cmd_new == 'move':
		status = move(status[0], status[1], status[2])
	elif cmd_new == 'jump':
		status = move(status[0], status[1], status[2], 50)
	elif cmd_new == 'turn':
		status[2] = turn(status[2])
	elif cmd_new == 'sleep':
		print('Turtle falls asleep.')
		sleep = -sleep 
	else:
		status = status
	print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))
	cmd_list.append(cmd_3)
else:
	print('Turtle is currently sleeping ... no command this turn.')
	sleep = -sleep
	print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))


if sleep > 0:
	cmd_4 = input('Command (move,jump,turn,sleep) => ')
	print(cmd_4)
	cmd_new = cmd_4.lower()
	if cmd_new == 'move':
		status = move(status[0], status[1], status[2])
	elif cmd_new == 'jump':
		status = move(status[0], status[1], status[2], 50)
	elif cmd_new == 'turn':
		status[2] = turn(status[2])
	elif cmd_new == 'sleep':
		print('Turtle falls asleep.')
		sleep = -sleep
	else:
		status = status
	print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))
	cmd_list.append(cmd_4)
else:
	print('Turtle is currently sleeping ... no command this turn.')
	sleep = -sleep
	print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))


if sleep > 0:
	cmd_5 = input('Command (move,jump,turn,sleep) => ')
	print(cmd_5)
	cmd_new = cmd_5.lower()
	if cmd_new == 'move':
		status = move(status[0], status[1], status[2])
	elif cmd_new == 'jump':
		status = move(status[0], status[1], status[2], 50)
	elif cmd_new == 'turn':
		status[2] = turn(status[2])
	elif cmd_new == 'sleep':
		print('Turtle falls asleep.')
		sleep = -sleep 
	else:
		status = status
	print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))
	cmd_list.append(cmd_5)
else:
	print('Turtle is currently sleeping ... no command this turn.')
	sleep = -sleep
	print('Turtle: ({0}, {1}) facing: {2}'.format(status[0],status[1], status[2]))



print()
cmd_list_neat = sorted(cmd_list)
print('All commands entered:', cmd_list)
print('Sorted commands:', cmd_list_neat)