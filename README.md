# Assignment 4a: NRIC

**Note:** This is the same as Assignment 3a, but this time you can use lists and loops.

The Singapore NRIC number is made up of a leading letter, 7 digits, and a check digit calculated from the first 7 digits using the modulus eleven method.

The steps involved to obtain the check digit are:

1. Multiply each digit in the NRIC number by its weight (See Table 1).
2. Add the products from Step 1 together.
3. If the first letter is T or G, add 4 to the total in Step 2.
4. Divide the resulting sum in Step 2 by 11 and keep the remainder.
5. Check the check digit against the table to obtain the alphabet (See Table 2).

The following table shows the weight for each digit of the NRIC number:

    ┍━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━┑
    │Digit sequence  │ 1  2  3  4  5  6  7 │
    ┝━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━┥
    │Digit weight    │ 2  7  6  5  4  3  2 │
    ┕━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━┙
    Table 1: Weight table for each NRIC digit

The following table is used to change the check digit into the corresponding alphabet.

    ┍━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
    │Check Digit     │ 0  1  2  3  4  5  6  7  8  9 10  │
    ┝━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥
    │Starts with S/T │ J  Z  I  H  G  F  E  D  C  B  A  │ 
    ┝━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥
    │Starts with F/G │ X  W  U  T  R  Q  P  N  M  L  K  │ 
    ┕━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
    Table 2: Check digit to alphabet conversion

### Validation reporting

The validation report should inform the user whether the NRIC string is valid. No reason needs to be provided.

Write program code to:

1. validate the check digit of the NRIC number,
2. Print the result of the NRIC validation (`valid` or `invalid` only)

### Expected output

    The input NRIC is S1234567A.
    NRIC is invalid.
    The input NRIC is S1234567D.
    NRIC is valid.
    The input NRIC is <your NRIC>.
    NRIC is valid.


# Submission

Before submission, run the tests on your final code.
