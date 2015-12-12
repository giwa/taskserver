import glob
from workers.wakachi import Wakachi


wakachi = Wakachi()

def read_raw_file():
    for l in glob.glob("./data/raw_text/*"):
        yield l


def wakachiwake(file_path):
    """ Parse plain text with wakachiwake
    """
    r = []
    with open(file_path) as f:
        for l in f:
            w = list(wakachi.parse(l))
            if w:
                r.extend(w)
    return r


def do_wakachi():
    for f in read_raw_file():
        wakachi_result = wakachiwake(f)
        hashed_uri = f.split("/")[-1]
        with open("./data/wakachi/" + hashed_uri, "w") as wakachi_f:
            for waka in wakachi_result:
                wakachi_f.write(waka)
                wakachi_f.write("\n")


if __name__ == "__main__":
    do_wakachi()
