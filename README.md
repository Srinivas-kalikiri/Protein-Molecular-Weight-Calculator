# Protein Molecular Weight Calculator

A Python tool that computes the molecular weight of a protein or peptide from its amino acid sequence (single-letter codes), along with an amino acid composition breakdown.

## Features
- Computes molecular weight using standard average residue masses
- Validates input sequences and reports invalid amino acid codes with a clear error message
- Reports amino acid composition (counts and percentages)
- Reports average residue weight
- Usable as a CLI tool or imported as a Python module in other projects
- Interactive mode for analyzing multiple sequences in one session

## Tech Stack
- Python 3.9+ (standard library only — no external dependencies)

## Project Structure
```
protein-molecular-weight-calculator/
├── protein_calculator.py       # Core library + CLI
├── tests/
│   └── test_calculator.py      # Unit tests
├── requirements.txt
└── README.md
```

## Setup
```bash
git clone https://github.com/<your-username>/protein-molecular-weight-calculator.git
cd protein-molecular-weight-calculator
```
No external dependencies required — just Python 3.9+.

## Usage

Analyze a sequence directly:
```bash
python protein_calculator.py MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTK
```

Or run in interactive mode:
```bash
python protein_calculator.py
```

### Example Output
```
Sequence: MVLSPADKTNVKAAW
Length: 15 residues
Molecular weight: 1630.92 Da (1.63 kDa)
Average residue weight: 107.53 Da
Amino acid composition:
  A: 3 (20.0%)
  D: 1 (6.7%)
  K: 2 (13.3%)
  L: 1 (6.7%)
  M: 1 (6.7%)
  N: 1 (6.7%)
  P: 1 (6.7%)
  S: 1 (6.7%)
  T: 1 (6.7%)
  V: 2 (13.3%)
  W: 1 (6.7%)
```

## How It Works
Molecular weight is calculated by summing the average residue mass of each amino acid in the sequence (each already adjusted for the water lost during peptide bond formation) and adding a single water molecule (18.02 Da) to account for the free amino and carboxyl termini — the standard method used in protein chemistry.

## Running Tests
```bash
python -m unittest discover tests
```

## Possible Improvements
- Support monoisotopic mass in addition to average mass
- Isoelectric point (pI) estimation
- Accept 3-letter amino acid codes as input
- Hydrophobicity / GRAVY score calculation

## License
MIT
