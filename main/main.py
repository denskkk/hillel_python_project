from pympler import asizeof


def find_in_file(file_name: str, pattern: str) -> list[str]:
    results = []
    with open(file_name, "r") as file:
        for word in file.readlines():
            if pattern in word:
                results.append(word)

    return results


input = input("Enter pattern: ")
results = find_in_file(
    file_name="hillel_python_project/main/rockyou.txt",
    pattern=input,
)

with open("result.txt", "w") as file:
    for resultfile in results:
        file.write(resultfile + "\n")

num_lines = len(results)
print(f"Number of lines in the file: {num_lines}")

# Get the total size of the file
total_size = asizeof.asizeof(results)
print(f"Total size of the file (in bytes): {total_size}")
