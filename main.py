from map import Map

def main():
    new_map = Map("The Cavern", "a dank and dirty cave full of worms")
    print(new_map)
    new_map.generate_map()

if __name__ == '__main__':
    main()