import numpy as np


def prepare_qubits(num_qubits):
    return np.random.randint(0, 4, num_qubits)


def measure_qubits(qubits):
    bases = np.random.randint(0, 2, len(qubits))
    measurements = []

    for idx, qubit in enumerate(qubits):
        if bases[idx] == qubit % 2:
            measurements.append(qubit)
        else:
            measurements.append(-1)
    return bases, measurements


def compare_bases_and_filter_key(alice_bases, bob_bases, qubits):
    return [qubits[i] % 2 for i in range(len(qubits)) if alice_bases[i] == bob_bases[i]]


def eavesdrop_qubits(qubits):
    eve_bases = np.random.randint(0, 2, len(qubits))
    eavesdropped_qubits = []

    for idx, qubit in enumerate(qubits):
        if eve_bases[idx] == qubit % 2:
            eavesdropped_qubits.append(qubit)
        else:
            eavesdropped_qubits.append(-1)
    return eavesdropped_qubits


def calculate_error_rate(alice_key, bob_key):
    errors = sum([1 for a, b in zip(alice_key, bob_key)
                 if a != b and a != -1 and b != -1])
    valid_bits = sum(
        [1 for a, b in zip(alice_key, bob_key) if a != -1 and b != -1])
    return errors / valid_bits if valid_bits > 0 else 0


def main():
    num_qubits = 100

    # Alice prepares qubits and sends them to Bob
    alice_qubits = prepare_qubits(num_qubits)

    # Eve eavesdrops on the qubits
    eavesdropped_qubits = eavesdrop_qubits(alice_qubits)

    # Bob measures the qubits received
    bob_bases, bob_measurements = measure_qubits(eavesdropped_qubits)

    # Alice and Bob compare bases and filter their keys
    alice_bases = [qubit % 2 for qubit in alice_qubits]
    alice_key = compare_bases_and_filter_key(
        alice_bases, bob_bases, alice_qubits)
    bob_key = compare_bases_and_filter_key(
        alice_bases, bob_bases, bob_measurements)

    # Calculate the error rate
    error_rate = calculate_error_rate(alice_key, bob_key)

    print("Alice's qubits: ", alice_qubits)
    print("Eavesdropped qubits: ", eavesdropped_qubits)
    print("Bob's bases:    ", bob_bases)
    print("Bob's measurements: ", bob_measurements)
    print("Alice's key:    ", alice_key)
    print("Bob's key:      ", bob_key)
    print("Error rate:     ", error_rate)


if __name__ == "__main__":
    main()
