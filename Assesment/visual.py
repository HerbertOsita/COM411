import matplotlib.pyplot as plt

def plot_reviews_per_park_pie(counts: dict[str,int]) -> None:
    plt.figure()
    plt.pie(list(counts.values()), labels=list(counts.keys()), autopct="%1.1f%%")
    plt.title("Reviews per pack")
    plt.show()

def plot_top_locations_bar(top10: list[tuple[str,float]], park: str) -> None:

    locations = [x[0] for x in top10]
    ratings = [x[1] for x in top10]

    plt.figure()
    plt.bar(locations, ratings)
    plt.title(f"Top locations in {park}")
    plt.ylabel("Average Rating")
    plt.xlabel("Location")
    plt.tight_layout()
    plt.show()

import calendar

def plot_avg_by_month_bar(month_avgs: dict, park: str) -> None:

    months = list(month_avgs.keys())
    ratings = list(month_avgs.values())

    months = [calendar.month_abbr[m] for m in months]

    plt.figure()
    plt.bar(months, ratings)
    plt.title(f"Average Rating by Month ({park})")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.xticks(months)
    plt.tight_layout()
    plt.show()