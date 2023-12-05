import re

def main():
    with open("input.txt", 'r') as file:
        input_str = file.readlines()
        file.seek(0)
        input_str_2 = file.read()
        #print(input_str_2)
        seeds = get_seeds([int(x) for x in input_str[0].replace('seeds: ', '').strip().split(' ')])
        s2s_map = re.search("seed-to-soil map:.*?soil-to-fertilizer map:", input_str_2, re.DOTALL).group(0)
        s2f_map = re.search("soil-to-fertilizer map:.*?fertilizer-to-water map:", input_str_2, re.DOTALL).group(0)
        f2w_map = re.search("fertilizer-to-water map:.*?water-to-light map:", input_str_2, re.DOTALL).group(0)
        w2l_map = re.search("water-to-light map:.*?light-to-temperature map:", input_str_2, re.DOTALL).group(0)
        l2t_map = re.search("light-to-temperature map:.*?temperature-to-humidity map:", input_str_2, re.DOTALL).group(0)
        t2h_map = re.search("temperature-to-humidity map:.*?humidity-to-location map:", input_str_2, re.DOTALL).group(0)
        h2l_map = re.search("humidity-to-location map:.*?$", input_str_2, re.DOTALL).group(0)
        locations = []
        for seed in seeds:
            soil = map_value(s2s_map, seed)
            fert = map_value(s2f_map, soil)
            water = map_value(f2w_map, fert)
            light = map_value(w2l_map, water)
            temp = map_value(l2t_map, light)
            hum = map_value(t2h_map, temp)
            locations.append(map_value(h2l_map, hum))
        print(min(locations))
       
def get_seeds(s_in):
    seeds = []
    for i in range(0, len(s_in), 2):
        for j in range(s_in[i], s_in[i]+s_in[i+1]):
            seeds.append(j)
    return seeds
        

def map_value(m, i):
    m = list(m.split('\n'))
    for line in m:
        if len(line) > 0 and line[0].isnumeric():
            d, s, r = [int(x) for x in line.split(' ')]
            if i >= s and i <= s+r:
                return i + (d-s)
    return i

if __name__ == "__main__":
    main()      
