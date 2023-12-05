def main():
	with open("input.txt", 'r') as file:
		part1_sum=0
		part2_sum=0
		file = file.readlines()
		for line in file:
			line = line.strip()
			res_first, res_second = line[:len(line)//2], line[len(line)//2:] 
			for c in res_first:
				if c in res_second:
					part1_sum += get_priority(c)
					break
		for i in range(0, len(file), 3):
			for c in range(len(file[i])):
				if (file[i][c] in file[i+1] and file[i][c] in file[i+2]):
					part2_sum += get_priority(file[i][c])
					break
		print(part1_sum)
		print(part2_sum)

def get_priority(c):
	if(c.isupper()):
		return ord(c) - 38
	else:
		return ord(c) - 96

if __name__ == "__main__":
	main()
