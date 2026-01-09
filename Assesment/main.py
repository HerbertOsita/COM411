import tui
import process
import visual

DATA_FILE = "data/disneyland_reviews.csv"

def view_data_menu(reviews: list[dict]) -> None :
    while True:
        tui.show_view_data_menu()
        choice = tui.get_choice({"A", "B", "C", "D", "X"})
        tui.confim_choice(choice)

        if choice == "A":
            park = tui.ask_park()
            rows = process.filter_by_park(reviews, park)
            tui.print_reviews(rows)

        elif choice == "B":
            park = tui.ask_park()
            location = tui.ask_location()
            count = process.count_by_park_location(reviews, park, location)
            tui.print_count(count, park, location)

        elif choice == "C":
            park = tui.ask_park()
            year = tui.ask_year()
            avg = process.avg_rating_by_park_year(reviews, park, year)
            tui.print_average(avg, park, year)

        elif choice == "D":
            result = process.avg_score_per_park_by_location(reviews)
            tui.print_avg_score_table(result)

        elif choice == "X":
            return

def visual_menu(reviews: list[dict]) -> None:

    while True:
        tui.show_visual_menu()
        choice = tui.get_choice({"A", "B", "C", "X"})
        tui.confirm_choice(choice)

        if choice == "A":
            counts = process.count_reviews_per_park(reviews)
            visual.plot_reviews_per_park_pie(counts)

        elif choice == "B":
            park = tui.ask_park()
            top10 = process.top_locations_by_avg_rating(reviews, park, n=10)
            visual.plot_top_locations_bar(top10, park)

        elif choice == "C":
            park = tui.ask_park()
            month_avgs = process.avg_rating_by_month(reviews, park)
            visual.plot_avg_by_month_bar(month_avgs, park)

        elif choice == "X":
            return

def main() -> None:
    tui.show_title()

    reviews = process.load_reviews(DATA_FILE)
    tui.show_loaded(len(reviews))

    while True:
        tui.show_main_menu()
        choice = tui.get_choice({"A", "B", "X"})
        tui.confirm_choice(choice)

        if choice == "A":
            view_data_menu(reviews)

        elif choice == "B":
            visual_menu(reviews)

        elif choice == "X":
            tui.goodbye()
            break

if __name__ == "__main__":
    main()