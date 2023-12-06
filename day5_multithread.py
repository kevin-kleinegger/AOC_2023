import re
import multiprocessing
from tqdm import tqdm
import sys


def main():
    with open("input.txt", 'r') as file:
        input_str = file.read()
        seeds = [int(x) for x in re.search("seeds:.*?\n", input_str, re.DOTALL).group(0).replace('seeds: ', '').strip().split(' ')]
        size = len(seeds)//5
        t1 = multiprocessing.Process(target=loop_seeds, args=(list(split(seeds, size))[0], input_str))
        t2 = multiprocessing.Process(target=loop_seeds, args=(list(split(seeds, size))[1], input_str))
        t3 = multiprocessing.Process(target=loop_seeds, args=(list(split(seeds, size))[2], input_str))
        t4 = multiprocessing.Process(target=loop_seeds, args=(list(split(seeds, size))[3], input_str))
        t5 = multiprocessing.Process(target=loop_seeds, args=(list(split(seeds, size))[4], input_str))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()



def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

def loop_seeds(seeds, input_str):
    min_v = sys.maxsize
    print(seeds)
    for i in range(0, len(seeds), 2):
        print(i)
        for j in tqdm(range(seeds[i], seeds[i]+seeds[i+1])):
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
