from timeout.indenter import Indenter


def print_venues(venues):

    if venues["good_venues"]:
        with Indenter() as indent:
            indent.print("Places to go:")
            with indent:
                for venue in venues["good_venues"]:
                    indent.print(f"- {venue}")

    if venues["bad_venues"]:
        with Indenter() as indent:
            indent.print("Places to avoid:")
            with indent:
                for venue, issues in venues["bad_venues"].items():
                    indent.print(f"- {venue}")
                    with indent:
                        for issue in issues:
                            indent.print(f"- {issue}")
