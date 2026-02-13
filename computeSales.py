# pylint: disable=invalid-name
# Module name required by assignment specification (Req 4).
"""
Compute total sales from a product catalogue and sales records.

Usage:
    python computeSales.py priceCatalogue.json salesRecord.json
"""

import json
import sys
import time


def load_json_file(file_path):
    """Load and parse a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def build_price_catalogue(products):
    """Build a dictionary mapping product title to price."""
    catalogue = {}
    for product in products:
        title = product.get("title", "")
        price = product.get("price", 0)
        catalogue[title] = price
    return catalogue


def compute_total_sales(catalogue, sales):
    """Compute total cost for all sales, handling invalid data."""
    grand_total = 0.0
    sale_totals = {}

    for record in sales:
        sale_id = record.get("SALE_ID", "Unknown")
        product_name = record.get("Product", "")
        quantity = record.get("Quantity", 0)

        if product_name not in catalogue:
            print(
                f"  Error: Product '{product_name}' "
                f"is not in the catalogue. Skipping."
            )
            continue

        if not isinstance(quantity, (int, float)):
            print(
                f"  Error: Invalid quantity ({quantity}) "
                f"for '{product_name}'. Skipping."
            )
            continue

        price = catalogue[product_name]
        cost = price * quantity

        if sale_id not in sale_totals:
            sale_totals[sale_id] = {
                "items": [],
                "total": 0.0,
            }

        sale_totals[sale_id]["items"].append({
            "product": product_name,
            "quantity": quantity,
            "unit_price": price,
            "cost": cost,
        })
        sale_totals[sale_id]["total"] += cost
        grand_total += cost

    return grand_total, sale_totals


def format_results(grand_total, sale_totals, elapsed_time):
    """Format the results as a human-readable string."""
    lines = []
    lines.append("=" * 40)
    lines.append("SALES REPORT")
    lines.append("=" * 40)

    for sale_id in sorted(sale_totals.keys()):
        sale = sale_totals[sale_id]
        items_count = len(sale["items"])
        lines.append(
            f"  SALE {sale_id:<5} "
            f"({items_count} items)  "
            f"${sale['total']:.2f}"
        )

    lines.append("=" * 40)
    lines.append(f"GRAND TOTAL:  ${grand_total:.2f}")
    lines.append(f"Time elapsed: {elapsed_time:.4f} seconds")
    lines.append("=" * 40)

    return "\n".join(lines)


def main():
    """Main function to compute sales."""
    if len(sys.argv) != 3:
        print(
            "Usage: python computeSales.py "
            "priceCatalogue.json salesRecord.json"
        )
        sys.exit(1)

    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    start_time = time.time()

    try:
        products = load_json_file(catalogue_file)
    except (FileNotFoundError, json.JSONDecodeError) as err:
        print(f"Error loading catalogue file: {err}")
        sys.exit(1)

    try:
        sales = load_json_file(sales_file)
    except (FileNotFoundError, json.JSONDecodeError) as err:
        print(f"Error loading sales file: {err}")
        sys.exit(1)

    catalogue = build_price_catalogue(products)
    grand_total, sale_totals = compute_total_sales(catalogue, sales)

    elapsed_time = time.time() - start_time

    report = format_results(grand_total, sale_totals, elapsed_time)
    print(report)

    with open("SalesResults.txt", 'w', encoding='utf-8') as out_file:
        out_file.write(report + "\n")

    print("\nResults saved to SalesResults.txt")


if __name__ == "__main__":
    main()
