import csv

def load_reviews(path: str) -> list[dict]:
    reviews: list[dict] = []

    with open(path, newline="", encoding=""utf-8")
as file:
        reader= csv.DictReader(file)

        for row in reader:
            reviews.append({"Review_ID": int(row["Review_ID"]),"Rating": int(row["Rating"]),"Year_Month": row["Year_Month"].strip(),"Reviewer Location": row["Reviewer Location"].strip(),"Branch": row["Branch"].strip()})

    return reviews

def _norm(s: str) -> str:
    return s.strip().casefold()


def filter_by_park(reviews: list[dict], park: str) -> list[dict]:
    park = park.strip().lower()
    rows = []

    for review in reviews:
        branch = str(review["Branch"]).strip().lower()
        if branch == park:
            rows.append(review)
    return rows


def count_by_park_location(reviews: list[dict], park: str, location: str) -> int:
    park = park.strip().lower()
    location = location.strip().lower()

    count = 0
    for review in reviews:
        if str(review["Branch"]).strip().lower() == park and str(
                review["Reviewer_Location"]).strip().lower() == location:
            count += 1
    return count


def avg_rating_by_park_year(reviews: list[dict], park: str, year: int) -> float | None:
    target_park = _norm(park)

    total = 0.0
    n = 0

    for r in reviews:
        # match Branch (park)
        if _norm(str(r.get("Branch", ""))) != target_park:
            continue

        ym = str(r.get("Year_Month", ""))
        if len(ym) < 4 or not ym[:4].isdigit():
            continue
        y = int(ym[:4])

        if y != year:
            continue

        rating_val = r.get("Rating", r.get("rating"))
        if rating_val is None:
            continue

        try:
            rating = float(rating_val)
        except (TypeError, ValueError):
            continue

        total += rating
        n += 1

    return None if n == 0 else total / n


def count_reviews_per_park(reviews: list[dict]) -> dict[str, int]:
    counts = {}
    for review in reviews:
        park = review["Branch"]
        counts[park] = counts.get(park, 0) + 1
    return counts

def top_locations_by_avg_rating(reviews: list[dict], park: str, n: int = 10) -> list[tuple[str, float]]:

    totals: dict[str, float] = {}
    counts: dict[str, int] = {}

    for review in reviews:
        branch = str(review["Branch"]).strip().lower()
        if branch == park:
            continue

        loc = str(review["Reviewer_Location"]).strip()
        rating = float(review["Rating"])

        totals[loc] = totals.get(loc, 0.0) + rating
        counts[loc] = counts.get(loc, 0) + 1

    avgs = [(loc, totals[loc] / counts[loc]) for loc in totals]
    avgs.sort(key=lambda x: x[1], reverse=True)
    return avgs[:n]



def avg_rating_by_month(reviews: list[dict], park: str) -> dict:
    totals: dict[int, float] = {}
    counts: dict[int, int] = {}

    for review in reviews:
        branch = str(review["Branch"]).strip().lower()
        if branch != park:
            continue

        year_month = str(review["Year_Month"]).strip()
        parts = year_month.split("-")
        if len(parts) != 2:
            continue
        month = int(year_month.split("-")[1])

        rating = float(review["Rating"])

        totals[month] = totals.get(month, 0.0) + rating
        counts[month] = counts.get(month, 0) + 1

    month_avgs = {m: totals[m] / counts[m] for m in totals}
    return dict(sorted(month_avgs.items()))


def avg_score_per_park_by_location(reviews: list[dict]) -> list[tuple[str, str, float]]:
    totals = {}
    counts = {}

    for review in reviews:
        park = str(review["Branch"]).strip()
        location = str(review["Reviewer_Location"]).strip()
        rating = float(review["Rating"])
        key = (park, location)

        totals[key] = totals.get(key, 0) + rating
        counts[key] = counts.get(key, 0) + 1

    result = []
    for (park, location), total in totals.items():
        avg = total / counts[(park, location)]
        result.append((park, location, avg))
    return result