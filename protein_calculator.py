"""
Protein Molecular Weight Calculator
Computes the molecular weight of a protein/peptide from its amino acid
sequence (single-letter codes), using standard average residue masses.
"""

import argparse

# Average molecular weight of each amino acid residue in Daltons - i.e. the
# mass already reduced by one water molecule lost during peptide bond formation.
RESIDUE_WEIGHTS = {
    'A': 71.0788,   # Alanine
    'R': 156.1875,  # Arginine
    'N': 114.1038,  # Asparagine
    'D': 115.0886,  # Aspartic acid
    'C': 103.1388,  # Cysteine
    'E': 129.1155,  # Glutamic acid
    'Q': 128.1307,  # Glutamine
    'G': 57.0519,   # Glycine
    'H': 137.1411,  # Histidine
    'I': 113.1594,  # Isoleucine
    'L': 113.1594,  # Leucine
    'K': 128.1741,  # Lysine
    'M': 131.1926,  # Methionine
    'F': 147.1766,  # Phenylalanine
    'P': 97.1167,   # Proline
    'S': 87.0782,   # Serine
    'T': 101.1051,  # Threonine
    'W': 186.2132,  # Tryptophan
    'Y': 163.1760,  # Tyrosine
    'V': 99.1326,   # Valine
}

WATER_WEIGHT = 18.0153  # Da - added once to account for the free terminal H and OH


class InvalidSequenceError(ValueError):
    pass


def clean_sequence(seq):
    return "".join(seq.split()).upper()


def validate_sequence(seq):
    if not seq:
        raise InvalidSequenceError("Sequence is empty.")
    invalid_chars = sorted(set(seq) - set(RESIDUE_WEIGHTS.keys()))
    if invalid_chars:
        raise InvalidSequenceError(
            f"Sequence contains invalid amino acid code(s): {', '.join(invalid_chars)}. "
            f"Valid codes: {', '.join(sorted(RESIDUE_WEIGHTS.keys()))}"
        )
    return True


def molecular_weight(seq):
    """Total molecular weight of the peptide/protein in Daltons."""
    seq = clean_sequence(seq)
    validate_sequence(seq)
    residue_total = sum(RESIDUE_WEIGHTS[aa] for aa in seq)
    return round(residue_total + WATER_WEIGHT, 2)


def amino_acid_composition(seq):
    """Returns a dict of {amino_acid: count} for the sequence."""
    seq = clean_sequence(seq)
    validate_sequence(seq)
    composition = {}
    for aa in seq:
        composition[aa] = composition.get(aa, 0) + 1
    return composition


def average_residue_weight(seq):
    seq = clean_sequence(seq)
    validate_sequence(seq)
    return round(sum(RESIDUE_WEIGHTS[aa] for aa in seq) / len(seq), 2)


def analyze(seq):
    seq = clean_sequence(seq)
    mw = molecular_weight(seq)
    composition = amino_acid_composition(seq)
    print(f"\nSequence: {seq}")
    print(f"Length: {len(seq)} residues")
    print(f"Molecular weight: {mw} Da ({round(mw / 1000, 2)} kDa)")
    print(f"Average residue weight: {average_residue_weight(seq)} Da")
    print("Amino acid composition:")
    for aa, count in sorted(composition.items()):
        print(f"  {aa}: {count} ({round(count / len(seq) * 100, 1)}%)")


def main():
    parser = argparse.ArgumentParser(
        description="Calculate the molecular weight of a protein from its amino acid sequence."
    )
    parser.add_argument("sequence", nargs="?", help="Amino acid sequence, e.g. MVLSPADKTNVKAAW")
    args = parser.parse_args()

    if args.sequence:
        try:
            analyze(args.sequence)
        except InvalidSequenceError as e:
            print(f"Error: {e}")
    else:
        print("Protein Molecular Weight Calculator")
        print("Enter an amino acid sequence (or 'exit' to quit).")
        while True:
            seq = input("\nSequence: ").strip()
            if seq.lower() in ("exit", "quit"):
                break
            try:
                analyze(seq)
            except InvalidSequenceError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()
