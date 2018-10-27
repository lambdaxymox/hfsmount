import sys
import subprocess


def usage():
    """
    Print out the usage of the script with an example.
    """
    return 'USAGE: hfsmount /path/to/hfs/plus/drive/'


def main():
    if len(sys.argv) != 2:
        print(usage())

        # An exit code of 2 is standard unix convention.
        sys.exit(2)

    hfs_drive = sys.argv[1]
    return_code = subprocess.run(
        ['mount', '-t', 'hfsplus', '-o', 'force,remount,rw', hfs_drive]
    )

    sys.exit(return_code)


if __name__ == 'main':
    main()
else:
    main()
