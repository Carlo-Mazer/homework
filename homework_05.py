# Package Loading System Simulation

MAX_PACKAGE_WEIGHT = 20

def get_integer_input(message):
    """Safely get an integer from the user."""
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Error: Please enter a valid number.")


def main():

    max_items = get_integer_input("Enter the maximum number of items to ship: ")

    current_package_weight = 0
    total_weight_sent = 0
    packages_sent = 0
    items_entered = 0

    most_unused_capacity = -1
    package_with_most_unused = 0

    while items_entered < max_items:

        weight = get_integer_input("Enter item weight (1-10 kg, 0 to stop): ")

        # Stop condition
        if weight == 0:
            break

        # Validate weight range
        if weight < 1 or weight > 10:
            print("Error: Weight must be between 1 and 10 kg.")
            continue

        items_entered += 1

        # Check if item fits in current package
        if current_package_weight + weight > MAX_PACKAGE_WEIGHT:

            # Send current package
            packages_sent += 1
            total_weight_sent += current_package_weight

            unused_capacity = MAX_PACKAGE_WEIGHT - current_package_weight

            if unused_capacity > most_unused_capacity:
                most_unused_capacity = unused_capacity
                package_with_most_unused = packages_sent

            # Start new package
            current_package_weight = weight

        else:
            current_package_weight += weight

    # Send last package if it has items
    if current_package_weight > 0:
        packages_sent += 1
        total_weight_sent += current_package_weight

        unused_capacity = MAX_PACKAGE_WEIGHT - current_package_weight

        if unused_capacity > most_unused_capacity:
            most_unused_capacity = unused_capacity
            package_with_most_unused = packages_sent

    total_unused_capacity = (packages_sent * MAX_PACKAGE_WEIGHT) - total_weight_sent

    # Results
    print("\n--- Shipping Summary ---")
    print("Number of packages sent:", packages_sent)
    print("Total weight of packages sent:", total_weight_sent, "kg")
    print("Total unused capacity:", total_unused_capacity, "kg")

    if packages_sent > 0:
        print("Package with most unused capacity:", package_with_most_unused)
        print("Unused capacity in that package:", most_unused_capacity, "kg")


if __name__ == "__main__":
    main()