from itertools import product


def parse_csv_line(line):
    return [value.strip() for value in line.split(",")]


def read_problem():
    variable_count = int(input().strip())

    domains = [parse_csv_line(input().strip()) for _ in range(variable_count)]
    adjacency = [input().strip().split() for _ in range(variable_count)]

    sample_count = int(input().strip())
    samples = [parse_csv_line(input().strip()) for _ in range(sample_count)]

    return domains, adjacency, samples


def parent_indices(adjacency, variable_index):
    return [
        parent_index
        for parent_index, row in enumerate(adjacency)
        if row[variable_index] == "1"
    ]


def estimate_distribution(variable_index, parents, domains, samples):
    variable_domain = domains[variable_index]

    if not parents:
        denominator = len(samples)
        return [
            count_matches(samples, variable_index, value) / denominator
            if denominator
            else 0.0
            for value in variable_domain
        ]

    probabilities = []
    parent_domains = [domains[parent] for parent in parents]

    for value in variable_domain:
        for parent_values in product(*parent_domains):
            matching_parent_rows = [
                sample
                for sample in samples
                if all(
                    sample[parent] == parent_value
                    for parent, parent_value in zip(parents, parent_values)
                )
            ]

            denominator = len(matching_parent_rows)
            numerator = count_matches(matching_parent_rows, variable_index, value)
            probabilities.append(numerator / denominator if denominator else 0.0)

    return probabilities


def count_matches(samples, variable_index, value):
    return sum(1 for sample in samples if sample[variable_index] == value)


def format_distribution(probabilities):
    return " ".join(f"{probability:.4f}" for probability in probabilities)


def main():
    domains, adjacency, samples = read_problem()

    for variable_index in range(len(domains)):
        parents = parent_indices(adjacency, variable_index)
        probabilities = estimate_distribution(variable_index, parents, domains, samples)
        print(format_distribution(probabilities))


if __name__ == "__main__":
    main()
