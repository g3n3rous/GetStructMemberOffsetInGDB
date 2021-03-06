import gdb

class Offsets(gdb.Command):
    def __init__(self):
        super (Offsets, self).__init__ ('offsets-of', gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        argv = gdb.string_to_argv(arg)
        if len(argv) != 1:
            raise gdb.GdbError('offsets-of takes exactly 1 argument.')

        try:
            stype = gdb.lookup_type(argv[0])
        except:
            print("[!] No such type named {}".format(argv[0]))
            return

        print(argv[0])
        print('{')
        for field in stype.fields():
            print('    +{} --- {} {}'.format(hex(field.bitpos // 8), field.type, field.name))
        print('}')

Offsets()
