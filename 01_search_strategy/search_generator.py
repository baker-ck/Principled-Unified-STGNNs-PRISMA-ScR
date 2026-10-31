from itertools import product
import yaml
import pandas as pd
from pathlib import Path


OUTPUT = Path("output")
OUTPUT.mkdir(exist_ok=True)


def normalize_term(term, db):
    """
    Apply database-specific wildcard handling.
    """

    wildcard = db.get("wildcard", "*")

    if not db.get("use_wildcard", True):
        term = term.rstrip(wildcard)

    return term


def quote(term, q, db):
    """
    Apply database-specific quoting rules.
    """

    wildcard = db.get("wildcard", "*")

    # Database supports wildcard but forbids
    # wildcard inside quoted phrases (ACM)
    if (
        db.get("wildcard_no_quotes", False)
        and wildcard in term
    ):
        return term

    if " " in term:
        return f"{q}{term}{q}"

    return term


def format_term(term, db):
    """
    Format an individual term.
    """
    term = normalize_term(term, db)
    return quote(term, db["quote"], db)


def or_group(terms, db):
    """
    Create OR group for a concept.
    Handles ACM field-first expansion.
    """

    formatted_terms = [
        format_term(term, db)
        for term in terms
    ]

    # ACM: expand fields around the entire concept group
    if "field_templates" in db:

        fields = []

        for template in db["field_templates"]:
            field_terms = (
                f" {db['or']} ".join(formatted_terms)
            )

            fields.append(
                template.format(term=field_terms)
            )

        return (
            "("
            + f" {db['or']} ".join(fields)
            + ")"
        )

    # Existing behavior for IEEE / Scopus
    return (
        "("
        + f" {db['or']} ".join(formatted_terms)
        + ")"
    )

with open("concepts.yaml") as f:
    concepts = yaml.safe_load(f)

with open("databases.yaml") as f:
    databases = yaml.safe_load(f)


concept_names = list(concepts.keys())

groups = [
    concepts[name]
    for name in concept_names
]


records = []


for db_name, db in databases.items():

    queries = []

    for combination in product(*groups):

        pieces = []

        metadata = {}

        for concept_name, option in zip(concept_names, combination):

            metadata[concept_name] = option["name"]

            pieces.append(
                or_group(
                    option["terms"],
                    db
                )
            )

        search = f" {db['and']} ".join(pieces)

        # Preserve existing Scopus-style wrapping
        # Only applies when no field_template is used
        if (
            "field_template" not in db
            and "field_templates" not in db
            and db.get("field", "") != ""
        ):
            search = (
                f"{db['field']}"
                f"{search}"
                f"{db['field_close']}"
            )

        queries.append(search)

        records.append(
            {
                "Database": db_name,
                **metadata,
                "Search": search
            }
        )


    with open(
        OUTPUT / f"{db_name.lower()}.txt",
        "w"
    ) as f:
        f.write("\n\n".join(queries))


pd.DataFrame(records).to_csv(
    OUTPUT / "all_searches.csv",
    index=False
)


print("Finished.")
