#!/usr/bin/env python3


# Visualizacion histograma de frecuencias de un texto largo.
import matplotlib.pyplot as plt
import string

# Take frecuency of letters
def count_letters(text: str, vocab: str = string.ascii_lowercase) -> dict[str, int]:
    counts = {ch: 0 for ch in vocab}
    for c in text.lower():
        if c in counts:
            counts[c] += 1
    return counts

# Make hist with frecuency of letters
def plot_histogram(text: str):
    counts = count_letters(text)
    letters = list(counts.keys())
    values = list(counts.values())

    plt.bar(letters, values)
    plt.xlabel("Letters")
    plt.ylabel("Count")
    plt.title("Letter Frequency")
    plt.show()

def main():
    tex = input("Put text here").lower()
    voc = input("Put vocabulary here, left blank to use default").lower()
    if voc != "":
        plot_histogram(tex,voc)
    else:
        plot_histogram(tex)

if __name__ == "__main__":
    main()