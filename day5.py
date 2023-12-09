def main():
    with open("day5.txt", 'r') as file:
        input = file.read().strip()
        print(part1(input))
        print(part2(input))

def get_maps(maps):
    all_maps = []
    for m in maps:
        m = m.split('\n')[1:]
        m = [[int(x) for x in i.split(' ')] for i in m]
        all_maps.append(m)
    return all_maps

def apply_map(seed, map):
    for d, s, r in map:
        if seed >= s and seed <= s+r:
            return seed + (d-s)
    return seed

def apply_range(ranges, map):
    final = []
    for d, s, r in map:
        need_work = []
        src_end = s + r
        while(ranges):
            (start, end) = ranges.pop()
            before = (start, min(s, end))
            inner = (max(start,s), min(src_end, end))
            after = (max(src_end, start), end)
            if(before[1] > before[0]):
                need_work.append(before)
            if(inner[1] > inner[0]):
                final.append((inner[0]-s+d, inner[1]-s+d))
            if(after[1] > after[0]):
                need_work.append(after)
        ranges = need_work
    return final+ranges

def apply_maps(seed, maps):
    new_val = seed
    for m in maps:
        new_val = apply_map(new_val, m)
    return new_val

def part1(input):
    seeds, *maps = input.split('\n\n')
    seeds = [int(x) for x in seeds.split(':')[1].split()]
    maps = get_maps(maps)
    locations = []
    for s in seeds:
        locations.append(apply_maps(s, maps))
    return min(locations)

def part2(input):
    seeds, *maps = input.split('\n\n')
    seeds = [int(x) for x in seeds.split(':')[1].split()]
    maps = get_maps(maps)
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))
    outputs = []
    for ss, ez in seed_pairs:
        range = [(ss, ss+ez)]
        for m in maps:
            range = apply_range(range, m)
        outputs.append(min(range)[0])
    return min(outputs)

if __name__ == "__main__":
    main()