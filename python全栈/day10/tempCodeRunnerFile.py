def show_magicians(lis):
    for name in lis:
        print(name)

def make_great(lis):
    new_lis = []
    for name in lis:
        name = f'the Great {name}'
        new_lis.append(name)
    return new_lis

magicians_lis = ['mack', 'king', 'wang']
new_magicians_lis = make_great(magicians_lis[:])
show_magicians(new_magicians_lis)
show_magicians(magicians_lis)