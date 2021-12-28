def generator(*args):
    gen_list = [gen_holder(name) for name in args]
    while gen_list:
        for i in gen_list:
            try:
                yield next(i)
            except StopIteration:
                gen_list.remove(i)


def gen_holder(fname):
    with open(fname, encoding='utf-8') as fp:
        for line in fp:
            yield line.strip()

for line in generator('stih1.txt','stih2.txt','stih3.txt'):
    print(f'Ctroka {line}')

