def show_title() -> None:
    print("--------------------------")
    print("Disneyland Review Analyser")
    print("--------------------------")

def show_loaded(count: int) -> None:
    print("Dataset loaded successfully.")
    print(f"Number of rows loaded: {count}")

def show_main_menu() -> None:
    print("Main Menu")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")


def show_view_data_menu() -> None:
    print("\nView Data")
    print("[A] View reviews by park")
    print("[B] Number of reviews by park and reviewer location")
    print("[C] Average score per year by park")
    print("[D] Avg score per park by reviewer location")
    print("[X] Back")


def show_visual_menu() -> None:
    print("\nVisualise Data")
    print("[A] Most reviewed parks")
    print("[B] Park ranking by nationality")
    print("[C] Most popular month by park")
    print("[X] Back")


def get_choice(valid: set[str]) -> str:
    while True:
        choice = input("").strip().upper()
        if choice in valid:
            return choice
        print("Invalid choice, try again.")


def confirm_choice(choice: str) -> None:
    print(f"You have chosen option: {choice}")


def ask_park() -> str:
    return input("Please enter branch name: ").strip()


def ask_location() -> str:
    return input("Please enter reviewer location: ").strip()


def ask_year() -> int:
    while True:
        y = input("Please enter a year: ").strip()
        if y.isdigit():
            return int(y)
        print("The year must be digits only.")


def print_reviews(rows: list[dict]) -> None:
    if not rows:
        print("No matching reviews found.")
        return


    for r in rows[:20]:
        print(f"{r['Review_ID']:>6}  {r['Branch']:<22}  {r['Rating']}  {r['Year_Month']}  {r['Reviewer_Location']}")
    if len(rows) > 20:
        print(f"... ({len(rows)} total)")


def print_count(count: int, park: str, location: str) -> None:
    print(f"{count} reviews for {park} from {location}.")


def print_average(avg: float | None, park: str, year: int) -> None:
    if avg is None:
        print(f"No reviews for {park} in {year}.")
    else:
        print(f"Average rating for {park} in {year}: {avg:.2f}")


def print_avg_score_table(result: list[tuple[str,str,float]]) -> None:
    print(f"{'Park':20} {'Location':20} {'Average Rating'}")
    print("-" * 55)

    for park, location, avg in result:
        print(f"{park:20} {location:20} {avg:.2f}")

def print_todo(msg: str) -> None:
    print(msg)

def goodbye() -> None:
    print("Goodbye!")