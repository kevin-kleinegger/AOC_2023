import re

def main():
    with open("testinput.txt", 'r') as file:
        input_str = file.read()
        min_v = 9999999999999999999999
        seeds = [int(x) for x in re.search("seeds:.*?\n", input_str, re.DOTALL).group(0).replace('seeds: ', '').strip().split(' ')]
        for i in range(0, len(seeds), 2):
            for j in range(seeds[i], seeds[i]+seeds[i+1]):
                value = extract_location(input_str, j)
                if(value < min_v):
                    min_v = value
        print(min_v)
       
def extract_location(s_in, seed):
    s2s_map = re.search("seed-to-soil map:.*?soil-to-fertilizer map:", s_in, re.DOTALL).group(0)
    s2f_map = re.search("soil-to-fertilizer map:.*?fertilizer-to-water map:", s_in, re.DOTALL).group(0)
    f2w_map = re.search("fertilizer-to-water map:.*?water-to-light map:", s_in, re.DOTALL).group(0)
    w2l_map = re.search("water-to-light map:.*?light-to-temperature map:", s_in, re.DOTALL).group(0)
    l2t_map = re.search("light-to-temperature map:.*?temperature-to-humidity map:", s_in, re.DOTALL).group(0)
    t2h_map = re.search("temperature-to-humidity map:.*?humidity-to-location map:", s_in, re.DOTALL).group(0)
    h2l_map = re.search("humidity-to-location map:.*?$", s_in, re.DOTALL).group(0)
    soil = map_value(s2s_map, seed)
    fert = map_value(s2f_map, soil)
    water = map_value(f2w_map, fert)
    light = map_value(w2l_map, water)
    temp = map_value(l2t_map, light)
    hum = map_value(t2h_map, temp)
    return map_value(h2l_map, hum)
       

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
