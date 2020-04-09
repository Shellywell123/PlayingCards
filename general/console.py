def terminal_sizeLinux():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

#changed to this as windows doesnt use fcntl
def terminal_size():
    return 100,100

# print('Number of columns and Rows: ',terminal_size())