# WAP to represent the following graphs using a dictionary.

Tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}


G = {
    'Biratnagar': {
        'Itahari': 22,
        'Biratchowk': 30,
        'Rangeli': 25
    },
    'Itahari': {
        'Biratnagar': 22,
        'Dharan': 20,
        'Biratchowk': 11
    },
    'Dharan': {
        'Itahari': 20
    },
    'Biratchowk': {
        'Biratnagar': 30,
        'Itahari': 11,
        'Kanepokhari': 10
    },
    'Rangeli': {
        'Biratnagar': 25,
        'Kanepokhari': 25,
        'Urlabari': 40
    },
    'Kanepokhari': {
        'Biratchowk': 10,
        'Rangeli': 25,
        'Urlabari': 12
    },
    'Urlabari': {
        'Rangeli': 40,
        'Kanepokhari': 12,
        'Damak': 6
    },
    'Damak': {
        'Urlabari': 6
    },
}

def main():
    print(f'a) tree = {Tree}')
    print(f'b) graph = {G}')

if __name__ == "__main__":
    main()