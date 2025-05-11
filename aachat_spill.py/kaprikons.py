import sys


def kaprekar_step(n, num_digits=4):
    """
    Utfør ett Kaprekar-steg på tallet n med num_digits sifre.
    Returnerer en tuple (next_value, desc_str, asc_str).
    """
    s = str(n).zfill(num_digits)
    desc = ''.join(sorted(s, reverse=True))
    asc = ''.join(sorted(s))
    next_val = int(desc) - int(asc)
    return next_val, desc, asc


def run_kaprekar(n, num_digits=4):
    """
    Kjører Kaprekars algoritme inntil konstant eller fast punkt nås.
    Returnerer en liste av tuples (desc, asc, next_val) for hvert steg.
    """
    sequence = []
    current = n

    while True:
        next_val, desc, asc = kaprekar_step(current, num_digits)
        sequence.append((desc, asc, next_val))
        # Stopp hvis vi har nådd fast punkt
        if next_val == current:
            break
        current = next_val

    return sequence


def main():
    num_digits = 4
    prompt = f"Skriv inn et {num_digits}-sifret tall: "
    try:
        n_input = input(prompt)
        n = int(n_input)
    except ValueError:
        print("Ugyldig tall.")
        sys.exit(1)

    # Sjekk at input har riktig antall sifre
    if not (0 <= n < 10**num_digits):
        print(f"Tallet må være mellom 0 og {10**num_digits - 1}.")
        sys.exit(1)

    # Kjør algoritmen
    seq = run_kaprekar(n, num_digits)

    print(f"Kjører Kaprekar-algoritme for {num_digits}-sifret tall {n}:")
    for i, (desc, asc, nxt) in enumerate(seq, start=1):
        print(f"Steg {i}: {desc} - {asc} = {nxt}")

    konstant = seq[-1][2]
    steg = len(seq)
    print(f"Nådd Kaprekar-konstant {konstant} etter {steg} steg.")


if __name__ == '__main__':
    main()
